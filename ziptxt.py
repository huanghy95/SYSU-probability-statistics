import compress 
import argparse

#添加参数
# parser = argparse.ArgumentParser()
# parser.add_argument('inputFile', help='inputFile')
# parser.add_argument('outputFile', help='ouputFile')
# args=parser.parse_args()
# inputFile=args.inputFile
# outputFile=args.outputFile
inputFile="data.in"
outputFile="data.compress"
mycompress=compress.Compress()
mycompress.ziptxt(inputFile,outputFile)