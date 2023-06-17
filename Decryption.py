import cv2 as cv
import numpy as np
import time
from tqdm import tqdm 
import json

import Algorithm
rsa = Algorithm.RSA()


private_key_location = './keys/private_key.json'
private_key = rsa.get_private_key(private_key_location)

# retrieving data from txt file.
txt_name = 'Encrypted_image.npy'
en_image = np.load(txt_name)

shape = en_image.shape
img = en_image


start = time.time()

for i in tqdm(range(0, shape[0])):
	for j in range(0, shape[1]):
		for k in range(0, shape[2]):
			x = en_image[i][j][k]
			new_x = rsa.decrypt(int(x), private_key)
			img[i][j][k] = int(new_x)


img = np.array(img)
final_location = 'Decrypted_image.jpg'
cv.imwrite(final_location, img)

end = time.time()
eTime = end - start
print(f"time taken to decrpt the image :",eTime)