import os 

for (root, directories, files) in os.walk("."):
    for fileName in files:
        full_fileName = os.path.join(root,fileName)
    print (full_fileName)


data1 = open("D:\\UAIC\\an3\\python\\partial\\input\\khyge1.mail","rb").read() 
print (len(data1)) 
print (data1[0])
