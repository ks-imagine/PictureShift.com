from PIL import Image
import pytesseract

def ocr_function(file, filename):
    # Convert Image to Grey
    greyImage = Image.open(file).convert('LA')
    # Extract text from image
    text = pytesseract.image_to_string(greyImage)
    greyImage.save(filename + "-gray.png")
    return text
