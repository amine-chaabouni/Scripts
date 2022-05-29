# Script to change the quality of a pdf file
# $1 is the file to be change
# $2 is the name of the output file
# $3 is the setting of the quality. Choose from [screen, ebook, printer, prepress, default]

gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/$3 -dNOPAUSE -dQUIET -dBATCH -sOutputFile=$2 $1
