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
#import tensorflow as tf
import librosa

#tf.logging.set_verbosity(tf.logging.ERROR)
#%%

#PATH = os.getcwd()
# Define data path
audio_data_list=[]
num_channel=1

data_path ='/home/joelkiran/Desktop/DATASET/splitAudio/file1.wav'
X, sample_rate = librosa.load(data_path,res_type='kaiser_fast',mono=False)
print("x : ",X.shape,sample_rate)
print(np.sum(X[0]))
print(np.sum(X[1]))

X = librosa.to_mono(X)
print("x : ",X.shape,sample_rate)
print(np.sum(X[1]))
mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=60).T,axis=0) 

audio_data_list.append(mfccs)
audio_data = np.array(audio_data_list)
audio_data = audio_data.astype('float32')
audio_data /= 255
print (audio_data.shape)

if num_channel==1:
	if K.image_dim_ordering()=='th':
		audio_data= np.expand_dims(audio_data, axis=1) 
		print (audio_data.shape)
	else:
		audio_data= np.expand_dims(audio_data, axis=4) 
		print (audio_data.shape)

model=load_model('25feb.h5')
model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=["accuracy"])

test_image = audio_data
print (test_image.shape)


(model.predict(test_image))
print()
print()
print("The Output ")
print("******************************************************")
print(model.predict_classes(test_image))
print()
print("******************************************************")
	
