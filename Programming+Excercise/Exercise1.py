import csv
import math

def round_number(n, decimals=2):
    multiplier = 10 ** decimals
    return math.ceil(n*multiplier - 0.5) / multiplier

def exchange_max(list): 
    return max(set(list), key = list.count)

# Variable declaration
exchanges=[] 
valueEUR=[]
companies=[]
dates_Significance=[]
months=['Jan','Feb','March','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
transactions=[]

#Reading csv file
with open ('2017.csv','r',encoding="utf8") as csv_file:
    
    csv_reader = csv.reader(csv_file,delimiter=',')

    for row in csv_reader:
        exchanges.append(row[-1])
        if row[-4]=='3':
            dates_Significance.append(row[-15])

        if "201706" in row[-15]:
            valueEUR.append(float(row[-8]))
            companies.append(row[2])

        

#Percentage calculation
for i in range(1,13):
    
    count=0
    if i<10:
        date="20170"+str(i)
    else:
        date="2017"+str(i)

    for dates in dates_Significance:
        if date in str(dates):
            count=count+1
            
    
    transactions.append(months[i-1]+","+ str(round_number((count*100)/len(dates_Significance)))+"%")


    

    




print("Exchange with most transactions: "+exchange_max(exchanges))
print ("Company with the highest combined valueEUR in August 2017: "+companies[valueEUR.index(max(valueEUR))])
print("Percentage of transactions with tradeSignificance=3 per month:")
for element in transactions:
    print(element)
        




