import csv
with open("D:\data science\RUNE\LearnPython-main\LearnPython-main\colab\files\SalesData.csv","r")as f:
    sales_data=csv.DictReader(f)
    sales_data=list(sales_data)

sales_data=sales_data


repe_wise={}

for i in sales_data:
    repe_wise["Sales rep"]=repe_wise.get(i['Sales rep'],[])+ [i['Price']]

print(repe_wise)