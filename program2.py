#We have to find the Loyal customers

# Those customers who :
# 1) Visited both the days
# 2) must visit different page each days

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


# process -

# step -1 Make a dictionary and store the customers as keys and value as an array of pages visited on day 1

day1_record = {}
for i in range(len(cus1)):
    if (day1_record.get(cus1[i]) is None):
        day1_record[cus1[i]] = [[pag1[i]],[]]
    else:
        day1_record[cus1[i]][0].append(pag1[i])


print(len(day1_record))  # total 4306 customers visited on day 1

# Now we will search only for those customers in day2 log file who are present in day1_record. If they are present
# then we will insert the pages in 1st index of 2 dimension array.

# If a customer has visited website both days then it can be demonstated as

'''
    {
      customer_with_some_id : [[pages_visited_on_day_1],[pages_visited_on_day_2]]
    }
'''

for i in range(len(cus2)):
    if day1_record.get(cus2[i]) is not None:
        day1_record[cus2[i]][1].append(pag2[i])


# now we will compare the elements of arr[0] and arr[1] which are the value of keys of day1_record
common_record = {}
for customers in day1_record:
    if len(day1_record[customers][1]) != 0:
        common_record[customers] = day1_record[customers]

# common_recored will contain all those customers who are visited website both the days.



print(len(common_record)) # 3817 customers visited both days

# Now to find the loyal customers we need to follow this

# 1) if length of both the unique of arrays is 1 and each element in arrays is same then the customer is not loyal
# 2) if unique of any array is greater than 1 then the customer is loyal
# 

loyal_customers = []

for key in common_record:
    if len(set(common_record[key][0])) == 1 and len(set(common_record[key][1])) == 1 and common_record[key][0][0] != common_record[key][1][0]:
        loyal_customers.append(common_record[key])
    if len(set(common_record[key][0]))!= len(set(common_record[key][1])):
        loyal_customers.append(common_record[key])


print(len(loyal_customers))   #loyal customers 

