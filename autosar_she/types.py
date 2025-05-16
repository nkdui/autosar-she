from enum import Enum

from bitarray import bitarray

KEY_UPDATE_ENC_C = bytes.fromhex("01015348 45008000 00000000 000000B0")
KEY_UPDATE_MAC_C = bytes.fromhex("01025348 45008000 00000000 000000B0 ")
DEBUG_KEY_C = bytes.fromhex("01035348 45008000 00000000 000000B0 ")
PRNG_KEY_C = bytes.fromhex("01045348 45008000 00000000 000000B0 ")
PRNG_SEED_KEY_C = bytes.fromhex("01055348 45008000 00000000 000000B0 ")
PRNG_EXTENSION_C = bytes.fromhex("80000000 00000000 00000000 00000100")


class ProtectionFlag(Enum):
    NONE = bitarray("000000")
    CMAC_USAGE = bitarray("000001")
    WILDCARD = bitarray("000010")
    KEY_USAGE = bitarray("000100")
    DEBUGGER_PROTECTION = bitarray("001000")
    BOOT_PROTECTION = bitarray("010000")
    WRITE_PROTECTION = bitarray("100000")

    def __or__(self, value: "ProtectionFlag") -> "ProtectionFlag":
        return ProtectionFlag(self.value | value.value)


class MemorySlot(Enum):
    SECRET_KEY = bitarray("0000")
    MASTER_ECU_KEY = bitarray("0001")
    BOOT_MAC_KEY = bitarray("0010")
    BOOT_MAC = bitarray("0011")
    KEY_1 = bitarray("0100")
    KEY_2 = bitarray("0101")
    KEY_3 = bitarray("0110")
    KEY_4 = bitarray("0111")
    KEY_5 = bitarray("1000")
    KEY_6 = bitarray("1001")
    KEY_7 = bitarray("1010")
    KEY_8 = bitarray("1011")
    KEY_9 = bitarray("1100")
    KEY_10 = bitarray("1101")
    RAM_KEY = bitarray("1110")
