import compress 
import argparse

#添加参数
parser = argparse.ArgumentParser()
parser.add_argument('inputFile', help='inputFile')
parser.add_argument('outputFile', help='ouputFile')
args=parser.parse_args()
print(args.inputFile)
print(args.outputFile)

# mycompress=compress.Compress()
# mycompress.ziptxt(inputFile,outputFile);