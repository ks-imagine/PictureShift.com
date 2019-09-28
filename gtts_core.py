#Import the required module for text
# to speech conversion
from gtts import gTTS

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/home/kevinscaringi/mysite/static/uploads/'

# Language in which you want to convert
language = 'en'

def gtts_function(mytext, filename):
    mp3_file = gTTS(text=mytext, lang=language, slow=False)
    mp3_file.save(UPLOAD_FOLDER + filename + ".mp3")
