###Password generation 
import string as s
import random 
from csv import writer



def passgen():
    s1=s.ascii_lowercase
    #s1=s1.split()
   # print(s1)
    s2=s.ascii_uppercase
    #print(s2)
    s3=s.digits
    #print(s3)
    s4=s.printable
    #print(s4)
    s5=s.punctuation
    #print(s5)
    ##s6=s.whitespace
    ##print(s6)
    c=[]
    c.extend(list(s4))
    del c[-6:]
    #print(c)
    random.shuffle(c)
    #print("shuffled list : \n",c)
    platform=input("enter the website which is used by the password : ")
    pass_length=int(input("the length of the password is : "))
    #print("\n")
    print("the obtained password is  : ")
    password =("".join(c[0:pass_length]))
    ##storing(site,password) the the obtained password and it is used in the website in a csv file and by using file handling
    pass_data=[platform,password]
    ##appending the platform and the password in the csv file 
    with open('pass.csv','a') as f:
        writedata = writer(f)
        writedata.writerow(pass_data)
    print(password)


passgen()
