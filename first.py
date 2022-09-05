

import csv


with open("D:\data science\python with harsh full\CSV FILE\cars.csv","r") as f:
    cvs_reader=csv.DictReader(f)
    name_reader=list(cvs_reader)

print(name_reader[0])
print(name_reader[0]['Make'])

car_data={}

for i in name_reader:
    car_data[i['Make']]=car_data.get(i['Make'],[])+ [i['Horsepower']]

print(car_data)

for car,hp in car_data.items():
    print(f"{car} : {hp}")

#//////////////// finding the average horse power of each car/////////////////

for car,hp in car_data.items():
    hp_sum=0
    for i in hp:
        hp_sum+=int(i)
        
    car_data[car]=hp_sum/len(hp)
    print(f"{car_data} : ")
