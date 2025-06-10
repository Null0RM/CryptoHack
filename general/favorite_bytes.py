c = bytes.fromhex('73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d')
x = c[0] ^ ord('c')
print(''.join(chr(i ^ x) for i in c))
# crypto{0x10_15_my_f4v0ur173_by7e}