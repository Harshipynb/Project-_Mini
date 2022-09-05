import csv


with open("D:\data science\python with harsh full\CSV FILE\cars.csv","r") as f:
    cvs_reader=csv.DictReader(f)
    name_reader=list(cvs_reader)


car_newdata={}

for i in name_reader:
    car_newdata[i["Make"]]=car_newdata.get(i['Make'],[])+[i["Horsepower"]]



#/////////////////////   finding avg horse power of the cars///////////////////////////////////
car_list={}

for key, value in car_newdata.items():
    print(f"Car Brand name{key} and Horse power {value}")
    hp_sum=0

    for i in value:
        hp_sum+=int(i)
    
    car_list[key]=hp_sum/len(value)
    
print(f"New data of average gorse power {car_list}")


#////////////////// 
max_hp={}
for i in car_list:
    car_list[i]=int(car_list[i])
    if car_list[i]>500:
        max_hp[i]=car_list[i]
print(max_hp)