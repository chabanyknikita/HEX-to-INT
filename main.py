hex_s = input("Write your value: ")
byte = int(input("Write byte of your value = "))
a = int(hex_s, 16)
msgHB = "HEX to BigEndian:"
msgBH = "BigEndian to HEX:"
msgHL = "HEX to LittleEndian:"
msgLH = "LittleEndian to HEX:"


def hex_to_BigEndian(hex_s):
    print(f"\n{msgHB} \n{hex_s} -> {a}")


def BigEndian_to_hex(number):
    print(f"{msgBH} \n{number} -> {hex(number)}")


def BigEndian_to_LittleEndian(value: int) -> int:
    return int.from_bytes(value.to_bytes(byte, byteorder="little"), byteorder="big")


hex_to_BigEndian(hex_s)
BigEndian_to_hex(a)
print(f"{msgHL}\n{hex_s} -> {BigEndian_to_LittleEndian(a)}")
print(f"{msgLH}\n{BigEndian_to_LittleEndian(a)} -> {hex_s}")
