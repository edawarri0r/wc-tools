# ccwc to do 

#1 import argparse
import argparse

#import sys needed to read from standard input if no filename is specified 
import sys


#1. create the command line using argparse.ArgumentParser()
#argparse.ArgumentParser It is a container for argument specifications and has options that apply to the parser as whole
parser = argparse.ArgumentParser(
    prog='ccwc'
    ,usage='ccwc [options] [filename]'
    ,description='WC TOOL: word, line, character,and byte count just like UNIX command line tool')

#2. use argparse.add_argument to define the argument (-v, --v will be doing what) 

#nargs="?" is needed to make sure that filename can be optional, this is to adapt the case to support being able to read from standard input if no filename is specified
parser.add_argument('filename', nargs="?", help="File Name, If no options used then shows result of -c -l -w")

parser.add_argument('-c','--count',action='store_true', help="Count number of bytes in the file")
parser.add_argument('-l','--lines',action='store_true', help="Count number of lines in the file")
parser.add_argument('-w','--words',action='store_true', help="Count number of words in the file")
parser.add_argument('-m','--characters',action='store_true', help="Count number of characters in a file")

#3. call parse_args()
args = parser.parse_args()

#4. read file using open while get the filename from parse_args
if args.filename:
    try:
        #have to use encoding utf-8 if you dont use 'b' on open
        with open(args.filename,"r",encoding="utf-8") as f:
            data = f.read()
    except FileNotFoundError:
        print("File not found")
        exit(1)
else : 
    #sys.stdin.read is to read data from input
    data = sys.stdin.read()


#5. create class with method to process the file

class Count: 
    def __init__(self,data):
        self.data = data
    
    def count_bytes(self):
        #since we only use "r" then has to encode it 
        return len(self.data.encode("utf-8"))

    def count_lines(self):
        return len(self.data.split('\n'))-1

    def count_words(self):
        return len(self.data.split())

    def count_characters(self):
        return len (self.data)
    

    def run(self):
        if args.count:
            print(self.count_bytes())
        elif args.lines:
            print(self.count_lines())
        elif args.words:
            print(self.count_words())
        elif args.characters:
            print(self.count_characters())
        else:
            print(f"{self.count_bytes()}  {self.count_lines()} {self.count_words()}")

Count(data).run()