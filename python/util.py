import io 

def read_lines(file):
    A = []
    with io.open(file,"r") as f:
        while True:
            a = f.readline()
            if a == "" or a == None:
                break
            A.append(a.strip())
        return A

def read_int_lines(file):
    A = read_lines(file)
    return [int(a) for a in A]
