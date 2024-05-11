import matplotlib.pyplot as plt

def drawline(x1,x2,y1,y2):
    dy=y2-y1 
    dx=x2-x1
    m=dy/dx
    x=[]
    y=[]
    p=(2*dy)-dx
    xnext=x1
    ynext=y1
    x.append(xnext)
    y.append(ynext)
    while(xnext<x2 or ynext<y2):
        if(m<1):
            xnext=x1+1
            if(p<0):
                ynext=y1
                p=p+(2*dy)
            else:
                ynext=y1+1
                p=p+(2*(dy-dx))
        else:
            ynext=y1+1
            if(p<0):
                xnext=x1
                p=p+(2*dx)
            else:
                xnext=x1+1
                p=p+(2*(dx-dy))
        x.append(xnext)
        y.append(ynext)
        x1=xnext
        y1=ynext
    print("x coordinates are :- ",x)
    print("y coordinates are :- ",y)
    plt.plot(x,y)
    plt.show()

X1=int(input("Enter x coordinate of starting point of line : "))
Y1=int(input("Enter y coordinate of starting point of line : "))
X2=int(input("Enter x coordinate of ending point of line : "))
Y2=int(input("Enter x coordinate of ending point of line : "))
drawline(X1,X2,Y1,Y2)