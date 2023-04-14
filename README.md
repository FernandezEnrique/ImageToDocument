# ImageToDocument

ImageToDocument is a Python script that allows you to extract text from images and convert it into a Word document (.docx).

## How it works

The script utilizes OpenCV and [pytesseract](https://github.com/UB-Mannheim/tesseract/wiki) to perform optical character recognition (OCR) and extract text from images.

## How to use

To use the script, you need to have Python 3.x and Tesseract installed. You can install the required dependencies by running the following command:

```bash
pip3 install -r requirements.txt
```

There are two methods to import images into the script:

1. Using all images from a directory with a specific file extension:

```bash 
python3 main.py -d <folder> <extension>

python3 main.py -d img/ png
```

2. Selecting images manually:

```
python3 main.py -f <files>

python3 main.py -f img.png book.png letter.png
```

## How to contribute

If you're interested in contributing to ImageToDocument, you're welcome to submit pull requests or open issues with your suggestions, bug reports, or feature requests. Here's how you can contribute:

1. Fork the repository.
2. Create a new branch for your contribution.
3. Make your changes and commit them with descriptive commit messages.
4. Push your changes to your forked repository.
5. Submit a pull request to the main repository.

We appreciate your contributions to make ImageToDocument even better! Thank you in advance for your support.

## Technologies used

- Image processing: [OpenCV](https://pypi.org/project/opencv-python/)
- Optical character recognition (OCR): [pytesseract](https://github.com/UB-Mannheim/tesseract/wiki)
- Word document creation: [python-docx](https://pypi.org/project/python-docx/)
