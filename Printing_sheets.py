price=0;
n=int(input("Enter no of orders:\t"));
x=[];
y=[];
size=[];
for i in range(n):
    print("Enter length (in mm) for order  ",i+1);
    xin=int(input());
    x.append(xin);
    print("Enter breadth(in mm) for order  ",i+1);
    yin=int(input());
    y.append(yin);
    size.append(x[i]*y[i]);
    if(size[i]>0 and size[i]<68200):
        print("Best paper size for order",i+1,"= A4\tPrice Rs.10");price+=10;
    elif(size[i]>62370 and size[i]<133300):
        print("Best paper size for order",i+1,"= A3\tPrice Rs.15");price+=15;
    elif(size[i]>124740 and size[i]<262300):
        print("Best paper size for order",i+1,"= A2\tPrice Rs.20");price+=20;
    elif(size[i]>249480 and size[i]<585000):
        print("Best paper size for order",i+1,"= A1\tPrice Rs.25");price+=25;
    else:
        continue;
print("Total price=\tRs.",price);
