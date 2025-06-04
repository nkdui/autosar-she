from autosar_she import MemorySlot, ProtectionFlag, memory_update


def test_update_mem():
    m1, m2, m3, m4, m5 = memory_update(
        bytes.fromhex("000000000000000000000000000001"),
        MemorySlot.MASTER_ECU_KEY,
        bytes.fromhex("000102030405060708090a0b0c0d0e0f"),
        MemorySlot.KEY_1,
        bytes.fromhex("0f0e0d0c0b0a09080706050403020100"),
        1,
        ProtectionFlag.NONE,
    )
    assert m1 == bytes.fromhex("00000000000000000000000000000141")
    assert m2 == bytes.fromhex(
        "2b111e2d93f486566bcbba1d7f7a9797 c94643b050fc5d4d7de14cff682203c3"
    )
    assert m3 == bytes.fromhex("b9d745e5ace7d41860bc63c2b9f5bb46")
    assert m4 == bytes.fromhex(
        "00000000000000000000000000000141 b472e8d8727d70d57295e74849a27917"
    )
    assert m5 == bytes.fromhex("820d8d95dc11b4668878160cb2a4e23e")


def test_update_mem_1():
    m1, m2, m3, m4, m5 = memory_update(
        bytes(15),
        MemorySlot.MASTER_ECU_KEY,
        bytes(16),
        MemorySlot.MASTER_ECU_KEY,
        bytes(16),
        1,
        ProtectionFlag.NONE,
    )
    assert m1 == bytes.fromhex("00000000000000000000000000000011")
    assert m2 == bytes.fromhex(
        "ff8b75f73e6ad5a1729423c6e9311f1a69ccff393e17baeda2952454af1b2311"
    )
    assert m3 == bytes.fromhex("68d4ae16c35e8b073d030913edde9a3f")
    assert m4 == bytes.fromhex(
        "00000000000000000000000000000011ee52f069492a9d3d1283557ea645746c"
    )
    assert m5 == bytes.fromhex("109c84887e96f51107265a9876de04ca")


def test_update_mem_2():
    m1, m2, m3, m4, m5 = memory_update(
        bytes.fromhex("0102030405060708090a0b0c0d0e0f"),
        MemorySlot.MASTER_ECU_KEY,
        bytes(16),
        MemorySlot.MASTER_ECU_KEY,
        bytes(16),
        1,
        ProtectionFlag.NONE,
    )
    assert m1 == bytes.fromhex("0102030405060708090a0b0c0d0e0f11")
    assert m2 == bytes.fromhex(
        "ff8b75f73e6ad5a1729423c6e9311f1a69ccff393e17baeda2952454af1b2311"
    )
    assert m3 == bytes.fromhex("8c9a5b545e74ccc28b5f99ea97e9d14c")
    assert m4 == bytes.fromhex(
        "0102030405060708090a0b0c0d0e0f11ee52f069492a9d3d1283557ea645746c"
    )
    assert m5 == bytes.fromhex("d009cac32911a04f9d24f2e7fbce9752")


def test_update_mem_3():
    m1, m2, m3, m4, m5 = memory_update(
        bytes.fromhex("0102030405060708090a0b0c0d0e0f"),
        MemorySlot.BOOT_MAC_KEY,
        bytes(16),
        MemorySlot.MASTER_ECU_KEY,
        bytes(16),
        1,
        ProtectionFlag.NONE,
    )
    assert m1 == bytes.fromhex("0102030405060708090a0b0c0d0e0f12")
    assert m2 == bytes.fromhex(
        "ff8b75f73e6ad5a1729423c6e9311f1a69ccff393e17baeda2952454af1b2311"
    )
    assert m3 == bytes.fromhex("345a196cf7dd91b99773d5f183661c7b")
    assert m4 == bytes.fromhex(
        "0102030405060708090a0b0c0d0e0f12ee52f069492a9d3d1283557ea645746c"
    )
    assert m5 == bytes.fromhex("8af3e86ad88fce145374c0d5a4e9a0ce")


def test_update_mem_4():
    m1, m2, m3, m4, m5 = memory_update(
        bytes.fromhex("0102030405060708090a0b0c0d0e0f"),
        MemorySlot.BOOT_MAC_KEY,
        bytes.fromhex("345a196cf7dd91b99773d5f183661c7b"),
        MemorySlot.MASTER_ECU_KEY,
        bytes(16),
        1,
        ProtectionFlag.NONE,
    )
    assert m1 == bytes.fromhex("0102030405060708090a0b0c0d0e0f12")
    assert m2 == bytes.fromhex(
        "61aaeed46052c59be923e9ef26b83e7b834d487a4e887782b730f2c085725475"
    )
    assert m3 == bytes.fromhex("6e61d16953e83a055f3783c187b3b8fb")
    assert m4 == bytes.fromhex(
        "0102030405060708090a0b0c0d0e0f12ee52f069492a9d3d1283557ea645746c"
    )
    assert m5 == bytes.fromhex("8af3e86ad88fce145374c0d5a4e9a0ce")


def test_update_mem_5():
    m1, m2, m3, m4, m5 = memory_update(
        bytes.fromhex("0102030405060708090a0b0c0d0e0f"),
        MemorySlot.BOOT_MAC_KEY,
        bytes.fromhex("345a196cf7dd91b99773d5f183661c7b"),
        MemorySlot.BOOT_MAC,
        bytes(16),
        1,
        ProtectionFlag.NONE,
    )
    assert m1 == bytes.fromhex("0102030405060708090a0b0c0d0e0f32")
    assert m2 == bytes.fromhex(
        "61aaeed46052c59be923e9ef26b83e7b834d487a4e887782b730f2c085725475"
    )
    assert m3 == bytes.fromhex("28c77534040eb793a8d86cdd82f1692c")
    assert m4 == bytes.fromhex(
        "0102030405060708090a0b0c0d0e0f32ee52f069492a9d3d1283557ea645746c"
    )
    assert m5 == bytes.fromhex("f97df5759090aacab28eed52c5cb71df")


def test_update_mem_6():
    m1, m2, m3, m4, m5 = memory_update(
        bytes.fromhex("0102030405060708090a0b0c0d0e0f"),
        MemorySlot.BOOT_MAC_KEY,
        bytes.fromhex("345a196cf7dd91b99773d5f183661c7b"),
        MemorySlot.BOOT_MAC,
        bytes.fromhex("28c77534040eb793a8d86cdd82f1692c"),
        1,
        ProtectionFlag.NONE,
    )
    assert m1 == bytes.fromhex("0102030405060708090a0b0c0d0e0f32")
    assert m2 == bytes.fromhex(
        "61aaeed46052c59be923e9ef26b83e7bd3bc6d8a4ba5afad4d29b6ce96f0e0fa"
    )
    assert m3 == bytes.fromhex("e7e1344b3a1ab27089bd6e3e960293dc")
    assert m4 == bytes.fromhex(
        "0102030405060708090a0b0c0d0e0f32a700f476957a02ebb3f8bca0a301912f"
    )
    assert m5 == bytes.fromhex("00ad07dd1e7a587a7d6a40d5aa365a50")


def test_update_mem_7():
    m1, m2, m3, m4, m5 = memory_update(
        bytes.fromhex("0102030405060708090a0b0c0d0e0f"),
        MemorySlot.BOOT_MAC_KEY,
        bytes.fromhex("345a196cf7dd91b99773d5f183661c7b"),
        MemorySlot.BOOT_MAC,
        bytes.fromhex("28c77534040eb793a8d86cdd82f1692c"),
        2,
        ProtectionFlag.NONE,
    )
    assert m1 == bytes.fromhex("0102030405060708090a0b0c0d0e0f32")
    assert m2 == bytes.fromhex(
        "e7261c1ec36d2e5c031c5518026b85c2fe0cba7961ed6fcbb93d764e7be0a2ce"
    )
    assert m3 == bytes.fromhex("c2d4217bb2a2fe7e21985aff26c8cf4c")
    assert m4 == bytes.fromhex(
        "0102030405060708090a0b0c0d0e0f32f622cd17b3f83d8f98140ba37f9e88a2"
    )
    assert m5 == bytes.fromhex("7ad0089b48e374bbf2333897f16707b7")


def test_update_mem_8():
    m1, m2, m3, m4, m5 = memory_update(
        bytes.fromhex("0102030405060708090a0b0c0d0e0f"),
        MemorySlot.BOOT_MAC_KEY,
        bytes.fromhex("345a196cf7dd91b99773d5f183661c7b"),
        MemorySlot.BOOT_MAC,
        bytes.fromhex("28c77534040eb793a8d86cdd82f1692c"),
        2,
        ProtectionFlag.NONE | ProtectionFlag.WILDCARD,
    )
    assert m1 == bytes.fromhex("0102030405060708090a0b0c0d0e0f32")
    assert m2 == bytes.fromhex(
        "09e4e392457f01472835889d4b8545507c32e0f0e67448add9ee5f4e9763edf5"
    )
    assert m3 == bytes.fromhex("6270895dbebc1878881036c8e7951f35")
    assert m4 == bytes.fromhex(
        "0102030405060708090a0b0c0d0e0f32f622cd17b3f83d8f98140ba37f9e88a2"
    )
    assert m5 == bytes.fromhex("7ad0089b48e374bbf2333897f16707b7")


def test_update_mem_9():
    m1, m2, m3, m4, m5 = memory_update(
        bytes.fromhex("0102030405060708090a0b0c0d0e0f"),
        MemorySlot.BOOT_MAC_KEY,
        bytes.fromhex("345a196cf7dd91b99773d5f183661c7b"),
        MemorySlot.BOOT_MAC,
        bytes.fromhex("28c77534040eb793a8d86cdd82f1692c"),
        2,
        ProtectionFlag.NONE
        | ProtectionFlag.WILDCARD
        | ProtectionFlag.KEY_USAGE
        | ProtectionFlag.CMAC_USAGE,
    )
    assert m1 == bytes.fromhex("0102030405060708090a0b0c0d0e0f32")
    assert m2 == bytes.fromhex(
        "1f2c8ec20fa481e601f4c19d4fb5a7c8b44b73bb8665ebc0df64742dd91a62cc"
    )
    assert m3 == bytes.fromhex("88dbd84c4b61a92a22b3cf1dfcc1fb12")
    assert m4 == bytes.fromhex(
        "0102030405060708090a0b0c0d0e0f32f622cd17b3f83d8f98140ba37f9e88a2"
    )
    assert m5 == bytes.fromhex("7ad0089b48e374bbf2333897f16707b7")


def test_update_mem_10():
    m1, m2, m3, m4, m5 = memory_update(
        bytes.fromhex("0102030405060708090a0b0c0d0e0f"),
        MemorySlot.MASTER_ECU_KEY,
        bytes.fromhex("345a196cf7dd91b99773d5f183661c7b"),
        MemorySlot.KEY_1,
        bytes.fromhex("28c77534040eb793a8d86cdd82f1692c"),
        3,
        ProtectionFlag.NONE
        | ProtectionFlag.WILDCARD
        | ProtectionFlag.KEY_USAGE
        | ProtectionFlag.CMAC_USAGE,
    )
    assert m1 == bytes.fromhex("0102030405060708090a0b0c0d0e0f41")
    assert m2 == bytes.fromhex(
        "5a92bbe0d03b6bb92a0da6495c7110577e8d09bbde75a392061ac64de2fdc8ce"
    )
    assert m3 == bytes.fromhex("2cefccddd6a865c3bda11b2e4cc1c2f2")
    assert m4 == bytes.fromhex(
        "0102030405060708090a0b0c0d0e0f415469b228dea53dc2d252cd4bcf74ccd9"
    )
    assert m5 == bytes.fromhex("ed84a4b17af21083f63894fe145f1b64")
