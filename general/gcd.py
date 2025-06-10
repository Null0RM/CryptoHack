a_ = 66528
b_ = 52920

def gcd(a, b):
    if (b == 0): 
        return a
    if (a < b):
        tmp = a
        b = a
        a = tmp
    r = a % b
    return gcd(b, r)
    
print(gcd(a_, b_))

'''
ax + by = 0
'''