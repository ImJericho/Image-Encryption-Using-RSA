from math import gcd
import json


# take two primes whatever we like 
p = 101
q = 103

# get prime numbers from https://





# calculating n
n = p * q

# calculating totient, t
t = (p - 1) * (q - 1)

# selecting public key, e
for i in range(2, t):
    if gcd(i, t) == 1:
        e = i
        break

# selecting private key, d
j = 0
while True:
    if (j * e) % t == 1:
        d = j
        break
    j += 1


private_key = {}
private_key['d'] = e
private_key['n'] = n


public_key = {}
public_key['e'] = d
public_key['n'] = n

with open('./Keys/private_key.json', 'w') as f:
    json.dump(private_key, f)

with open('./Keys/public_key.json', 'w') as f:
    json.dump(public_key, f)
