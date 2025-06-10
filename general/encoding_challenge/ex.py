from pwn import *
import json

p = remote('socket.cryptohack.org', 13377)

def json_recv():
    line = p.readline() # bytes data로 받는데
    return json.loads(line.decode()) # 이걸 문자열로 바꿔줘야 json에서 load가 가능

def json_send(res):
    response = {"decoded": res}
    p.sendline(json.dumps(response).encode()) # 보낼때는 다시 byte data로

import base64
import codecs
from Crypto.Util.number import long_to_bytes 

while 1:
    recv = json_recv()
    if 'flag' in recv:
        print(recv['flag'])
        break
    
    type = recv['type']
    encoded = recv['encoded']
    if  type == "base64":
        decoded = base64.b64decode(encoded).decode()
    elif type == "hex":
        decoded = bytes.fromhex(encoded).decode()
    elif type == "rot13":
        decoded = codecs.decode(encoded, 'rot13')
    elif type == "bigint":
        hex = encoded.lstrip('0x')
        decoded = long_to_bytes(int(hex, 16)).decode()
    elif type == "utf-8":
        decoded = ''.join(chr(c) for c in encoded)

    json_send(decoded)

p.close()

'''
encode(): 문자열을  bytes data로
decode(): bytes data를 문자열로
'''