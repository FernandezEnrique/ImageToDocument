# ImageToDocument

Python script that gets the text from an image and converts it to a
Word Document (.docx)

## How does it work

We are using opencv and [pytesseract](https://github.com/UB-Mannheim/tesseract/wiki)
 to extract the text from an image.

## How to use it

You need Python3.x and 
[Tesseract](https://github.com/UB-Mannheim/tesseract/wiki) installed.

The `requirements` can be installed running this command.

```bash
pip3 install -r requirements.txt
```

You have 2 ways to import the images.

- Using all the images from a directory (with a specific extension)

```bash
python3 main.py -d <folder> <extension>

python3 main.py -d img/ png
```
 
- Selecting the images by yourself.

```bash
python3 main.py -f <files>

python3 main.py -f img.png book.png letter.png
```

## What are we using

Image processor: https://pypi.org/project/opencv-python/

Tesseract: https://github.com/UB-Mannheim/tesseract/wiki

Word Document: https://pypi.org/project/python-docx/
