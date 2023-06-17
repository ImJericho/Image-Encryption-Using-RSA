import json


# storing the private key pair, and public key pair in json format inside keys folder





class RSA:
    def get_private_key(self, location):
        ''' this function can not retrive the private key unless someone knows the location of it'''
        # retrive the private key stored in json format in location
        f = open(location)
        private_key = json.load(f)
        # returning in python dictonary format
        return private_key

    def get_public_key(self, location):
        # retrive the public key stored in json format in location
        f = open(location)
        public_key = json.load(f)
        # returning in python dictonary format
        return public_key
    

    def encrypt(self, message, public_key):
        # public key = e,n
        e = public_key['e']
        n = public_key['n']
        
        # performing encryption
        encrypted_message = (message ** e) % n

        # encryption using RSA algorithm
        # for more clear understanding see the RSA_Algorithm.txt
        return encrypted_message
    
    def decrypt(self, en_message, private_key):
        #private key = d,n
        d = private_key['d']
        n = private_key['n']
        
        # performing decryption
        message = (en_message ** d) % n
        # Decryption using RSA algorithm
        return message
    





def print_something():
    print("Hey there this is running from algorithm.py files")

print_something()