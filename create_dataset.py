# Import the os module, for the os.walk function
import os
import shutil

# Set the directory you want to start from
i=0
d={}
path="/home/joelkiran/Desktop/DATASET/recordings";
for dirpath, subdirList, fileList in os.walk(path):
	for fl in fileList:
		if '0_' in fl[:2] : 
			newpath = r'/home/joelkiran/Desktop/DATASET/numbers/0' 
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			shutil.copy(path+"/"+fl,"/home/joelkiran/Desktop/DATASET/numbers/0/"+fl)
		elif '1_' in fl[:2] : 

			newpath = r'/home/joelkiran/Desktop/DATASET/numbers/1' 
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			shutil.copy(path+"/"+fl,"/home/joelkiran/Desktop/DATASET/numbers/1/"+fl)
		elif '2_' in fl[:2] : 
			newpath = r'/home/joelkiran/Desktop/DATASET/numbers/2' 
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			shutil.copy(path+"/"+fl,"/home/joelkiran/Desktop/DATASET/numbers/2/"+fl)
		elif '3_' in fl[:2] : 
			newpath = r'/home/joelkiran/Desktop/DATASET/numbers/3' 
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			shutil.copy(path+"/"+fl,"/home/joelkiran/Desktop/DATASET/numbers/3/"+fl)
		elif '4_' in fl[:2] : 
			newpath = r'/home/joelkiran/Desktop/DATASET/numbers/4' 
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			shutil.copy(path+"/"+fl,"/home/joelkiran/Desktop/DATASET/numbers/4/"+fl)
	
		elif '5_' in fl[:2] : 
			newpath = r'/home/joelkiran/Desktop/DATASET/numbers/5' 
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			shutil.copy(path+"/"+fl,"/home/joelkiran/Desktop/DATASET/numbers/5/"+fl)
	
		elif '6_' in fl[:2] : 
			newpath = r'/home/joelkiran/Desktop/DATASET/numbers/6' 
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			shutil.copy(path+"/"+fl,"/home/joelkiran/Desktop/DATASET/numbers/6/"+fl)
	
		elif '7_' in fl[:2] : 
			newpath = r'/home/joelkiran/Desktop/DATASET/numbers/7' 
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			shutil.copy(path+"/"+fl,"/home/joelkiran/Desktop/DATASET/numbers/7/"+fl)
		
		elif '8_' in fl[:2] : 
			newpath = r'/home/joelkiran/Desktop/DATASET/numbers/8' 
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			shutil.copy(path+"/"+fl,"/home/joelkiran/Desktop/DATASET/numbers/8/"+fl)
	
		if '9_' in fl[:2] : 
			newpath = r'/home/joelkiran/Desktop/DATASET/numbers/9' 
			if not os.path.exists(newpath):
				os.makedirs(newpath)
			shutil.copy(path+"/"+fl,"/home/joelkiran/Desktop/DATASET/numbers/9/"+fl)
	
	
	
	
	
	
	
        
