import pytesseract
import sys
import re
from PIL import Image
import tempfile
from pdf2image import convert_from_path

if (len(sys.argv) != 2):
    print("Usage: infocheck.py <pdf_filename>\n")
#filename = '/Users/woonie/Downloads/testtt.pdf'
filename = sys.argv[1]
pattern = re.compile('([0-9]{2}(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|[3][01]))-([1-4][0-9]{6})', re.MULTILINE)


with tempfile.TemporaryDirectory() as temp_dir:
    images = convert_from_path(filename, output_folder=temp_dir)

    temp_images = []

    for i in range(len(images)):
        image_path = temp_dir+str(i)+'.jpg'
        images[i].save(image_path, 'JPEG')
        temp_images.append(image_path)
        m = pytesseract.image_to_string(Image.open(temp_images[i]))
        s = pattern.search(m)
        if(s):
            print(s)
        else:
            print("There is no private information")



