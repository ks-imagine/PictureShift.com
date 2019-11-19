#Import the required module for text
# to speech conversion
from gtts import gTTS

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/home/kevinscaringi/PictureShift.com/static/uploads/' #PythonAnywhere
#UPLOAD_FOLDER = '/Users/Kevin/Documents/PictureShift.com/static/uploads/' #PC

# Language in which you want to convert
language = 'en'

def gtts_function(mytext, filename):
    txt_file = open(UPLOAD_FOLDER + filename + ".txt",'w')
    txt_file.write(mytext)
    txt_file.close()
    mp3_file = gTTS(text=mytext, lang=language, slow=False)
    mp3_file.save(UPLOAD_FOLDER + filename + ".mp3")
