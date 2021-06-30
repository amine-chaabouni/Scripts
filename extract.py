from PyPDF2 import PdfFileWriter, PdfFileReader
import argparse	


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(description='extract pages from pdf file')
	parser.add_argument('-n', dest="pages", metavar='n', type=int, nargs='+',
		            help='the pages to be extracted')
	parser.add_argument('--except', dest="type_of_extraction", action = "store_const", const=True, default=False, help='type of extraction')
	parser.add_argument('file', nargs=1,
		            help='input file name')
	parser.add_argument('-o', dest='output_name', default="result.pdf",
		            help='outuput file name')
		            

	args = parser.parse_args()
	print(args)
	inputpdf = PdfFileReader(open(args.file[0], "rb"))
	output = PdfFileWriter()
	if args.type_of_extraction:
		pages = [x for x in range(1, inputpdf.numPages+1) if not (x in args.pages)]
	else:
		pages = args.pages
	#for i in range(inputpdf.numPages):
	for i in pages:
	    output.addPage(inputpdf.getPage(i-1))
	    with open(args.output_name, "wb") as outputStream:
	    	output.write(outputStream)
