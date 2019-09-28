from flask import Flask, render_template, request

# import our OCR function
from ocr_core import ocr_function

# import our gTTs function
from gtts_core import gtts_function

app = Flask(__name__)
application = app

# define a folder to store and later serve the images
UPLOAD_FOLDER = '/home/kevinscaringi/mysite/static/uploads/'
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
        # check if there is a file in the request
        if 'file' not in request.files:
            return render_template('index.html',
                                   msg='No file selected')
        file = request.files['file']
        # if no file is selected
        if file.filename == '':
            return render_template('index.html',
                                   msg='No file selected')

        if file and allowed_file(file.filename):

            # save file to static/uploads folder
            file.save(UPLOAD_FOLDER + file.filename)

            # call the OCR function for text
            extracted_text = ocr_function(file)

            if extracted_text:
                # call the gtts function for audio
                gtts_function(extracted_text, file.filename)

                # return text and audio + updated page
                return render_template('index.html',
                                       msg='Successfully processed!',
                                       extracted_text=extracted_text,
                                       img_src=SERVE_FOLDER + file.filename,
                                       mp3_file=SERVE_FOLDER + file.filename + ".mp3")
            else:
               # display error of no text detected
               return render_template('index.html',
                                      msg='No Text Detected',
                                      img_src=SERVE_FOLDER + file.filename)
        else:
            return render_template('index.html',
                                   msg='Invalid File Type')
    elif request.method == 'GET':
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
