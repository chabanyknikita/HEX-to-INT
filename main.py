import binascii

a = input("Write value ")
size = int(len(str(a)) / 2)
print(a)


def pad(mystr):
    padding_size = 2 * size
    mystr = mystr + "0" * (padding_size - len(mystr))
    return mystr


aa = pad(a[:2 * size])

a1 = int.from_bytes(binascii.unhexlify(aa), byteorder='little')
a2 = int.from_bytes(binascii.unhexlify(aa), byteorder='big')
print(f"Value: 0x{a}\nNumber of bytes: {size}\nLittle-endian: {a1}\nBig-endian: {a2}")

b = '0x{0:08X}'.format(a2)
l = '0x%X' % a1
print(f"BigEndian to HEX: {b}\nLittleEndian to HEX: {l}")
