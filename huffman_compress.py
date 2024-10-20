import heapq
from collections import defaultdict


class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def build_huffman_tree(data: bytes) -> Node:
    frequency = defaultdict(int)
    for byte in data:
        frequency[byte] += 1

    heap = [Node(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]


def build_codes(node: Node, prefix: str = "", codebook: dict = {}) -> dict:
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        build_codes(node.left, prefix + "0", codebook)
        build_codes(node.right, prefix + "1", codebook)
    return codebook


def huffman_compress(data: bytes) -> tuple:
    huffman_tree = build_huffman_tree(data)
    codes = build_codes(huffman_tree)
    compressed = ''.join(codes[byte] for byte in data)
    # Convert binary string to bytes
    # Ensure that the length of the binary string is divisible by 8
    padded_length = (len(compressed) + 7) // 8 * 8
    compressed = compressed.ljust(padded_length, '0')  # Padding with '0's to make it byte-aligned
    return int(compressed, 2).to_bytes(padded_length // 8, byteorder='big'), codes


def huffman_decompress(data: bytes, codes: dict) -> bytes:
    # Reverse the codebook to decode the binary string
    reverse_codes = {v: k for k, v in codes.items()}
    compressed_str = bin(int.from_bytes(data, byteorder='big'))[2:]  # Convert to binary string

    # Ensure the compressed string is zero-padded
    current_code = ""
    decompressed = bytearray()

    for bit in compressed_str:
        current_code += bit
        if current_code in reverse_codes:
            decompressed.append(reverse_codes[current_code])
            current_code = ""

    return bytes(decompressed)
