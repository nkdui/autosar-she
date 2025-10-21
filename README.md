# autosar-she
Implementation of AUTOSAR-SHE MemoryUpdate protocol in Python

[![main](https://github.com/nkdui/autosar-she/actions/workflows/main.yml/badge.svg)](https://github.com/nkdui/autosar-she/actions/workflows/main.yml)

# Installation
Install the latest version using `pip` or `uv`.
## pip
```
pip install git+https://github.com/nkdui/autosar-she.git
```
## uv
```
uv add https://github.com/nkdui/autosar-she.git
```

# Example
```python
from autosar_she import MemorySlot, ProtectionFlag, memory_update

m1, m2, m3, m4, m5 = memory_update(uid=bytes.fromhex("0102030405060708090a0b0c0d0e0f"),
                                   auth_id=MemorySlot.MASTER_ECU_KEY,
                                   k_auth_id=bytes.fromhex("345a196cf7dd91b99773d5f183661c7b"),
                                   id_=MemorySlot.KEY_1,
                                   k_id=bytes.fromhex("28c77534040eb793a8d86cdd82f1692c"),
                                   c_id=3,
                                   f_id=ProtectionFlag.NONE | ProtectionFlag.WILDCARD | ProtectionFlag.KEY_USAGE | ProtectionFlag.CMAC_USAGE)
```
For detailed description of the protocol and its parameters, please refer to the [AUTOSAR-SHE](https://www.autosar.org/fileadmin/standards/R21-11/FO/AUTOSAR_TR_SecureHardwareExtensions.pdf) document.
