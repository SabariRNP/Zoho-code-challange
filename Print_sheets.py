price=0;
order=0;
breadth=[210,297,420,594];       #constants
length=[297,420,594,841];
f=1;
diff=[0,0,0,0];
global i,n;                
def findsheet(b,l):                     #best paper for given length,breadth is found here
     global price,order,preorder,ch,prematch;ch=-1;
     for i in range(4):
          if (breadth[i]-b)<0 and(length[i]-l)<0:                  #difference between given breadth and alloted paper breadth(for all 4 paper) is calculated.
               diff[i]=-(abs(breadth[i]-b)*abs(length[i]-l));      #similarly difference is calculated for length.then two diff is multiplied. 
          else:
               diff[i]=(breadth[i]-b)*(length[i]-l);  
     thisdict ={diff[0]:"a4",diff[1]:"a3",diff[2]:"a2",diff[3]:"a1"};     #above calculated values are stored in dictionary and sorted
     #print("unsorted dict",thisdict);
     sortedlist=sorted(thisdict);#print("sorted dict",sortedlist);   
     minpre=500000;
     for i in range(4):                                  #least positive value(key in dictionary) in the dictionary is founded
          mincur=sortedlist[i];                          #then corresponding value in the dictionary is required paper.  
          if(sortedlist[i]>0 and mincur<minpre): 
               minpre=mincur;
               prematch=thisdict.get(sortedlist[i]);ch=1;#print("prematch=",prematch);
     #print("findsheet ch=",ch);
                    
def checkmatch():
     global j,totorder;
     if(ch!=-1):                                #if best paper is founded, j value is incremented and
         if(len(inputb)>1 and totorder!=0):     #again best paper match for incremented length and breadth is calculated 
             j+=1;                              #until when match occur
         return 1;
     else:
         if(j==0):
             print("Order cannot be acommodated!!");exit(0);
         return -1;
prematch='a'         
n=int(input("Enter no of orders:\t"));             #no of orders is stores in variable n
totorder=n;
if(n<1 or n>10000):                                #here n value is checked, i.e, n is valid value or not
     print("Enter valid number(1-10000)");f=0;   
if(f==1):
    inputs={0:1};inputb=[];inputl=[];listb=[];listl=[];
    for i in range(n):
         print("Enter length (in mm) for order  ",i+1);        #length and breadth for each order is get and stored in list
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
    for k in range(len(listb)):                               #length list and breadth list are sorted
        for i in range(len(inputb)):
             if len(inputb)==1:
                  if(listb[k]>=inputb[i]):                 
                       inputb.insert(i+1,listb[k]);inputl.insert(i+1,listl[k]);break;
             else:
                  if(listb[k]>=inputb[i] and listb[k]<=inputb[i+1]):
                       inputb.insert(i+1,listb[k]);inputl.insert(i+1,listl[k]);break;
    #print("IP after sort",inputb,"\n",inputl);
    
    for i in range(n): 
        if(inputb[i]<50 or inputl[i]<50 or inputl[i]>841 or inputb[i]>594):            #all entered length and breadth values are checked
            print("Paper size too small or too long!!\nOrder cannot be accomodated!!");exit(0);
    #print("len(inputb)",len(inputb));
    while(len(inputb)>0):
         j=0;
         c=1; 
         while(c>0 and len(inputb)>=1 and totorder!=0):                 #initially first order(length & breadth) values are feeded to findsheet function
               #print("Process start");                                  #if best paper match is found, length and breadth values are incremented(i.e, sum of two order)
               findsheet(sum(inputb[0:j+1]),sum(inputl[0:j+1]));totorder-=1;   #while loop stopped when paper match is not occur
               if(totorder>0): 
                    c=checkmatch();
               #print("c",c);print("totorder",totorder);print("j",j);
         #print("inputb",inputb);
         if(ch<0):
             j-=1;totorder+=1;
         match=prematch;                            #price is calculated for previously matched one
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
         if(match=='a4' or match=='a3' or match=='a2' or match=='a1'):         #length , breadth for taken orders are removed from the list inputl and inputb
               while(j>=0):                                                  #process will continue upto finishing all orders
                    inputb.pop(j);inputl.pop(j);#print("popped");
                    j-=1;           
    print("Total price=\tRs.",price);        #total price for all order is printed


