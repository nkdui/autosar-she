import random

from autosar_she.algo import _aes_mp, _padding, kdf


def test_padding_0_bytes():
    data = random.randbytes(0)
    assert _padding(data) == data + bytes.fromhex("80000000000000000000000000000000")


def test_padding_1_bytes():
    data = random.randbytes(1)
    assert _padding(data) == data + bytes.fromhex("800000000000000000000000000008")


def test_padding_2_bytes():
    data = random.randbytes(2)
    assert _padding(data) == data + bytes.fromhex("8000000000000000000000000010")


def test_padding_15_bytes():
    data = random.randbytes(15)
    assert _padding(data) == data + bytes.fromhex("8000000000000000000000000000000078")


def test_padding_16_bytes():
    data = random.randbytes(16)
    assert _padding(data) == data + bytes.fromhex("80000000000000000000000000000080")


def test_padding_17_bytes():
    data = random.randbytes(17)
    assert _padding(data) == data + bytes.fromhex("800000000000000000000000000088")


def test_padding_31_bytes():
    data = random.randbytes(31)
    assert _padding(data) == data + bytes.fromhex("80000000000000000000000000000000F8")


def test_padding_32_bytes():
    data = random.randbytes(32)
    assert _padding(data) == data + bytes.fromhex("80000000000000000000000000000100")


def test_padding_33_bytes():
    data = random.randbytes(33)
    assert _padding(data) == data + bytes.fromhex("800000000000000000000000000108")


def test_aes_mp():
    M = bytes.fromhex(
        "6bc1bee22e409f96e93d7e117393172aae2d8a571e03ac9c9eb76fac45af8e51"
    )
    M_PADDED = _padding(M)
    output = _aes_mp(M_PADDED)
    assert M_PADDED[len(M) :] == bytes.fromhex("80000000000000000000000000000100")
    assert output == bytes.fromhex("c7277a0dc1fb853b5f4d9cbd26be40c6")


def test_kdf():
    K = bytes.fromhex("000102030405060708090a0b0c0d0e0f")
    C = b"\x01\x01SHE\x00"
    assert kdf(K, C) == bytes.fromhex("118a46447a770d87828a69c222e2d17e")
