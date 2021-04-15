lift_pos=['3','G','6','12','10','11'];
print(lift_pos);
while(1):
    f=1;
    n=str(input("Enter your Floor:\t")); 
    if n.isalpha():
        if n!='G':
           print("Enter correct floor number!!");
           f=0;
    elif int(n)>12:
        print("Enter correct floor number!!");
        f=0;
    else:
        f=1;
    if(f):
        diff_pre=12;
        for x in range(6):
           if lift_pos[x]=='G':
                lift_pos[x]=0;
           if n=='G':
                n=0;
           diff_cur=abs(int(lift_pos[x])-int(n));
           if(diff_cur<diff_pre):
                pos=x; diff_pre=diff_cur;
           if lift_pos[x]==0:
                lift_pos[x]='G';  
        if n==0:
            n='G';
        if(diff_pre==0):
            print("Lift is already in requested floor");
        else:
            print("Nearest lift number\t",pos+1);
            lift_pos[pos]=n;
    print("Current lift position:",lift_pos);
    y=input("Are You want to call the lift again(Y/N):\t");
    print(y);
    if(y!='Y'):
       break;
    

