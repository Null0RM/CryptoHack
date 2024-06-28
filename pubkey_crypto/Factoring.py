'''
installing primefac
$ pip3 install --upgrade pip
$ pip3 install git+https://github.com/elliptic-shiho/primefac-fork@master
'''
import primefac

N = 510143758735509025530880200653196460532653147
factors = list(primefac.primefac(N)) 
print(min(factors))

# 19704762736204164635843