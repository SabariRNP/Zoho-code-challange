price=0;
n=int(input("Enter no of orders:\t"));
f=1;
if(n<1 or n>10000):
     print("Enter valid number(1-10000)");
     f=0;
x=[];
y=[];
size=[];
f1,f2,f3,f4=1,1,1,1;
if(f==1):
    for i in range(n):
        print("Enter length (in mm) for order  ",i+1);
        xin=int(input());
        x.append(xin);
        print("Enter breadth(in mm) for order  ",i+1);
        yin=int(input());
        y.append(yin);
        size.append(x[i]*y[i]);
        if(xin<1 or yin<1):
            print("Paper size too small\nEnter correct paper size!!");
        else:
            if(size[i]>0 and size[i]<68200):
                if(f1==1):
                     print("Best paper size for order",i+1,"= A4\tPrice Rs.10");price+=10;f1=0;
            elif(size[i]>62370 and size[i]<133300):
                if(f2==1):
                     print("Best paper size for order",i+1,"= A3\tPrice Rs.15");price+=15;f2=0;
            elif(size[i]>124740 and size[i]<262300):
                if(f3==1):
                     print("Best paper size for order",i+1,"= A2\tPrice Rs.20");price+=20;f3=0;
            elif(size[i]>249480 and size[i]<585000):
                if(f4==1):
                     print("Best paper size for order",i+1,"= A1\tPrice Rs.25");price+=25;f4=0;
            else:
                print("Paper size too large!!\nOrder cannot be accomodated");
    print("Total price=\tRs.",price);
