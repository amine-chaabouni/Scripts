from PyPDF2 import PdfFileMerger
import argparse	


if __name__ == "__main__":
	
	parser = argparse.ArgumentParser(description='extract pages from pdf file')
	parser.add_argument('-f', dest="files", nargs='+',
		            help='the files to be merged')
	parser.add_argument('-o', dest='output_name', default="result.pdf",
		            help='outuput file name')
		            

	args = parser.parse_args()
	print(args)


	merger = PdfFileMerger()

	for pdf in args.files:
	    merger.append(pdf)
	
	merger.write(args.output_name)
	merger.close()


