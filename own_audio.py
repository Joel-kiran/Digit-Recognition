import os,cv2
import numpy as np

from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
#from sklearn.cross_validation import train_test_split
from keras import backend as K
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation, Flatten
#from keras.layers.convolutional import Convolution2D, MaxPooling2D
from keras.optimizers import SGD,RMSprop,adam
from keras.models import load_model
import keras
from keras.callbacks import ModelCheckpoint

import librosa

#%%

#PATH = os.getcwd()
# Define data path
data_path ='/home/joelkiran/Desktop/DATASET/Mic_processed_18feb'
data_dir_list = os.listdir(data_path)


num_channel=1
num_epoch=50

# Define the number of classes
num_classes = 29

audio_data_list=[]
size_data=[]
for dataset in data_dir_list:
	audio_list=os.listdir(data_path+'/'+ dataset)
	print ('Loaded the images of dataset-'+'{}\n'.format(dataset))
	#print(audio_list)
	for audio in audio_list:
		X, sample_rate = librosa.load(data_path+'/'+dataset+'/'+audio, res_type='kaiser_fast')
		# we extract mfcc feature from data
		mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=60).T,axis=0) 

		audio_data_list.append(mfccs)
	size_data.append(len(audio_list))

print(data_dir_list)
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

num_classes =29

num_of_samples = audio_data.shape[0]
labels = np.ones((num_of_samples,),dtype='int64')

j=0
n=0
print("/////////////")

class_label={}
for i in range(len(data_dir_list)):
	class_label[data_dir_list[i]]=i;
for i in data_dir_list:
	labels[j:j+size_data[n]]=class_label[i]
	j=j+size_data[n]
	n=n+1
print(size_data)
'''
labels[0:24]=0
labels[24:48]=1
labels[48:72]=2
labels[72:96]=3
labels[96:120]=4
labels[120:144]=5
labels[144:168]=6
labels[168:192]=7
labels[192:216]=8
labels[218:]=9
'''

names = []
for i in data_dir_list:
	names.append(i);
	
Y = np_utils.to_categorical(labels, num_classes)

x,y = shuffle(audio_data,Y, random_state=2)



# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)


#print("EG : ",X_train[0])

#%%
# Defining the model
shape=X_train[0].shape
print(shape)
model = Sequential()

model.add(Dense(64, input_shape=shape))
model.add(Activation('relu'))
model.add(Dropout(0.3))

'''
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dropout(0.5))
'''
model.add(Flatten())
model.add(Dense(num_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

filepath="18feb.h5"
checkpoint = ModelCheckpoint(filepath, monitor='val_acc', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

model.fit(X_train, y_train, batch_size=32, epochs=500, callbacks=callbacks_list,validation_data=(X_test, y_test))


model=load_model(filepath)
model.compile(loss='categorical_crossentropy', optimizer='rmsprop',metrics=["accuracy"])

#print('X_test',X_test)
#score = model.evaluate(X_test, y_test, verbose=0)
#print('Test Loss:', score[0])
#print('Test accuracy:', score[1])

test_image = X_test
print (test_image.shape)


(model.predict(test_image))
for k in (model.predict_classes(test_image)):
	for i in class_label:
		if class_label[i]==k :
			print(i)
	
#print(y_test)

print(class_label)

#actual classes

'''
op=[]
for i in y_test:
	for j in range(len(i)):
		if i[j]==1 :
			op.append(j)
print(op)
'''

