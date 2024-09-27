# step:1  Read the file

logFile1 = open('./Day1.log','r')
logFlie2 = open('./Day2.log','r')

cus1 = []
pag1 = []
for log in logFile1:
    cus1.append(log.split(' ')[2])
    pag1.append(log.split(' ')[3])

cus2 = []
pag2 = []
for log in logFlie2:
    cus2.append(log.split(' ')[2])
    pag2.append(log.split(' ')[3])


# Now we will find how many customerIds are common in both da1 and day2 and we will insert them into another arra common_customers

day1_record = {}
day2_record = {}
for i in range(len(cus1)):
    if(day1_record.get(cus1[i]) is None):
        day1_record[cus1[i]] = [pag1[i]]
    else:
        day1_record[cus1[i]].append(pag1[i])

for i in range(len(cus2)):
    if(day2_record.get(cus2[i]) is None):
        day2_record[cus2[i]] = [pag2[i]]
    else:
        day2_record[cus2[i]].append(pag2[i])



# now we will traverse in cus1 

# Now we will traverse in day1_record and find which keys have a unique array whose lenght is atleast 2.
day1_loyal_customers = []
day2_loyal_customers = []
for key in day1_record:
    if(len(set(day1_record[key])) >= 2):
        day1_loyal_customers.append(key)
for key in day2_record:
    if(len(set(day2_record[key])) >= 2):
        day2_loyal_customers.append(key)

# print(day1_loyal_customers) #contains unique customers who visited atleast 2 unique pages in day 1
# print(day2_loyal_customers) #contains unique customers who visited atleast 2 unique pages in day 2

# we have got loyal customers for each day. Now only those customers will be termed as loyal who are common in both days
loyal_customers = [] #those customers who visited atleast 2 unique pages for both days  : Required result
for i in range(len(day1_loyal_customers)):
    for j in range(i+1,len(day2_loyal_customers)):
        if(day1_loyal_customers[i] == day2_loyal_customers[j]):
             loyal_customers.append(day1_loyal_customers[i])
             break
        
# print(loyal_customers)

print("\t\t stats")

print("Total customers in the DB of the website : ", 5000)
print("Total unique on the website : ", 1000)
print("Total numeber of customers who visited the website on day 1 : ", len(day1_record))
print("Total numeber of customers who visited the website on day 2 : ", len(day2_record))
print("Total numeber of customers who visited atleast 2 unique pages of the website on day 1 : ", len(day1_loyal_customers))
print("Total numeber of customers who visited atleast 2 unique pages of the website on day 2 : ", len(day2_loyal_customers))
print("Loyal Customers (Those customers who visited at least 2 unique pages of the website on both days) : ", len(loyal_customers))




