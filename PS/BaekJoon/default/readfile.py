
class Readtxt:
    def __init__(self,file_path):
        self.fpath = file_path
        self.lines = self.read()

    def read(self):
        lines = ""
        with open(self.fpath,"r") as f:
            lines = f.read()

        return lines

if __name__ == "__main__":
    r = Readtxt("default/ex1.txt")
    l = r.read()
    print(l)
