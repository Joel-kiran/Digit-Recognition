from pydub import AudioSegment
import os
import shutil
def detect_leading_silence(sound, silence_threshold=-32.0, chunk_size=40):
    '''
    sound is a pydub.AudioSegment
    silence_threshold in dB
    chunk_size in ms

    iterate over chunks until you find the first one with sound
    '''
    trim_ms = 0 # ms

    assert chunk_size > 0 # to avoid infinite loop
    while sound[trim_ms:trim_ms+chunk_size].dBFS < silence_threshold and trim_ms < len(sound):
        trim_ms += chunk_size

    return trim_ms

'''
val=1
for i in range(10):

	sound = AudioSegment.from_file("/home/joelkiran/Desktop/DATASET/Microphone/0/0_"+str(val)+".wav", format="wav")

	start_trim = detect_leading_silence(sound)
	end_trim = detect_leading_silence(sound.reverse())

	duration = len(sound)    
	trimmed_sound = sound[start_trim:duration-end_trim]

	trimmed_sound.export("Mic_processed/0/0_"+str(val)+".wav",format="wav");
	val=val+1;
	
'''
	
for (dirpath, subdir, filenames) in os.walk("/home/joelkiran/Desktop/DATASET/Microphone/"):
		for fl in filenames:
				digit=dirpath.split('/')[::-1][0]
				sound = AudioSegment.from_file("/home/joelkiran/Desktop/DATASET/Microphone/"+digit+'/'+fl, format="wav")

				start_trim = detect_leading_silence(sound)
				end_trim = detect_leading_silence(sound.reverse())

				duration = len(sound)    
				trimmed_sound = sound[start_trim:duration-end_trim]
				if(len(trimmed_sound)!=0):
					newpath="/home/joelkiran/Desktop/DATASET/Mic_processed_18feb/"+digit+"/"
					if not os.path.exists(newpath):
						os.makedirs(newpath)
					trimmed_sound.export(newpath+fl,format="wav");

	
	

