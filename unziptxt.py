import decompress 
import argparse

添加参数
parser = argparse.ArgumentParser()
parser.add_argument('inputFile', help='inputFile')
parser.add_argument('outputFile', help='ouputFile')
args=parser.parse_args()
print(args.inputFile)
print(args.outputFile)

mydecompress=decompress.Decompress()
mydecompress.unziptxt(inputFile,outputFile)