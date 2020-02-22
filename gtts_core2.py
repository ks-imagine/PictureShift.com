from gtts import gTTS
language = 'en'

UPLOAD_FOLDER = '/home/kevinscaringi/PictureShift.com/static/uploads/' #PythonAnywhere
# UPLOAD_FOLDER = '/Users/Kevin/Documents/PictureShift.com/static/uploads/' #Mac

def gtts_function2(mytext):
    # Create text file
    txt_file = open(UPLOAD_FOLDER + "stage-3.txt",'w')
    txt_file.write(mytext)
    txt_file.close()
    # Create mp3 file
    mp3_file = gTTS(text=mytext, lang=language, slow=False)
    mp3_file.save(UPLOAD_FOLDER + "stage-3" + ".mp3")
