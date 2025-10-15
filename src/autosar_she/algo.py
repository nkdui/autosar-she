from bitarray import bitarray
from cryptography.hazmat.primitives.ciphers.algorithms import AES128
from cryptography.hazmat.primitives.ciphers.base import Cipher
from cryptography.hazmat.primitives.ciphers.modes import ECB

BLOCKSIZE = 16


def _aes_mp(data: bytes) -> bytes:
    """Miyaguchi-Preneel compression function"""
    assert (len(data) % BLOCKSIZE) == 0, "'data' length must divisible by 16 bytes"

    block_count = len(data) // BLOCKSIZE

    out_i = bytes(BLOCKSIZE)
    for i in range(block_count):
        block_i = data[i * BLOCKSIZE : (i + 1) * BLOCKSIZE]
        encrypted_block = Cipher(AES128(out_i), ECB()).encryptor().update(block_i)
        out_i = bytes(a ^ b ^ c for a, b, c in zip(encrypted_block, block_i, out_i))
    return out_i


def _padding(data: bytes) -> bytes:
    """AUTOSAR-SHE specific padding"""
    data_ba = bitarray()
    data_ba.frombytes(data)
    bit_length = len(data_ba)
    data_ba += bitarray([1])
    k = 0
    while ((bit_length + 1 + k) % 128) != 88:
        k += 1
    data_ba += bitarray(k)
    number_ba = bitarray()
    number_ba.frombytes(bit_length.to_bytes(5))
    data_ba += number_ba
    return data_ba.tobytes()


def kdf(key: bytes, const: bytes) -> bytes:
    """AUTOSAR-SHE Key Derive Function"""
    return _aes_mp(_padding(key + const))
