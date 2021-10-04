from PyPDF2 import PdfFileMerger
import sys
import argparse



def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('pdfs', metavar="files", type=str, nargs='+',
                        help='a list of chosen pdf to merge')
    parser.add_argument('-o', dest='out', type=str, default="result", help='the output file name (default to result)')

    args = parser.parse_args()

    pdfs = args.pdfs
    print("pdfs to concatenate :", pdfs)
    

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf)

    
    output = args.out
    if(output[-4:]!=".pdf"):
        output+=".pdf"
    merger.write(output)
    merger.close()

if __name__ == "__main__":
    # execute only if run as a script
   
    main()
