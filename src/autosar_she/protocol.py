"""MemoryUpdate protocol"""

from bitarray import bitarray
from cryptography.hazmat.primitives.ciphers import Cipher
from cryptography.hazmat.primitives.ciphers.algorithms import AES128
from cryptography.hazmat.primitives.ciphers.modes import CBC, ECB
from cryptography.hazmat.primitives.cmac import CMAC

from autosar_she.algo import kdf
from autosar_she.types import MemorySlot, ProtectionFlag


def _m1(uid: bytes, id_: MemorySlot, auth_id: MemorySlot) -> bytes:
    assert len(uid) == 15, "'uid' length must be 15 bytes (120 bits)"
    uid_ba = bitarray()
    uid_ba.frombytes(uid)
    return (uid_ba + id_.value + auth_id.value).tobytes()


def _m2(k_auth_id: bytes, k_id: bytes, c_id: int, f_id: ProtectionFlag) -> bytes:
    assert len(k_auth_id) == 16, "'k_auth_id' length must be 16 bytes (128 bits)"
    assert len(k_id) == 16, "'k_id' length must be 16 bytes (128 bits)"
    c_id_ba = bitarray()
    c_id_ba.frombytes(c_id.to_bytes(4))
    c_id_ba = c_id_ba[4:]
    f_id_ba = bitarray()
    f_id_ba.frombytes(f_id.value.to_bytes(1))
    f_id_ba = f_id_ba[2:]
    key_id_ba = bitarray()
    key_id_ba.frombytes(k_id)
    m2_plain = (c_id_ba + f_id_ba + bitarray(94) + key_id_ba).tobytes()
    k1 = kdf(k_auth_id, b"\x01\x01SHE\x00")
    return Cipher(AES128(k1), CBC(bytes(16))).encryptor().update(m2_plain)


def _m3(k_auth_id: bytes, m1: bytes, m2: bytes) -> bytes:
    assert len(k_auth_id) == 16, "'k_auth_id' length must be 16 bytes (128 bits)"
    assert len(m1) == 16, "'m1' length must be 16 bytes (128 bits)"
    assert len(m2) == 32, "'m2' length must be 32 bytes (256 bits)"
    k2 = kdf(k_auth_id, b"\x01\x02SHE\x00")
    cmac = CMAC(AES128(k2))
    cmac.update(m1 + m2)
    return cmac.finalize()


def _m4(uid: bytes, auth_id: MemorySlot, id_: MemorySlot, k_id: bytes, c_id: int):
    assert len(uid) == 15, "'uid' length must be 15 bytes (120 bits)"
    assert len(k_id) == 16, "'k_id' length must be 16 bytes (128 bits)"
    uid_ba = bitarray()
    uid_ba.frombytes(uid)
    c_id_ba = bitarray()
    c_id_ba.frombytes(c_id.to_bytes(4))
    c_id_ba = c_id_ba[4:]
    k3 = kdf(k_id, b"\x01\x01SHE\x00")
    return (uid_ba + id_.value + auth_id.value).tobytes() + Cipher(
        AES128(k3), ECB()
    ).encryptor().update((c_id_ba + bitarray("1" + "0" * 99)).tobytes())


def _m5(k_id: bytes, m4: bytes):
    assert len(k_id) == 16, "'k_id' length must be 16 bytes (128 bits)"
    assert len(m4) == 32, "'m4' length must be 32 bytes (256 bits)"
    k4 = kdf(k_id, b"\x01\x02SHE\x00")
    cmac = CMAC(AES128(k4))
    cmac.update(m4)
    return cmac.finalize()


def memory_update(
    uid: bytes,
    auth_id: MemorySlot,
    k_auth_id: bytes,
    id_: MemorySlot,
    k_id: bytes,
    c_id: int,
    f_id: ProtectionFlag,
):
    """MemoryUpdate protocol"""
    assert len(uid) == 15, "'uid' length must be 15 bytes (120 bits)"
    assert len(k_auth_id) == 16, "'k_auth_id' length must be 16 bytes (128 bits)"
    assert len(k_id) == 16, "'k_id' length must be 16 bytes (128 bits)"
    m1 = _m1(uid, id_, auth_id)
    m2 = _m2(k_auth_id, k_id, c_id, f_id)
    m3 = _m3(k_auth_id, m1, m2)
    m4 = _m4(uid, auth_id, id_, k_id, c_id)
    m5 = _m5(k_id, m4)
    return (m1, m2, m3, m4, m5)
