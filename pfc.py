from hmac import HMAC as h
from secrets import token_hex as t
n=input('Nonce: ')
nw=int(input('Number you want: '))
ss=input('Server seed: ')
s1=':'.join((n,ss,n)).encode()
while 1:
 cs=t(4)
 s2=':'.join((n,cs,n)).encode()
 if round(int.from_bytes(h(s2,s1,'sha512').digest()[:4])/429496.7295)==nw: print(cs);break
