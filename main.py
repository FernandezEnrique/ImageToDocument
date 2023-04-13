import sys
import os
from os import listdir
from os.path import isfile, join
from pytesseract import pytesseract

class ImageConversor:
    def __init__(self):
        # Argument counter
        self.argc = len(sys.argv)

        # Files or arguments
        self.mode = None

        # Images
        self.images = []

        # https://github.com/UB-Mannheim/tesseract/wiki
        
        # tesseract path
        pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        self.check_args()

        self.get_images(self.argc)

    def get_images(self):
        '''Stores in self.images all the images provided'''

        # If user is using a directory
        if self.mode == "d":
            # Checks if the directory exists
            if os.path.exists(sys.argv[2]):
                # Saves files with the extension provided
                self.images = [f for f in listdir(sys.argv[2]) 
                               if isfile(f) and
                               f.endswith(sys.argv[3])]
            else:
                print("Directory does not exists")
                exit()
        else:
            for f in range(2, len(sys.argv)):
                # Adds every image that is a file
                if isfile(f):
                    self.images.append(f)

    def check_args(self):
        '''Checks users parameters'''
        if self.argc < 3:
            # Not enough arguments were provided
            print("Error. Expecting at least 2 argument.")
            exit()
        elif sys.argv[1] == "-f":
            if self.argc != 4:
                print("You must include directory and extension.")
                exit()
            # User is providing files
            self.mode = "f"
        elif sys.argv[1] == "-d":
            # User is providing directories
            self.mode = "d"
        elif sys.argv[1] == "-h":
            # Show help
            pass
        else:
            print("Please, select a mode")


if __name__ == '__main__':
    ImageConversor()
