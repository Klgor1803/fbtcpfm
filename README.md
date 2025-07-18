# fbtcpfm
Freebitco.in provably fair manipulator

This code needs the server seed to work, freebitco.in only shows it's hash precisely to prevent manipulations, however, if you manage to get it, you can manipulate it to generate the number you want

Freebitco.in number generation algorithm:

`string1=b'nonce:server_seed:nonce'`

`string2=b'nonce:client_seed:nonce'`

`hmac=HMAC_SHA512(message=string1,key=string2).digest()`

`number=round(int(hmac[:4])/429496.7295)`

Example:

Nonce=630

Client_seed='thisismyclientseed'

Server_seed='30d1631c26f495fdf9044df0776ec4b051af2cfecbd7bf02334ffa27173c5123'

string1=b'630:30d1631c26f495fdf9044df0776ec4b051af2cfecbd7bf02334ffa27173c5123:630'

string2=b'630:thisismyclientseed:630'

`round(int.from_bytes(hmac(string1,string2,'sha512').digest()[:4])/429496.7295)=4801`

verify [here](https://s3.amazonaws.com/roll-verifier/verify.html?server_seed=30d1631c26f495fdf9044df0776ec4b051af2cfecbd7bf02334ffa27173c5123&client_seed=thisismyclientseed&server_seed_hash=902beff3bef3a8ce6bfb1a9c41f9e4d0a36172a27e105a5ee9a08528749d26eb&nonce=630)

Now, let's say you want the number 10000
Server_seed='00e0cc052d9721b4a7adcda47b2c5469f8b6c685860df214bc4506f76ca9ca8d'
Nonce=630

```~ $ python pfc.py
Nonce: 630
Number you want: 10000
Server seed: 00e0cc052d9721b4a7adcda47b2c5469f8b6c685860df214bc4506f76ca9ca8d
5840a37d```

5840a37d is (one of) the client seed you would use to get the number 10000 with that server seed and nonce

