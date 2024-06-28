from Crypto.Util.number import *

# d*e /equiv 1 mod phi_N
# d = inv(e, phi_N)

p = 857504083339712752489993810777
q = 1029224947942998075080348647219
e = 65537
d = inverse(e, (p-1)*(q-1))

print('N', p*q)
print('res', (d*e)%((p-1)*(q-1)))
print('d', d)

# 121832886702415731577073962957377780195510499965398469843281