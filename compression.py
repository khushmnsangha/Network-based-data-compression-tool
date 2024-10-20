import zlib
import bz2
import gzip
from rle_compress import rle_compress, rle_decompress
from lzw_compress import lzw_compress, lzw_decompress
from huffman_compress import huffman_compress, huffman_decompress  # Ensure huffman functions are imported

def compress_data(data: bytes, algorithm: str = 'zlib') -> bytes:
    if algorithm == 'zlib':
        return zlib.compress(data)
    elif algorithm == 'gzip':
        return gzip.compress(data)
    elif algorithm == 'bz2':
        return bz2.compress(data)
    # elif algorithm == 'rle':
    #     return rle_compress(data)
    # elif algorithm == 'huffman':
    #     return huffman_compress(data)  # Ensure this returns the correct compressed byte data
    # elif algorithm == 'lzw':
    #     return lzw_compress(data)
    else:
        raise ValueError("Unsupported compression algorithm")

def decompress_data(data: bytes, algorithm: str = 'zlib', codes=None) -> bytes:
    if algorithm == 'zlib':
        return zlib.decompress(data)
    elif algorithm == 'gzip':
        return gzip.decompress(data)
    elif algorithm == 'bz2':
        return bz2.decompress(data)
    # elif algorithm == 'rle':
    #     return rle_decompress(data)
    # elif algorithm == 'huffman':
    #     return huffman_decompress(data, codes)  # Make sure this function correctly uses the codes
    # elif algorithm == 'lzw':
    #     return lzw_decompress(data)
    else:
        raise ValueError("Unsupported decompression algorithm")
