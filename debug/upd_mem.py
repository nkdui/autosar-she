from autosar_she import MemorySlot, ProtectionFlag, memory_update
from autosar_she.algo import kdf

m12345 = memory_update(
    bytes.fromhex("000000000000000000000000000001"),
    MemorySlot.MASTER_ECU_KEY,
    bytes.fromhex("000102030405060708090a0b0c0d0e0f"),
    MemorySlot.KEY_1,
    bytes.fromhex("0f0e0d0c0b0a09080706050403020100"),
    1,
    ProtectionFlag.NONE,
)

for mi in m12345:
    print(mi.hex())
