from autosar_she import MemorySlot, ProtectionFlag, memory_update

if __name__ == "__main__":
    m12345 = memory_update(
        bytes(15),
        MemorySlot.MASTER_ECU_KEY,
        bytes(16),
        MemorySlot.KEY_1,
        bytes(16),
        2,
        ProtectionFlag.NONE | ProtectionFlag.CMAC_USAGE,
    )

    for mi in m12345:
        print(mi.hex(' ', 4))
