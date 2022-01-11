import glob,os
from PIL import Image
from pytesseract import pytesseract
# Defining paths to tesseract.exe
# and the image we would be using

def parseImg():
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"  

    print("Input statblock file")
    image_path = input()  
    if(os.path.exists(image_path)==False): #Force resubmission until filename is valid
        while(os.path.exists(image_path)==False):
            print("Invalid Filename/ File does not exist")
            image_path = input()  
        
    # Opening the image & storing it in an image object
    img = Image.open(image_path)
    
    # Providing the tesseract executable
    # location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract
    
    # Passing the image object to image_to_string() function
    # This function will extract the text from the image
    rawText = pytesseract.image_to_string(img)
    
    # Displaying the extracted text
    # print(rawText[:-1])
    return rawText

def save_to_file(name, text): # Saves statblock raw data to file
    #with open(image_path[:(len(image_path)-4)]+".txt", 'w') as f:
    with open(name+".txt", 'w') as f:
        f.write(text)#Write to file of the same name

def main():

    print("How many images. (Input -1 for all)")
    img_num= input()
    while(img_num<-1):
        print("Invalid Number (Input -1 for all)")
        file_name = input()
    if(img_num==-1):
        entire_directory= True

    if(entire_directory):
        print("Enter Directory")
        directory_name = input()
        while(os.path.exists(directory_name)==False):
            print("Invalid Filename/ File does not exist")
            directory_name = input()
            directory = "/"+directory_name
        for file in os.listdir(directory):
            if file.endswith(".png"):
                print(os.path.join(directory, file))
        
    else: #Repeat Manual entry for each img
        for i in range(img_num):
            print("Input filename")
            file_name = input()  
            if(os.path.exists(file_name)==False): #Force resubmission until filename is valid
                while(os.path.exists(file_name)==False):
                    print("Invalid Filename/ File does not exist")
                    file_name = input()

            save_to_file( file_name, parseImg())
            a_file = open(file_name+".txt")

            lines = a_file.readlines()
            lines  = list(filter(("\n").__ne__, lines )) # Remove all blank lines
            statlist = [lines[0], lines[1], lines[2]]
            print(statlist)
    


if __name__ == "__main__":
    main()


