#/////////////////////////// mean , median , mode //////////////////////////////////





def mean_meadian_mode(user,choice):
    if (choice=="1" or choice=="mean"):
        sum_num=0
        for i in user:
            sum_num+=i
        return (sum_num/len(user))
    elif(choice=="2" or choice=="mode"):
        mode_ele={}
        
        for i in user:
            cnt=user.count(i)
            mode_ele[i]=cnt
        

        return (max(mode_ele,key=mode_ele.get))
    if (choice=="3" or choice=="median"):
        asced=[]
        for i in range(len(user)):
            asced.append(min(user))
            user.remove(min(user))
        print(f"List arranged in ascending order {asced}")
        if (len(asced)%2)==0:
            pos1=int(len(asced)/2)
            pos2=int(len(asced)/2)+1
            median=asced[pos1-1]+asced[pos2-1]
            median=median/2
            return median
        if (len(asced)%2)!=0:
            pos3=int(len(asced)/2)
            return asced[pos3]
    
        


def quartile(inpu,ch):
    if ch=="1":
        asc=[]
        for i in range(len(inpu)):
            asc.append(min(inpu))
            inpu.remove(min(inpu))
        rang=asc[-1]-asc[0] 
        q1=(len(asc)+1)/4
        q1=round(q1)
        q1=asc[q1]
        q2=(len(asc)+1)/2
        q2=round(q2)
        q2=asc[q2]
        q3=3/4*(len(asc)+1)
        q3=round(q3)
        q3=asc[q3]
        iqr=q3-q1
        return  rang, q1,  q2,  q3,  iqr
    elif ch=="2":

        mean_dev=mean_meadian_mode(inpu,"1")
        print(mean_dev)
        
        deviation=[]
        for i  in range(len(inpu)):
            res=abs(inpu[i]-mean_dev)
            deviation.append(res)
        return deviation
    elif ch=="3":
        mea_var=mean_meadian_mode(inpu,"1")
        new_list=[]
        sum=0
        for i in range(len(inpu)):
            ele=inpu[i]-mea_var
            new_list.append(ele**2)
        for i in new_list:
            sum+=i
        return (sum/len(new_list))    
    



'''
       






#////////////////////// SKEWNESS OF THE DATA ///////////////////////


def skewness(data):
    mean_of_data=mean_meadian_mode(data,"1")
    median_of_data=mean_meadian_mode(data,'3')
    varaince_of_data=quartile(data,'3')
    standard_dev=sqrt(varaince_of_data)
    print(standard_dev)
    skewness=(3*(mean_of_data-median_of_data))/standard_dev
    if (skewness>=0.5 and skewness<=-0.5):
        print("symmetric Skewness")
    else:
        print('asd')





def ch():
    
    x=list(map(int,input("Enter the list of elements ").split()))
    user_choice=input("Enter choice 1. Mean  2:Meadian 3: Mode 4: Range Q1 Q2 Q3  5: Deviation  6: Variance  '\n' Do you want to perform more operation  : y/n  ")
    user_choice=user_choice.lower()
    if user_choice=="1":
        print(mean_meadian_mode(x,"1"))
    elif user_choice=="2":
        print(mean_meadian_mode(x,"2"))
    elif user_choice=="3":
        print(mean_meadian_mode(x,"3"))
    elif user_choice=="4":
        print(quartile(x,"1"))
    elif user_choice=="5":
        print(quartile(x,"2"))
    elif user_choice=="6":
        print(quartile(x,"3"))
    elif user_choice=='y':
       
        ch()
    elif user_choice=="n":
        print("Closed")


'''