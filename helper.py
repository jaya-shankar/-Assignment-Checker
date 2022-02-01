import os

def comparator(file,file_1):   
    file=open(file,'r')
    file_1=open(file_1,'r')
    binary_1=list(file.read())
    binary=list(file_1.read())
    file_1.close()
    file.close()
    i=0
    for x,y in zip(binary,binary_1):
        if(x==y):
            i=i+1
        else:
            continue
    try:
        result=(i/len(binary))*100
    except:
        result=100.0
    if result == 100.0:
        return True
    return False

def check_assignment2(path):
    return True
    
    pass