lift_pos=['3','G','6','12','10','11'];       #Initial position of all 6 lifts
print(lift_pos);
while(1):
    f=1;
    n=str(input("Enter your Floor:\t"));     #Requested floor number is get from user
    if n.isalpha():
        if n!='G':                                      #Entered floor number is checked before going to the actual process
           print("Enter correct floor number!!"); 
           f=0;
    elif int(n)>12 or int(n)<1:
        print("Enter correct floor number!!");
        f=0;
    else:
        f=1;
    if(f):
        diff_pre=12;
        for x in range(6):           
           if lift_pos[x]=='G':              #If entered input or list position is 'G' then it is converted to 0
                lift_pos[x]=0;
           if n=='G':
                n=0;
           diff_cur=abs(int(lift_pos[x])-int(n));      #difference between n and each lift position is found 
           if(diff_cur<diff_pre):                      #nearest lift is founded by minimum difference
                pos=x; diff_pre=diff_cur;
           if lift_pos[x]==0:              # value zero is changed to original char 'G'
                lift_pos[x]='G';  
        if n==0:                    
            n='G';
        if(diff_pre==0):                                  
            print("Lift is already in requested floor");
        else:
            print("Nearest lift number\t",pos+1);         #nearest lift is printed
            lift_pos[pos]=n;
    print("Current lift position:",lift_pos);
    y=input("Are You want to call the lift again(Y/N):\t");
    print(y);
    if(y!='Y'):
       break;
    

