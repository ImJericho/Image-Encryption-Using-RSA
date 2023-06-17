import cv2 as cv
import numpy as np
import time
from tqdm import tqdm 
import Algorithm
rsa = Algorithm.RSA()



# specify the location where public key's json file is available
public_key_location = './keys/public_key.json'
public_key = rsa.get_public_key(public_key_location)
print("encryption using public key:", public_key)



# read the image
image_name = "Image.jpg"
img = cv.imread(image_name)



start = time.time()


img = img.astype(np.uint16)
shape = img.shape
new_img = img


for i in tqdm(range(0, shape[0])):
	for j in range(0, shape[1]):
		for k in range(0, shape[2]):
			x = img[i][j][k]
			new_x = rsa.encrypt(int(x), public_key)
			new_img[i][j][k] = int(new_x)




# the encrypted file will be stored in npy format
new_img = np.array(new_img)
file_name = "Encrypted_image"+'.npy'
np.save(file_name, new_img)



end = time.time()
eTime = end - start
print(f"time taken to encrypt the image :",eTime)



#THIS NPY file is sharable and could be shared without any fear of anybody seeing with python
# as every pixel of it is 
