import PyPDF2  
import sys
import argparse

#feature : sort in descending order

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('pdf', metavar="file", type=str, nargs='+',
                        help='main file')
    parser.add_argument('-i', dest = 'to_insert', metavar="file", type=str, nargs='+',
                        help='a list of chosen pdf to insert')
    parser.add_argument('-s', dest = 'to_swap', metavar="file", type=str, nargs='+',
                        help='a list of chosen pdf to swap')
    parser.add_argument('-n', dest = 'numbers', metavar="page numbers", type=str, nargs='+',
                        help='where to insert/swap')
    parser.add_argument('-o', dest='out', type=str, default="result", help='the output file name (default to result)')

    args = parser.parse_args()

    pdf = args.pdf
    print("original :", pdf)

    to_swap = args.to_swap
    print("files to place (swap) in original file :", to_swap)

    to_insert = args.to_insert
    print("files to place (insert) in original file :", to_insert)

    numbers = args.numbers
    numbers = [int(x) for x in numbers]
    print("pages to be swapped/inserted ", numbers)

    assert((to_insert is None) ^ (to_swap is None)) #xor operation

    # See if we're inserting or swapping
    inserting = (to_swap is None)
    

    merger = PyPDF2.PdfMerger(strict = False)

    original = pdf[-1]
    nb_pages = PyPDF2.PdfReader(original, strict = False).getNumPages()
    
    if(inserting):
        L = to_insert
    else:
        L = to_swap
    assert(len(numbers) == len(L))
    index_pdf = 0
    i_old = 0
    for i in numbers:
        
        merger.append(original, pages=(i_old, i-1))
        if(inserting):
            i_old = i-1
        else:
            i_old = i
        merger.append(L[index_pdf])
        index_pdf += 1
    merger.append(original, pages=(i_old, nb_pages))


    
    output = args.out
    if(output[-4:]!=".pdf"):
        output+=".pdf"
    merger.write(output)
    merger.close()

if __name__ == "__main__":
    # execute only if run as a script
   
    main()
