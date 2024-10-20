def rle_compress(data: bytes) -> bytes:
    """Compress data using Run-Length Encoding (RLE)."""
    compressed = bytearray()
    count = 1

    for i in range(1, len(data)):
        if data[i] == data[i - 1]:
            count += 1
        else:
            compressed.append(data[i - 1])
            compressed.append(count)
            count = 1

    # Append the last value
    compressed.append(data[-1])
    compressed.append(count)

    return bytes(compressed)

def rle_decompress(data: bytes) -> bytes:
    """Decompress data using Run-Length Encoding (RLE)."""
    decompressed = bytearray()

    for i in range(0, len(data), 2):
        value = data[i]
        count = data[i + 1]
        decompressed.extend([value] * count)

    return bytes(decompressed)
