import glob,os
from PIL import Image
from pytesseract import pytesseract

class Statblock:

    name = ""
    image_path = ""
    raw_text = ""

    def __init__(self, name, img):
        self.name = name
        self.image_path = img
    
    def parse_img(self):
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  
        
        # Providing the tesseract executable
        # location to pytesseract library
        pytesseract.tesseract_cmd = path_to_tesseract

        #Use for input based parsing
        """
        print("Input statblock file")
        image_path = input()  
        """
        if(os.path.exists(self.image_path)==False): #Force resubmission until filename is valid
            while(os.path.exists(self.image_path)==False):
                print()
                exit("Invalid Filename/ File does not exist for ",self.name)
                self.image_path = input()  
            
        # Opening the image & storing it in an image object
        img = Image.open(self.image_path)
        
        # Passing the image object to image_to_string() function
        # This function will extract the text from the image
        rawText = pytesseract.image_to_string(img)
        
        # Displaying the extracted text
        # print(rawText[:-1])
        return rawText

    def set_raw(self):
        self.raw_text = self.parse_img()

    def save_to_file(name, text): # Saves statblock raw data to file
        #with open(image_path[:(len(image_path)-4)]+".txt", 'w') as f:
        with open(name+".txt", 'w') as f:
            f.write(text)#Write to file of the same name


    def raw(self):
        return self.raw_text