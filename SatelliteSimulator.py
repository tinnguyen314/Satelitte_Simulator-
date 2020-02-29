# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 13:40:00 2019

@author: TN
"""

import time
import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(0)
class package:
    def __init__(self):
        self.type = [1,2,3,4]
        self.price = [210, 350, 400, 500]
        self.time = [1, 3, 5, 10]
        
class Satellite_Simulator:
    def __init__(self):
        self.country = ["USA", "China", "Germany", "Japan", "Switzerland"]
        self.inTransmission = [0,0,0,0,0]
        self.temp1 = 0
        self.temp2 = 0
        self.country_select = -1    #country code for each country
        self.package_queue = []     #queue for package type 
        self.country_queue = []     #queue for country   
        self.package = package()    #create a package object
        self.tempCountryQueue =[]
        self.tempPackageQueue =[]
        
     
    # This method is to view the list of country in queue 
    # and list of packages which are requested by each country
    def view(self):
        for x in range (len(self.country_queue)):
            y = self.country[self.country_queue[x]]
            z = self.package.type[self.package_queue[x]]
            p = self.package.price[self.package_queue[x]]
            print("%12s requesting package type %3d cost %5d dollar"%(y,z,p))
        print("\n\n")
    # Create a country queue + package queue and add to 2 lists with the same order
    def push(self):
        packageHours = 0
        while packageHours <= 120:
            self.country_select = random.randrange(0,5,1)
            self.country_queue.append(self.country_select)
            package = random.randrange(0,4)
            self.package_queue.append(package)
            packageHours = self.package.time[package] + packageHours
    # Remove the first elevement of country queue + package queue that going to the channel
    def pop(self):
        self.country_queue.pop(0)
        self.package_queue.pop(0)
        
    # country select = position of the inTranmission list
    def mark_as_intransmission(self, country_select, n):
        #pos= self.country.index(country)
        self.inTransmission[country_select]=n

class channel:
    def __init__(self,name):
        self.name = name
        self.isActivated = False
        self.countdown = 0
        self.countryList = []
        self.packageList = []
        self.money = 0
        self.currentcountry = 0
    def count_down(self):
        if self.countdown <= 0:
            self.isActivated = False
        else:
            self.isActivated = True
            self.countdown = self.countdown - 1
        
S = Satellite_Simulator()
P = package()
S.push()
S.view()
a = channel("Channel A")
b = channel("channel B")
ChannelA = []
ChannelB = []
ChannelAC = []
ChannelBC = []
totalrun = []
for i in range (0,48):
    if (a.countdown == 0): 
        if S.inTransmission[S.country_queue[0]] == 1:
            S.tempCountryQueue.append(S.country_queue[0])
            S.tempPackageQueue.append(S.package_queue[0])
            S.pop()
        if len(S.tempCountryQueue) > 0 and S.inTransmission[S.tempCountryQueue[0]] == 0:
            PackageHr1 = P.time[S.tempPackageQueue[0]]
            S.mark_as_intransmission(S.tempCountryQueue[0],1)
            if PackageHr1 > (48 - i):
                if ((48 - i) > 5 and (48 - i) < 10):
                    PackageHr1 = 5
                    S.tempPackageQueue[0] = 2
                elif ((48 - i) > 3 and (48 - i) < 5):
                    PackageHr1 = 3
                    S.tempPackageQueue[0] = 1
                else:
                    PackageHr1 = 1
                    S.tempPackageQueue[0] = 0
            a.countdown = PackageHr1
            a.currentcountry = S.tempCountryQueue[0]
            a.countryList.append(S.tempCountryQueue[0])
            a.packageList.append(S.tempPackageQueue[0])
            S.tempCountryQueue.pop(0)
            S.tempPackageQueue.pop(0)
        else:   
            PackageHr1 = P.time[S.package_queue[0]]
            S.mark_as_intransmission(S.country_queue[0],1)
            if PackageHr1 > (48 - i):
                if ((48 - i) > 5 and (48 - i) < 10):
                    PackageHr1 = 5
                    S.package_queue[0] = 2
                elif ((48 - i) > 3 and (48 - i) < 5):
                    PackageHr1 = 3
                    S.package_queue[0] = 1
                else:
                    PackageHr1 = 1 
                    S.package_queue[0] = 0
            a.countdown = PackageHr1
            S.temp1 = S.country_queue[0]
            a.currentcountry = S.country_queue[0]
            a.countryList.append(S.country_queue[0])
            a.packageList.append(S.package_queue[0])
            S.pop()
            #S.view()
    if (b.countdown == 0):
        if S.inTransmission[S.country_queue[0]] == 1:
            S.tempCountryQueue.append(S.country_queue[0])
            S.tempPackageQueue.append(S.package_queue[0])
            S.pop()
        if len(S.tempCountryQueue) > 0 and S.inTransmission[S.tempCountryQueue[0]] == 0:
            PackageHr2 = P.time[S.tempPackageQueue[0]]
            S.mark_as_intransmission(S.tempCountryQueue[0],1)
            if PackageHr2 > (48 - i):
                if ((48 - i) > 5 and (48 - i) < 10):
                    PackageHr2 = 5
                    S.tempPackageQueue[0] = 2
                    
                if ((48 - i) > 3 and (48 - i) < 5):
                    PackageHr2 = 3
                    S.tempPackageQueue[0] = 1
                else:
                    PackageHr2 = 1
                    S.tempPackageQueue[0] = 0
            b.countdown = PackageHr2
            b.currentcountry = S.tempCountryQueue[0]
            b.countryList.append(S.tempCountryQueue[0])
            b.packageList.append(S.tempPackageQueue[0])
            S.tempCountryQueue.pop(0)
            S.tempPackageQueue.pop(0)
        else:
            PackageHr2 = P.time[S.package_queue[0]]
            S.mark_as_intransmission(S.country_queue[0],1)
            if PackageHr2 > (48 - i):
                if ((48 - i) > 5 and (48 - i) < 10):
                    PackageHr2 = 5
                    S.package_queue[0] = 2
                elif ((48 - i) > 3 and (48 - i) < 5):
                    PackageHr2 = 3
                    S.package_queue[0] = 1
                else:
                    PackageHr2 = 1
                    S.package_queue[0] = 0
            b.countdown = PackageHr2 
            b.currentcountry = S.country_queue[0]
            S.temp2 = S.country_queue[0]
            b.countryList.append(S.country_queue[0])
            b.packageList.append(S.package_queue[0])
            S.pop()
            #S.view()
    
    a.count_down()
    b.count_down()
    if a.countdown < 1:
        S.mark_as_intransmission(S.temp1,0)
        
    if b.countdown < 1:
        S.mark_as_intransmission(S.temp2,0)
    a_country = a.currentcountry + 1
    b_country = b.currentcountry + 1
    ChannelA.append(a_country)
    ChannelB.append(b_country)
    ChannelAC.append(S.country[a_country-1])
    ChannelBC.append(S.country[b_country-1])
totalrun = ChannelA + ChannelB
"""
print("This is country go on channel A for 48 hours:")
print(*ChannelA)
print("This is country go on channel B for 48 hours:")
print(*ChannelB)
"""
def count(list_use,n):
    count = 0
    for i in range(len(list_use)):
        if n == list_use[i]:
            count = count + 1
    return count
x = np.arange(0,48,1)
#for i in range (0,48):
#    x.append(i)
total_money = 0
total_package = a.packageList + b.packageList
#print(*total_package)
for i in range (len(total_package)):
    total_money = total_money + P.price[total_package[i]] 

print("This is how many hours USA use: " + str(count(totalrun,1)))
print("This is how many hours China use: " + str(count(totalrun,2)))
print("This is how many hours Germany use: " + str(count(totalrun,3)))
print("This is how many hours Japan use: " + str(count(totalrun,4)))
print("This is how many hours Switzerland use: " + str(count(totalrun,5)))
#print(total_money)
plt.step(x,ChannelA,'r', label='Channel A')
plt.step(x,ChannelB,'B', label = 'Channel B')
title = "Channel A and B country usage for 48 hours"
plt.title (title)
plt.xlabel('Total hours (48 hr)')
plt.ylabel('Countries 1-USA 2-China 3-Germany 4-Japan 5-Switzerland')
plt.legend()
plt.show()
plt.hist(totalrun,5,color="red",range = (0,6),rwidth=0.95)
plt.xlabel("Country usage: 1-USA 2-China 3-Germany 4-Japan 5-Switzerland")
plt.ylabel("Number of hours")
plt.text(0, 25, 'Total income of 2 channels: {:d}$'.format(total_money))
plt.title("Country usage in 2 channels")
plt.show()

#print(*S.inTransmission)
#print(*a.countryList)
#print(*a.packageList)
#print("\n\n")
#print(*b.countryList)
#print(*b.packageList)

           
        
        
    
    
    
    
    
 

    

 

    



        