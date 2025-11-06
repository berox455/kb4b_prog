import random

class File_reading:
    def __init__(self):
        self.name = "FileReading"
        self.path = "2. prace_se_soubory/data/citaty.txt"
        with open(self.path, "r") as file:
            self.rfile = file.readlines()
        self.nlines = 0
        self.nchars = 0
        self.nwords = 0     
        
    
    def get_lines(self):
        nlines = 0
        for line in self.rfile:
            nlines += 1

        self.nlines = nlines


    def get_chars(self):
        nchars = 0
        for line in self.rfile:
            line = line.strip("\\n")
            nchars += len(line)

        self.nchars = nchars


    def get_words(self):
        nwords = 0
        for line in self.rfile:
            line = line.strip("\\n")
            words = line.split(" ")
            nwords += len(words)

        self.nwords = nwords

    
    def get_stats(self):
        self.get_lines()
        self.get_chars()
        self.get_words()

        print("nlines:", self.nlines)
        print("nchars:", self.nchars)
        print("nwords:", self.nwords)


test = File_reading()

test.get_stats()