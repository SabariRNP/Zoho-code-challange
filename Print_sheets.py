price=0;
order=0;
breadth=[210,297,420,594];       #constants
length=[297,420,594,841];
f=1;
diff=[0,0,0,0];
global i,n;                
def findsheet(b,l):
     global price,order,preorder,ch,prematch;ch=-1;
     for i in range(4):
          if (breadth[i]-b)<0 and(length[i]-l)<0:
               diff[i]=-(abs(breadth[i]-b)*abs(length[i]-l));
          else:
               diff[i]=(breadth[i]-b)*(length[i]-l);  
     thisdict ={diff[0]:"a4",diff[1]:"a3",diff[2]:"a2",diff[3]:"a1"};
     #print("unsorted dict",thisdict);
     sortedlist=sorted(thisdict);#print("sorted dict",sortedlist);
     minpre=500000;
     for i in range(4):
          mincur=sortedlist[i];
          if(sortedlist[i]>0 and mincur<minpre):
               minpre=mincur;
               prematch=thisdict.get(sortedlist[i]);ch=1;#print("prematch=",prematch);
     #print("findsheet ch=",ch);
                    
def checkmatch():
     global j,totorder;
     if(ch!=-1):
         if(len(inputb)>1 and totorder!=0):
             j+=1;
         return 1;
     else:
         if(j==0):
             print("Order cannot be acommodated!!");exit(0);
         return -1;
prematch='a'         
n=int(input("Enter no of orders:\t"));
totorder=n;
if(n<1 or n>10000):
     print("Enter valid number(1-10000)");f=0;
if(f==1):
    inputs={0:1};inputb=[];inputl=[];listb=[];listl=[];
    for i in range(n):
         print("Enter length (in mm) for order  ",i+1);
         xin=int(input());
         print("Enter breadth(in mm) for order  ",i+1);
         yin=int(input());
         if(min(xin,yin) in inputs):
             listb.append(min(xin,yin));listl.append(max(xin,yin));
         else:
             inputs[min(xin,yin)]=max(xin,yin);
    inputs.pop(0);
    for i in sorted(inputs):
         inputb.append(i);inputl.append(inputs[i]);
    for k in range(len(listb)):
        for i in range(len(inputb)):
             if len(inputb)==1:
                  if(listb[k]>=inputb[i]):
                       inputb.insert(i+1,listb[k]);inputl.insert(i+1,listl[k]);break;
             else:
                  if(listb[k]>=inputb[i] and listb[k]<=inputb[i+1]):
                       inputb.insert(i+1,listb[k]);inputl.insert(i+1,listl[k]);break;
    #print("IP after sort",inputb,"\n",inputl);
    
    for i in range(n):
        if(inputb[i]<50 or inputl[i]<50 or inputl[i]>841 or inputb[i]>594):
            print("Paper size too small or too long!!\nOrder cannot be accomodated!!");exit(0);
    #print("len(inputb)",len(inputb));
    while(len(inputb)>0):
         j=0;
         c=1;
         while(c>0 and len(inputb)>=1 and totorder!=0):
               #print("Process start");
               findsheet(sum(inputb[0:j+1]),sum(inputl[0:j+1]));totorder-=1;
               if(totorder>0):
                    c=checkmatch();
               #print("c",c);print("totorder",totorder);print("j",j);
         #print("inputb",inputb);
         if(ch<0):
             j-=1;totorder+=1;
         match=prematch;
         if(match=='a4'):
               order+=1;print("Order",order,"A4 paper - size",sum(inputb[0:j+1]),"X",sum(inputl[0:j+1]),"price Rs.10");price+=10;
         elif(match=='a3'):
               order+=1;print("Order",order,"A3 paper - size",sum(inputb[0:j+1]),"X",sum(inputl[0:j+1]),"price Rs.15");price+=15;
         elif(match=='a2'):
               order+=1;print("Order",order,"A2 paper - size",sum(inputb[0:j+1]),"X",sum(inputl[0:j+1]),"price Rs.20");price+=20;
         elif(match=='a1'):
               order+=1;print("Order",order,"A1 paper - size",sum(inputb[0:j+1]),"X",sum(inputl[0:j+1]),"price Rs.25");price+=25;
         else:
               print("Unmatch");
         #print("last j",j);
         if(match=='a4' or match=='a3' or match=='a2' or match=='a1'):
               while(j>=0):
                    inputb.pop(j);inputl.pop(j);#print("popped");
                    j-=1;           
    print("Total price=\tRs.",price);


