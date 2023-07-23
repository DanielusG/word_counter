class Counter:
    def __init__(self, path: str, countLines: bool = False):
        self.path = path
        self.count = 0
        self.isIgnored = False
        self.notAFile = False
        self.countLines = countLines
        self.loadIgnore()

    def openFile(self):
        self.file = open(self.path, 'r')

    def countChars(self):
        for ignore in self.ignore:
            if ignore in self.path:
                self.count = 0
                self.isIgnored = True
                return
        try:
            if self.countLines:
                self.count = len(self.file.readlines())
            else:
                self.count = len(self.file.read())
        except:
            self.count = 0
            self.notAFile = True

    def closeFile(self):
        self.file.close()

    def loadIgnore(self):
        self.ignore = []
        try:
            with open('.ignorecount', 'r') as file:
                for line in file:
                    self.ignore.append(line.strip())
        except FileNotFoundError:
            print('No .ignorecount file found. It\'s not a problem, but you can create it if you want to ignore some files.')

    # open file, count chars, close file
    def analyze(self):
        self.openFile()
        self.countChars()
        self.closeFile()