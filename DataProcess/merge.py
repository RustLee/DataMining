import codecs

filepath = "E:/study/NLP/dataset/new data/hotel"
filename = filepath + "/test.txt"
f = codecs.open(filename,mode='r',encoding='utf8')
line = f.readline()
list = []
while line:
    a = line.split()
    b = a[1:2]
    list.append(b)
    result = f.readline()
f.close()
print(list)