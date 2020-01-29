from PIL import Image
import pytesseract

tessdata_dir_config = '--tessdata-dir "/home/kevinscaringi/tessdata"' #PythonAnywhere
# tessdata_dir_config = '--tessdata-dir "/Users/Kevin/Documents/tessdata_fast"' #Mac
def ocr_function(file, filename, language):
    # Convert Image to Grey
    greyImage = Image.open(file).convert('LA')

    # Extract text from image
    text = pytesseract.image_to_string(greyImage, lang=language, config=tessdata_dir_config)
    greyImage.save(filename + "-gray.png")
    return text
