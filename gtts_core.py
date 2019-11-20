from gtts import gTTS
language = 'en'

def gtts_function(mytext, filename):
    # Create text file
    txt_file = open(filename + ".txt",'w')
    txt_file.write(mytext)
    txt_file.close()
    # Create mp3 file
    mp3_file = gTTS(text=mytext, lang=language, slow=False)
    mp3_file.save(filename + ".mp3")
