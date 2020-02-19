from flask import Flask, render_template, request, session
from ocr_core import ocr_function
from gtts_core import gtts_function
# from ocr_google import detect_text

app = Flask(__name__)
application = app
application.secret_key = "13t9asd(HHIetho_!$asdj42"

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
        ### Stage 3 -  Advanced Settings ###
        if request.form.get('advanced_ocr') == 'advanced':
            file = session.get("USER_FILE")
            language = request.form.get('language')
            text_style = request.form.get('text-style')
            background_style = request.form.get('background-style')
            extracted_text = 'THIS TEXT CLIPS THE BACKGROUND IMAGE THIS TEXT CLIPS THE BACKGROUND IMAGE'
            gtts_function(extracted_text, UPLOAD_FOLDER + file.filename)
            # return text, audio, txt file + update page
            file = session.get("SERVE_FILE")
            session.clear()
            return render_template('index-stage-3.html',
                                   extracted_text=extracted_text,
                                   img_src=file,
                                   mp3_file=file + ".mp3",
                                   txt_file=file + ".txt")

        if request.form.get('new_file') == 'newFile':
            ### Stage 1 - No File Selected ###
            if 'file' not in request.files:
                session.clear()
                return render_template('index-stage-1.html',
                                       invalidFile='No file selected')
            file = request.files['file']
            if file.filename == '':
                extracted_text = file.filename
                session.clear()
                return render_template('index-stage-1.html',
                                       invalidFile='No file selected')

            ### Stage 2 - File Selected ###
            if file and allowed_file(file.filename):
                file.save(UPLOAD_FOLDER + file.filename)
                session["USER_FILE"] = UPLOAD_FOLDER + file.filename
                session["SERVE_FILE"] = SERVE_FOLDER + file.filename
                extracted_text = ocr_function(file, UPLOAD_FOLDER + file.filename, 'eng')

                ### Text Detected ###
                if extracted_text:
                    gtts_function(extracted_text, UPLOAD_FOLDER + file.filename)
                    # return text, audio, txt file + update page
                    return render_template('index-stage-2.html',
                                           extracted_text=extracted_text,
                                           img_src=SERVE_FOLDER + file.filename,
                                           mp3_file=SERVE_FOLDER + file.filename + ".mp3",
                                           txt_file=SERVE_FOLDER + file.filename + ".txt")
            ### STAGE 1 - Invalid File ###
            else:
                session.clear()
                return render_template('index-stage-1.html',
                                       invalidFile='Invalid File Type')

        ### Stage 1 - No File Selected ###
        if 'file' not in request.files and session.get("USER_FILE") is None:
            session.clear()
            return render_template('index-stage-1.html',
                                   invalidFile='No file selected')
        file = request.files['file']
        if file.filename == '':
            session.clear()
            return render_template('index-stage-1.html',
                                   invalidFile='No file selected')

        ### Stage 2 - File Selected ###
        if file and allowed_file(file.filename):
            file.save(UPLOAD_FOLDER + file.filename)
            session["USER_FILE"] = UPLOAD_FOLDER + file.filename
            session["SERVE_FILE"] = SERVE_FOLDER + file.filename
            extracted_text = ocr_function(file, UPLOAD_FOLDER + file.filename, 'eng')

            ### Text Detected ###
            if extracted_text:
                gtts_function(extracted_text, UPLOAD_FOLDER + file.filename)
                # return text, audio, txt file + update page
                return render_template('index-stage-2.html',
                                       extracted_text=extracted_text,
                                       img_src=SERVE_FOLDER + file.filename,
                                       mp3_file=SERVE_FOLDER + file.filename + ".mp3",
                                       txt_file=SERVE_FOLDER + file.filename + ".txt")
            ### No Text Detected ###
            else:
               session.clear()
               return render_template('index-stage-2.html',
                                      extracted_text='No Text Detected',
                                      img_src=SERVE_FOLDER + file.filename)

        ### STAGE 1 - Invalid File ###
        else:
            session.clear()
            return render_template('index-stage-1.html',
                                   invalidFile='Invalid File Type')
    ### STAGE 1 - Home ###
    elif request.method == 'GET':
        session.clear()
        return render_template('index-stage-1.html')

if __name__ == '__main__':
    app.run(debug=True)
