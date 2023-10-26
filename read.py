with open("sample.ini") as file:
        data = file.read()

def reader(data):
     for x in data.split('\n'):
        print(x)
        
        y= x.split("=")
        print(y[0])
reader(data)
