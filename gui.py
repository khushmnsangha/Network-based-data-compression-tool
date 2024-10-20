import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from compression import compress_data, decompress_data
from network import send_data, receive_data
from visualization import plot_compression_stats

class NetworkCompressionToolGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Network-Based Data Compression Tool")
        self.root.geometry("400x400")  # Set a larger size for the window
        self.file_path = ""
        self.algorithm = "zlib"
        self.create_widgets()

    def create_widgets(self):
        # Frame for File Selection
        file_frame = ttk.LabelFrame(self.root, text="File Operations", padding=(10, 10))
        file_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # File Selection Button
        ttk.Button(file_frame, text="Select File", command=self.select_file).grid(row=0, column=0, pady=10)

        # Compression Algorithm Dropdown
        self.algorithm_var = tk.StringVar(value="zlib")
        ttk.Label(file_frame, text="Select Compression Algorithm:").grid(row=1, column=0, pady=5)
        ttk.OptionMenu(file_frame, self.algorithm_var, "zlib", "zlib", "gzip", "bz2").grid(row=2, column=0, pady=5)

        # Frame for Send/Receive
        action_frame = ttk.LabelFrame(self.root, text="Data Transmission", padding=(10, 10))
        action_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Send Data Button
        ttk.Button(action_frame, text="Send Data", command=self.send_data).grid(row=0, column=0, padx=10, pady=10)

        # Receive Data Button
        ttk.Button(action_frame, text="Receive Data", command=self.receive_data).grid(row=0, column=1, padx=10, pady=10)

        # Visualization Button
        ttk.Button(action_frame, text="Visualize Compression", command=self.visualize).grid(row=1, column=0, columnspan=2, pady=10)

    def select_file(self):
        self.file_path = filedialog.askopenfilename(title="Select a file")
        if self.file_path:
            messagebox.showinfo("File Selected", f"File: {self.file_path}")

    def send_data(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file first")
            return
        try:
            with open(self.file_path, 'rb') as f:
                original_data = f.read()
            compressed_data = compress_data(original_data, self.algorithm_var.get())
            send_data("127.0.0.1", 65432, compressed_data)  # Ensure the receiver is running on this IP/Port
            messagebox.showinfo("Success", "Data sent successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send data: {str(e)}")

    def receive_data(self):
        try:
            received_data = receive_data("127.0.0.1", 65432)  # Ensure receiver is running
            decompressed_data = decompress_data(received_data, self.algorithm_var.get())
            with open("received_file.txt", 'wb') as f:
                f.write(decompressed_data)
            messagebox.showinfo("Success", "Data received and decompressed successfully")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to receive data: {str(e)}")

    def visualize(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a file first")
            return
        try:
            plot_compression_stats(self.file_path, self.algorithm_var.get())
        except Exception as e:
            messagebox.showerror("Error", f"Failed to visualize: {str(e)}")

    def run(self):
        self.root.mainloop()

# To start the GUI
def run_gui():
    gui_app = NetworkCompressionToolGUI()
    gui_app.run()

# Uncomment the line below to run the GUI
# run_gui()
