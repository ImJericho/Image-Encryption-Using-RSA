from math import gcd



# first prime
p = 100003
q = 32413

message = 34534             # although in my project it will only go up till 255 


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

print(e, n)
print(d, n)

# performing encryption
ct = (message ** e) % n
print(f"Encrypted message is {ct}")

# performing decryption
mes = (ct ** d) % n
print(f"Decrypted message is {mes}")
