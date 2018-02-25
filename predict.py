import os,cv2
import numpy as np

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split
from keras import backend as K
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD,RMSprop,adam
from keras.models import load_model
import keras
num_channel=1

num_classes = 10

img_data_list=[]
print("loading the image");

input_img=cv2.imread("/home/joelkiran/Desktop/DATASET/spectrogram.png")
input_img=cv2.cvtColor(input_img, cv2.COLOR_BGR2GRAY)
input_img=cv2.resize(input_img,(128,128))
img_data_list.append(input_img)

img_data = np.array(img_data_list)
img_data = img_data.astype('float32')
img_data /= 255

if num_channel==1:
	if K.image_dim_ordering()=='th':
		img_data= np.expand_dims(img_data, axis=1) 
		print (img_data.shape)
	else:
		img_data= np.expand_dims(img_data, axis=4) 
		print (img_data.shape)


model=load_model('own_data_large_3feb.h5')
model.compile(loss='categorical_crossentropy', optimizer='rmsprop',metrics=["accuracy"])


test_image = img_data;
print (test_image.shape)


print(model.predict(test_image))
print(model.predict_classes(test_image))


