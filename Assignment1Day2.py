#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Q1
L = [11,12,13,14]
#(i)
L.extend([50,60])
print("(i)",L)
#(ii)
L.remove(11)
L.remove(13)
print("(ii)",L)
#(iii)
L.sort()
print("(iii)",L)
#(iv)
L.sort(reverse = True)
print("(iv)",L)
#(v)
if (13 in L) == True:
    print("Found")
else:
    print('(v)','Not Found')
#(vi)
numberofelemetsinL=len(L)
print('(vi)',numberofelemetsinL)
#(vii)
sumofelements=sum(L)
print('(vii)',sumofelements)
#(viii)
evens = [i for i in L if i%2==0]
print("(viii)",sum(evens))
#(ix)
odds = [i for i in L if i%2!=0]
print("(ix)",sum(odds))
#(x)
import math
prime_sum = 0
for i in L:
    flag = 1  
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = 0
            break
    if flag:
        prime_sum += i

print('(x)',prime_sum)
#(xi)
L.clear()
print('(xi)',L)
#(xii)
del(L)
#print(L) gives error   


# In[52]:


#Q2
D = {1:5.6,2:7.8,3:6.6,4:8.7,5:7.7}
#i
D[8] = 8.8
print('(i)',D)
#ii
del(D[2])
print('(ii)',D)
#iii
if 6 in D.keys():
    print("(iii) found")
else: 
    print("(iii) not found")
#iv
numofelements = len(D)
print("(iv)",numofelements)
#v
sumofvalues = sum(D.values())
print("(v)",sumofvalues)
#vi
D[3] = 7.1
print("(vi)", D)
#vii
D.clear()
print("(vii)", D)


# In[68]:


#Q3
S1 = {10,20,30,40,50,60}
S2 = {40,50,60,70,80,90}
#i
S1.add(55)
S1.add(66)
print("(i)",S1)
#ii
S1.remove(10)
S1.remove(30)
print("(ii)",S1)
#iii
if 40 in S1:
    print("(iii)","Found")
else: 
    print("(iii)","Not Found")
#iv
Sunion=S1.union(S2)
print("(iv)",Sunion)
#v
Sintersection=S1.intersection(S2)
print("(v)",Sintersection)
#vi
Sdiff=S1-S2
print("(vi)",Sdiff)


# In[9]:


#Q4 (i)
import string as s
import random

def rangeof():
    return random.randint(6, 9)

for i in range(100):
    new = s.ascii_letters
    randomstring = ''.join(random.choices(new, k=rangeof()))
    print(randomstring)


# In[13]:


#Q4 (ii)
import math
for i in range(600, 801):
    flag = 1
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = 0
            break
    if flag:
        print(i)


# In[14]:


#Q4(iii)
for i in range(100,1000):
    if i%7==0 and i%9==0:
        print('divisible by both 100 and 1000',i)


# In[30]:


#Q5
import random as r
L1 = []
L2 = []
for i in range(10):
    L1.append(r.randint(10,31))
    L2.append(r.randint(10,31))
print("List 1: ",L1)
print("List 2: ",L2)
#(i)
CommonNumbers = []
for i in L1:
    if i not in L2:
        continue 
    else:
        if i not in CommonNumbers:
            CommonNumbers.append(i) 
print("(i)")
print(CommonNumbers)
#(ii)
print("(ii)")
Unique1 = []
for i in L1:
    if i not in Unique1:
         Unique1.append(i)   
print(Unique1)
Unique2 = []
for i in L2:
    if i not in Unique2:
         Unique2.append(i)   
print(Unique2)
#(iii)
print("(iii)")
print("Minimum of L1",min(L1))
print("Minimum of L2",min(L2))
#(iv)
print("(iv)")
print("Maximum of L1",max(L1))
print("Maximum of L2",max(L2))
#(v)
SumofLists = [ a+b for a,b in zip(L1,L2)]
print("(v)")
print(SumofLists)


# In[43]:


#Q6
L = []
for i in range(100):
    L.append(r.randint(100,901))
print("List: ",L)
#(i)
Odds =[]
for i in L:
    if i%2!=0:
        if i not in Odds:
            Odds.append(i)
print("(i)",Odds)      
#(ii)
Evens =[]
for i in L:
    if i%2==0:
        if i not in Evens:
            Evens.append(i)
print("(ii)",Evens)  
#(iii)
import math
Primes = []
for i in L:
    flag = 1
    for j in range(2,int(math.sqrt(i))+1):
        if i%j==0:
            flag = 0
    if flag:
        if i not in Primes:
            Primes.append(i)
print("(iii)",Primes)


# In[53]:


#Q7
D = {1:"One",2:"Two",3:"Three",4:"Four",5:"Five"}
file = open("Ques7.txt","w")
for key, value in D.items():
    file.writelines(f"{key}, {value}\n")
file.close()
with open("Ques7.txt",'r') as file:
    for i in range(5):
        print(file.readline())


# In[57]:


#Q8
L=["One","Two","Three","Four","Five"]
file = open("Ques8.txt","w")
for i in range(5):
    count = len(L[i])
    row = L[i] + "," + str(count) + '\n'
    file.write(row)
file.close()
with open("Ques8.txt","r") as file:
    for i in range(4):
        print(file.readline())
    


# In[67]:


#Q9
import random as r
import string as s 
def rangeof():
    return r.randint(10, 15)
with open("Ques9.txt","w") as file:
    for i in range(100):
        strings = s.ascii_letters
        randoms = ''.join(r.choices(strings,k=rangeof())) + '\n'
        file.write(randoms)
with open("Ques9.txt","r") as file:
    for i in range(100):
        print(file.readline())


# In[77]:


#Q10
file = open("Ques10.txt","w+")
import math
for i in range(600, 801):
    flag = 1
    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = 0
            break
    if flag:
        file.write(str(i)+'\n')
file.seek(0)
print(file.read())


# In[79]:


#Q11
import time
start = time.time()
for i in range(35):
    print("Hello World")
 
time.sleep(1)
end = time.time() 
print(f"Total runtime of the program is {end - start}")


# In[ ]:





# In[91]:


#Q13
D = {"Ani": 96, "Auchi": 94, "Kunal": 93, "Kartik": 96, "Maria": 89}
Values = list(D.values())
MaxMarks = max(Values)
MinMarks = min(Values)
AvgMarks = sum(Values) / len(Values)
print(list(D.items()))

for item in list(D.items()):
    name, value = item  
    if MaxMarks == value:
        print("Maximum marks:", name)
    if MinMarks == value:
        print("Minimum marks:", name)
    if AvgMarks == value:
        print("Average marks:",name)


# In[ ]:




