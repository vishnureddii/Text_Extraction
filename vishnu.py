import cv2
from PIL import Image
from pytesseract import pytesseract
camera=cv2.VideoCapture(0)
while True:
     _,image=camera.read()
     cv2.imshow('Text detection',image)
     if cv2.waitKey(1)& 0xFF==ord('s'):
         cv2.imwrite('text.jpg',image)
         break
     camera.release()
 cv2.destroyAllWindows()

def tesseract():
    path_to_tesseract=r"C:\\Users\\phani\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe"
    Imagepath='test12345.png'
    pytesseract.tesseract_cmd=path_to_tesseract
    tet=pytesseract.image_to_string(Image.open(Imagepath))
    f=open("ex.txt","w")
    f.write(tet[:-1])
    print(tet[:-1])
tesseract()
