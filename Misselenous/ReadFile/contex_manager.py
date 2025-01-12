class OpenFile:
    def __init__(self, filename, mode) :
        self.filename = filename
        self.mode = mode

    def _enter__(self):
        self. file = open(self.filename, self.mode)
        return self.file

    def __exit__(self):
        self. file. close()


with OpenFile('sample1.txt', 'W') as f:
    f.write('Testing')
    
print(f.closed)
