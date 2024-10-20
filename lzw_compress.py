def lzw_compress(data: bytes) -> list:
    """Compress data using Lempel-Ziv-Welch (LZW)."""
    dictionary = {bytes([i]): i for i in range(256)}
    current_string = bytearray()
    compressed = []

    for byte in data:
        current_string.append(byte)
        if current_string not in dictionary:
            # Add new entry to the dictionary
            dictionary[current_string] = len(dictionary)
            # Output the code for the previous string
            compressed.append(dictionary[current_string[:-1]])
            # Start a new current string
            current_string = bytearray([byte])

    if current_string:
        compressed.append(dictionary[current_string])

    return compressed

def lzw_decompress(compressed: list) -> bytes:
    """Decompress data using Lempel-Ziv-Welch (LZW)."""
    dictionary = {i: bytes([i]) for i in range(256)}
    current_code = compressed[0]
    current_string = bytearray(dictionary[current_code])
    decompressed = bytearray(current_string)

    for code in compressed[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == len(dictionary):
            entry = current_string + current_string[:1]

        decompressed.extend(entry)

        # Add new entry to the dictionary
        dictionary[len(dictionary)] = current_string + bytearray([entry[0]])
        current_string = entry

    return bytes(decompressed)
