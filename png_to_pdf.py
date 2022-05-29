import sys
import argparse
import PyPDF2
import img2pdf
from PIL import Image
import os


def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('image', metavar="file", type=str, nargs='+',
                        help='The png file to be converted')
    parser.add_argument('-o', dest='out', type=str, default="result", help='the output file name (default to result)')

    args = parser.parse_args()

    img = args.image[0]
    # opening image
    with Image.open(img) as image:
        
        # converting into chunks using img2pdf
        pdf_bytes = img2pdf.convert(image.filename)
        output_filename = args.out
        if(output_filename[-4:]!=".pdf"):
            output_filename+=".pdf"
        print(f"Convert {img} to {output_filename}")
        with open(output_filename,'wb') as out:
            out.write(pdf_bytes)
    
    print("Success")


if __name__ == "__main__":
    # execute only if run as a script
   
    main()
