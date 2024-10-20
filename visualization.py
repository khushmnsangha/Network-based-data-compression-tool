import matplotlib.pyplot as plt
import os
from compression import compress_data

def plot_compression_stats(file_path: str, algorithm: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist")

    with open(file_path, 'rb') as f:
        original_data = f.read()

    original_size = len(original_data)
    compressed_data = compress_data(original_data, algorithm)
    compressed_size = len(compressed_data)

    # Print sizes for debugging
    print(f"Original Size: {original_size} bytes")
    print(f"Compressed Size: {compressed_size} bytes")

    # Plot Original vs Compressed Size
    plt.figure(figsize=(8, 5))  # Optional: set the figure size for better visibility
    plt.bar(["Original Size", "Compressed Size"], [original_size, compressed_size], color=['blue', 'orange'])
    plt.title(f"Compression Stats using {algorithm}")
    plt.ylabel("Size (bytes)")
    plt.ylim(0, max(original_size, compressed_size) * 1.1)  # Optional: set y-axis limit for better view
    plt.grid(axis='y')  # Optional: add gridlines for easier reading
    plt.show()

# Example usage
# plot_compression_stats('path_to_your_file.txt', 'zlib')
