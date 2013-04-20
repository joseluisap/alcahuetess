import os,sys,numpy,constants

aDefault=1
# os.chdir('C:\\Documents and Settings\\Jose\\Mis documentos\\biblioteca\\papers\\propios\\wrcm\\pythonplots')

class test:
    def __init__(self,a=aDefault):
        self.a=a
        print self.a
        b=numpy.pi
        print b
def ftest1(t,a):
    if abs(t) < a:
        return(1.0)
    else:
        return(0.0)
def ftest2(a,b):
    if a != b:
        raise IOError,"a and b must be equal"
def ftest3():
    print(constants.c)