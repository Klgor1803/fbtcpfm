# fbtcpfm
Freebitco.in provably fair manipulator

Freebitco.in number generation algorithm:

string1=b'nonce:server_seed:nonce'
string2=b'nonce:client_seed:nonce'
hmac=HMAC_SHA512(message=string1,key=string2).digest()
number=round(int(hmac[:4])/429496.7295)

Example:
Nonce=630
Client_seed='thisismyclientseed'
Server_seed='30d1631c26f495fdf9044df0776ec4b051af2cfecbd7bf02334ffa27173c5123'
string1=b'630:30d1631c26f495fdf9044df0776ec4b051af2cfecbd7bf02334ffa27173c5123:630'
string2=b'630:thisismyclientseed:630'
round(int.from_bytes(hmac(string1,string2,'sha512').digest()[:4])/429496.7295)=4801
verify [here](https://s3.amazonaws.com/roll-verifier/verify.html?server_seed=30d1631c26f495fdf9044df0776ec4b051af2cfecbd7bf02334ffa27173c5123&client_seed=thisismyclientseed&server_seed_hash=902beff3bef3a8ce6bfb1a9c41f9e4d0a36172a27e105a5ee9a08528749d26eb&nonce=630)
