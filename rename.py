import os 
import random 

def rename_list(SRC, DIR, LIST):
	i = 0
	for filename in LIST: 
		dst ="Safe-" + str(i) + ".jpg"
		src =SRC+ filename 
		dst =DIR+ dst 
           
		os.rename(src, dst) 
		i += 1
	


def main(): 
	
	PERC = 0.75
	TRAIN_DIR = "/home/meg/Downloads/data/train/safe/"
	VAL_DIR = "/home/meg/Downloads/data/val/safe/"
	shuffled = os.listdir(TRAIN_DIR)
	random.shuffle(shuffled)
	NUM = len(shuffled)
	x = int(PERC*NUM)
	train_list = shuffled[0:x]
        val_list = shuffled[x:NUM]
	rename_list(TRAIN_DIR, TRAIN_DIR,train_list)
	rename_list(TRAIN_DIR, VAL_DIR,val_list)
	#rename_list(TRAIN_DIR, TRAIN_DIR, os.listdir(TRAIN_DIR))
	#rename_list(VAL_DIR, VAL_DIR, os.listdir(VAL_DIR))
	
	

# Driver Code 
if __name__ == '__main__': 
	
	# Calling main() function 
	main() 

