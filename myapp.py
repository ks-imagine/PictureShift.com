from flask import Flask, render_template, request
from ocr_core import ocr_function
from gtts_core import gtts_function

app = Flask(__name__)
application = app

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/home/kevinscaringi/PictureShift.com/static/uploads/' #PythonAnywhere
# UPLOAD_FOLDER = '/Users/Kevin/Documents/PictureShift.com/static/uploads/' #Mac
SERVE_FOLDER = '/static/uploads/'

# allow files of a specific type
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

# function to check the file extension
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route and function to handle the web page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        ### STAGE 1 - NO FILE SELECTED ###
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('index-new.html',
                                   invalidFile='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('index.html',
                                   invalidFile='No file selected')

        ### STAGE 2 ###
        if file and allowed_file(file.filename):
            # save file to static/uploads folder
            file.save(UPLOAD_FOLDER + file.filename)
            # call the OCR function for text
            extracted_text = ocr_function(file, UPLOAD_FOLDER + file.filename)

            if extracted_text:
                gtts_function(extracted_text, UPLOAD_FOLDER + file.filename)
                # return text, audio, txt file + update page
                return render_template('index.html',
                                       msg='Successfully processed!',
                                       extracted_text=extracted_text,
                                       img_src=SERVE_FOLDER + file.filename,
                                       mp3_file=SERVE_FOLDER + file.filename + ".mp3",
                                       txt_file=SERVE_FOLDER + file.filename + ".txt")
            ### STAGE 2 - NONE DETECTED ###
            else:
               return render_template('index.html',
                                      msg='No Text Detected',
                                      img_src=SERVE_FOLDER + file.filename)
        ### STAGE 1 - INVALID FILE ###
        else:
            return render_template('index-new.html',
                                   invalidFile='Invalid File Type')
    ### STAGE 1 ###
    elif request.method == 'GET':
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
