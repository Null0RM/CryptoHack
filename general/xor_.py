input = 'label'

print(''.join(chr(ord(i) ^ 13) for i in input))
# crypto{aloha}