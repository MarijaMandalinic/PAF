def funkcija(x1,y1,x2,y2):
    k=(y2-y1)/(x2-x1)
    l=-x1*k+y1
    if l<0:
        print("y={}x-{}".format(k,abs(l)))
    else:
        print("y={}x+{}".format(k,l))
funkcija(2,6,4,5)

