# multiplication table
num = int(input("Enter the  multiplication table:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)

#when else block will execute
number = int(input("Type any number: "))
flag = number % 2
if flag ==0:
    print("Given number is EVEN: ", number)
elif flag ==1:
    print("Given number is ODD: ", number)
else:
    print("Please enter valid int only")

#3.current date and time
import datetime
now = datetime.datetime.now()
print("Current date and time :")
print(now.strftime("%Y-%m-%d  %H:%M :%S"))

#3.2  after 4 days date from the current date
from datetime import datetime,timedelta
current_date = datetime.now().date()
future_date =current_date + timedelta(days=4)
print("Current date :",current_date)
print("Date 4 days from now :",future_date)

# before 4 days  date from the current date
from datetime import datetime,timedelta
current_date = datetime.now().date()
past_date =current_date - timedelta(days=4)
print("Current date :",current_date)
print("Date 4 days from now :",past_date)

# print Random mobile number
import random
def generate_random_mobile_number():
    return ''.join(random.choices('0123456789',k=10))
print("Random mobile number:",generate_random_mobile_number())

#print random email id's
import random
import string

def generate_random_email():
    domains = ["gmail.com", "yahoo.com", "hotmail.com", "example.com"]
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(5, 10)))
    domain = random.choice(domains)
    return f"{username}@{domain}"

# Generate and print 10 random email-like strings
for _ in range(10):
    print(generate_random_email())