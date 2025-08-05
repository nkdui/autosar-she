from autosar_she import MemorySlot, ProtectionFlag, memory_update
from autosar_she.algo import kdf


print("Master key")
m12345 = memory_update(
    bytes.fromhex("000000000000000000000000000000"),
    MemorySlot.MASTER_ECU_KEY,
    bytes.fromhex("00000000000000000000000000000000"),
    MemorySlot.MASTER_ECU_KEY,
    bytes.fromhex("2B7E151628AED2A6ABF7158809CF4F3C"),
    1,
    ProtectionFlag.NONE,
)
print(b"".join(m12345[:3]).hex())
print(b"".join(m12345[3:]).hex())

print("SW update key")
m12345 = memory_update(
    bytes.fromhex("000000000000000000000000000000"),
    MemorySlot.MASTER_ECU_KEY,
    bytes.fromhex("2B7E151628AED2A6ABF7158809CF4F3C"),
    MemorySlot.KEY_1,
    bytes.fromhex("06A9214036B8A15B512E03D534120006"),
    1,
    ProtectionFlag.NONE,
)
print(b"".join(m12345[:3]).hex())
print(b"".join(m12345[3:]).hex())

print("REE MAC key")
m12345 = memory_update(
    bytes.fromhex("000000000000000000000000000000"),
    MemorySlot.MASTER_ECU_KEY,
    bytes.fromhex("2B7E151628AED2A6ABF7158809CF4F3C"),
    MemorySlot.KEY_2,
    bytes.fromhex("06A9214036B8A15B512E03D534120006"),
    1,
    ProtectionFlag.NONE | ProtectionFlag.KEY_USAGE | ProtectionFlag.CMAC_USAGE,
)
print(b"".join(m12345[:3]).hex())
print(b"".join(m12345[3:]).hex())

print("HL MAC key")
m12345 = memory_update(
    bytes.fromhex("000000000000000000000000000000"),
    MemorySlot.MASTER_ECU_KEY,
    bytes.fromhex("2B7E151628AED2A6ABF7158809CF4F3C"),
    MemorySlot.KEY_3,
    bytes.fromhex("06A9214036B8A15B512E03D534120006"),
    1,
    ProtectionFlag.NONE | ProtectionFlag.KEY_USAGE,
)
print(b"".join(m12345[:3]).hex())
print(b"".join(m12345[3:]).hex())
