import datetime
import random
#list of possible customer_ids (random) -> 5000
#list of pages - Let's say we have 10 pages -> 1000
customer_ids = []
page_ids = []

for i in range(1,5001):
    customer_ids.append('customer' + str(i))
for i in range(1,1001):
    page_ids.append('page' + str(i))



#From the above lines, We have list of all customers and pages.


#function to generate a log



def generate_log_files(file_name, record):
    file = open(file_name,'w')
    for i in range(record):
        file.write(f"{file_name.split('.')[0]} {(datetime.datetime.now() + datetime.timedelta(minutes=random.randint(1,59))).strftime('%H:%M:%S')} {random.choice(customer_ids)} {random.choice(page_ids)} \n")


generate_log_files('Day1.log',10000)
generate_log_files('Day2.log',11000)




