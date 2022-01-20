#!/bin/python3

from argparse import ArgumentParser, FileType, ArgumentDefaultsHelpFormatter
from pathlib import Path
from PyPDF2 import PdfFileWriter, PdfFileReader
from os import remove

def Overlay(inputfile, outputfile):
    back_ground = PdfFileReader(open(inputfile, "rb"))
    over_lay = PdfFileReader(open(str(inputfile) + "-textonly.pdf", "rb"))
    output = PdfFileWriter()

    for page_num in range(0, back_ground.numPages):
        each_page = back_ground.getPage(page_num)
        each_page.mergePage(over_lay.getPage(page_num))

        output.addPage(each_page)
        
    outputStream = open(outputfile, "wb")
    output.write(outputStream)
    outputStream.close()

def remove_img(inputfile):

    inputStream = open(inputfile, "rb")
    outputStream = open(str(inputfile) + "-textonly.pdf", "wb")

    src = PdfFileReader(inputStream)
    output = PdfFileWriter()

    [output.addPage(src.getPage(i)) for i in range(src.getNumPages())]
    output.removeImages()

    output.write(outputStream)

    outputStream.close()
    inputStream.close()


if __name__ == "__main__":

    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-o", "--output", type=Path, required=True, help="出力ファイル指定")
    parser.add_argument("-i", "--input", type=Path, required=True, help="入力ファイル指定")

    args = parser.parse_args()

    inputfile = args.input
    outputfile = args.output

    remove_img(inputfile)
    Overlay(inputfile, outputfile)

    remove(str(inputfile) + "-textonly.pdf")