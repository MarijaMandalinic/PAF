x1=input("koordinata x1: ")
y1=input("koordinata y1: ")
x2=input("koordinata x2: ")
y2=input("koordinata y2: ")
while not x1.isdigit():
    x1=input("koordinata x1: ")
while not y1.isdigit():
    y1=input("koordinata y1: ")
while not x2.isdigit():
    x2=input("koordinata x2: ")
while not y2.isdigit():
    y2=input("koordinata y2: ")
while x1==x2:
    x2=input("koordinata x2: ")
x1=int(x1)
y1=int(y1)
x2=int(x2)
y2=int(y2)
k=(y2-y1)/(x2-x1)
l=-x1*k+y1
if l<0:
    print("y={}x-{}".format(k,abs(l)))
else:
    print("y={}x+{}".format(k,l))