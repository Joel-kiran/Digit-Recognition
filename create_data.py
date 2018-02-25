import os
import shutil
x='_120.'

for (dirpath, subdir, filenames) in os.walk("/home/joelkiran/Desktop/DATASET/Numbers_dataset/"):
	if '0' in dirpath[len(dirpath)-1:]:
	
		for fl in filenames:
			if x in fl:
				newpath="/home/joelkiran/Desktop/DATASET/digit_120/0/"
				if not os.path.exists(newpath):
					os.makedirs(newpath)
				shutil.copy("/home/joelkiran/Desktop/DATASET/Numbers_dataset/0/"+fl,newpath+fl)
	
	
	elif '1' in dirpath[len(dirpath)-1:]:
		for fl in filenames:
			if x in fl: 
				newpath="/home/joelkiran/Desktop/DATASET/digit_120/1/"
				if not os.path.exists(newpath):
					os.makedirs(newpath)
				shutil.copy("/home/joelkiran/Desktop/DATASET/Numbers_dataset/1/"+fl,newpath+fl)

	elif '2' in dirpath[len(dirpath)-1:]:
		for fl in filenames:
			if x in fl:
				newpath="/home/joelkiran/Desktop/DATASET/digit_120/2/"
				if not os.path.exists(newpath):
					os.makedirs(newpath)
				shutil.copy("/home/joelkiran/Desktop/DATASET/Numbers_dataset/2/"+fl,newpath+fl)
	
	elif '3' in dirpath[len(dirpath)-1:]:
		for fl in filenames:
			if x in fl:	
				newpath="/home/joelkiran/Desktop/DATASET/digit_120/3/"
				if not os.path.exists(newpath):
					os.makedirs(newpath)
				shutil.copy("/home/joelkiran/Desktop/DATASET/Numbers_dataset/3/"+fl,newpath+fl)

	elif '4' in dirpath[len(dirpath)-1:]:
		for fl in filenames:
			if x in fl:		
				newpath="/home/joelkiran/Desktop/DATASET/digit_120/4/"
				if not os.path.exists(newpath):
					os.makedirs(newpath)
				shutil.copy("/home/joelkiran/Desktop/DATASET/Numbers_dataset/4/"+fl,newpath+fl)
			
	elif '5' in dirpath[len(dirpath)-1:]:
		for fl in filenames:
			if x in fl:
				newpath="/home/joelkiran/Desktop/DATASET/digit_120/5/"
				if not os.path.exists(newpath):
					os.makedirs(newpath)
				shutil.copy("/home/joelkiran/Desktop/DATASET/Numbers_dataset/5/"+fl,newpath+fl)

	elif '6' in dirpath[len(dirpath)-1:]:
		for fl in filenames:
			if x in fl:
				newpath="/home/joelkiran/Desktop/DATASET/digit_120/6/"
				if not os.path.exists(newpath):
					os.makedirs(newpath)
				shutil.copy("/home/joelkiran/Desktop/DATASET/Numbers_dataset/6/"+fl,newpath+fl)
			
	elif '7' in dirpath[len(dirpath)-1:]:
		for fl in filenames:
			if x in fl:
				newpath="/home/joelkiran/Desktop/DATASET/digit_120/7/"
				if not os.path.exists(newpath):
					os.makedirs(newpath)
				shutil.copy("/home/joelkiran/Desktop/DATASET/Numbers_dataset/7/"+fl,newpath+fl)
				
					
	elif '8' in dirpath[len(dirpath)-1:]:
		for fl in filenames:
			if x in fl:
				newpath="/home/joelkiran/Desktop/DATASET/digit_120/8/"
				if not os.path.exists(newpath):
					os.makedirs(newpath)
				shutil.copy("/home/joelkiran/Desktop/DATASET/Numbers_dataset/8/"+fl,newpath+fl)

	elif '9' in dirpath[len(dirpath)-1:]:
		for fl in filenames:
			if x in fl:
				newpath="/home/joelkiran/Desktop/DATASET/digit_120/9/"
				if not os.path.exists(newpath):
					os.makedirs(newpath)
				shutil.copy("/home/joelkiran/Desktop/DATASET/Numbers_dataset/9/"+fl,newpath+fl)


		
			
			


		
		
