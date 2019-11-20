#Import the required module for text
# to speech conversion
from gtts import gTTS

# Language in which you want to convert
language = 'en'

def gtts_function(mytext, filename):
    txt_file = open(filename + ".txt",'w')
    txt_file.write(mytext)
    txt_file.close()
    mp3_file = gTTS(text=mytext, lang=language, slow=False)
    mp3_file.save(filename + ".mp3")
