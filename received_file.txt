# app.py
import argparse
from gui import run_gui
from network import run_receiver

def main():
    parser = argparse.ArgumentParser(description="Network-based Data Compression Tool")
    parser.add_argument('--mode', type=str, choices=['send', 'receive'], required=False, help="Run in send or receive mode")
    parser.add_argument('--host', type=str, default='127.0.0.1', help="IP address of the receiver")
    parser.add_argument('--port', type=int, default=65432, help="Port to connect to")
    args = parser.parse_args()

    if args.mode == 'receive':
        run_receiver(args.host, args.port)  # This should start the receiver only
    else:
        run_gui()  # This should start the GUI

if __name__ == "__main__":
    main()
