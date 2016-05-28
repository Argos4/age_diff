
import os

def find_Agedifference():
    elder=''
    younger=''
    try:
        name1=raw_input("Enter name of person 1")
        age1=raw_input("Enter age of "+name1+" in DD-Mon-YYYY format")
        name2=raw_input("Enter name of person 2")
        age2 = raw_input("Enter age of " + name2 + " in DD-Mon-YYYY format")
    except ValueError:
        print "Please enter valid input to program"
        os._exit(1)

    age1 = age1.split('-')
    age2 = age2.split('-')


    if (int(age1[2]) > int(age2[2])):
        yr_diff = int(age1[2]) - int(age2[2])
        elder=name2
        younger=name1

    elif (int(age2[2]) > int(age1[2])):
        yr_diff = int(age2[2]) - int(age1[2])
        elder=name1
        younger=name2
    else:
        yr_diff=0


    lmonth=[{'Jan':31},{'Feb':28},{'Mar':31},{'Apr':30},{'May':31},{'Jun':30},{'Jul':31},{'Aug':31},{'Sep':31},{'Oct':31},{'Nov':30},{'Dec':31}]

    tot_days1=0
    breaker=False
    for data in lmonth:
        print data
        for i in data:
            if str(i) != age1[1]:
                print age1[1]
                tot_days1=tot_days1+int(data[i])
            else:
                breaker = True
                break

        if breaker:
            print breaker
            break

    tot_days1=tot_days1+int(age1[0])
    print tot_days1

    tot_days2 = 0
    breaker = False
    for data in lmonth:
        print data
        for i in data:
            if str(i) != age2[1]:
                tot_days2 = tot_days2 + int(data[i])
            else:
                breaker = True
                break

        if breaker:
            print breaker
            break

    tot_days2 = tot_days2 + int(age2[0])
    print tot_days2
    daydiff=0
    if tot_days1 > tot_days2:
        daydiff=tot_days1-tot_days2
    elif tot_days2 > tot_days1:
        daydiff=tot_days2-tot_days1


    print "Total differenc is "+ str(daydiff) +" days "+str(yr_diff)+"years"

    if elder==name1:
        print name1 + " is older than "+ name2 +" by "+ str(daydiff) +" days "+str(yr_diff)+" years"
    elif elder==name2:
        print name2 + " is older than " + name1 + " by " + str(daydiff) + " days " + str(yr_diff) + " years"
    elif yr_diff==0:
        if tot_days1 > tot_days2:
            print name2 + " is older than " + name1 + " by " + str(daydiff) + " days " + str(yr_diff) + " years"
        elif tot_days2 > tot_days1:
            print name1 + " is older than " + name2 + " by " + str(daydiff) + " days " + str(yr_diff) + " years"

find_Agedifference()



