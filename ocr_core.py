from PIL import Image
import pytesseract
# import cv2

def ocr_function(filename):
    # image = cv2.imread(filename)
    # # Convert image to grayscale
    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # # If user enter 1, Process Threshold
    # gray = cv2.medianBlur(gray, 3)
    # # store grayscale image as a temp file to apply OCR
    # cv2.imwrite(filename, gray)
    # load the image as a PIL/Pillow image, apply OCR, and then delete the temporary file
    text = pytesseract.image_to_string(Image.open(filename))
    return text
