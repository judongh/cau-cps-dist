#  0x4d 0x76 0x50 0x50 0x76 0x2d 0x21 0x62 0x59 0x2d 0x15 0x12 0x04 0x3e 0x81 0x3e 0x6e 0x6e

temp = [0x4d, 0x76, 0x50, 0x50, 0x76, 0x2d, 0x21, 0x62, 0x59, 0x2d, 0x15, 0x12, 0x04, 0x3e, 0x81, 0x3e, 0x6e, 0x6e]

temp_de = [int(x) for x in temp]

print(temp_de)

temp_str = "".join([chr(x) for x in temp_de])
print(temp_str)