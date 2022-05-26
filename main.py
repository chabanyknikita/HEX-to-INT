hex_s = 'ff00000000000000000000000000000000000000000000000000000000000000'

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tHEX -> BigEndian")
a = int(hex_s, 16)
print(f"{hex_s} ->", a)

endian = a

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tBigEndian -> HEX ")
print(f"{endian} -> ", hex(endian))

# sorry, i dont know how to do it and i did it in this way :)
byte = int(input("Write byte of your value = "))
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tHEX->LittleEndian")


def be_to_le(value: int) -> int:
    return int.from_bytes(value.to_bytes(byte, byteorder="little"), byteorder="big")


print(f"{hex_s} -> ", be_to_le(endian))

print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tLittleEndian->HEX")
print(f"{be_to_le(endian)} -> ", hex_s)
