c = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')

idx = 0
prefix = 'crypto{1' # 노가다

x = []
for i in range(len(prefix)):
    x.append(c[i] ^ ord(prefix[i]))

res = []
for i in range(len(c)):
    res.append(chr(c[i] ^ x[i % len(x)]))

print(''.join(res))
# crypto{1f_y0u_Kn0w_En0uGH_y0u_Kn0w_1t_4ll}