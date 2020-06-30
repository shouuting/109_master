
# coding: utf-8

# ## hello world in python:

# In[31]:

print("hello world")


# ## string operations in python:

# In[32]:

a = "compare Python with Java"
print( a.split())


# ## control flow in python:

# In[5]:

condition =10
#if
if condition > 10:
    print(">10")
elif condition == 10:
    print("=10")
else:
    print("<10")
    


# In[6]:

#while
while condition >1:
    print(condition)
    condition = condition-1


# In[12]:

#switch
def f(x):
    return{
        1:1,
        2:2,
    }[x]
print(f(condition))


# In[51]:

#for
for x in range(1,10):
    print(x,end="")


# ## class&inheritance in python:

# In[24]:

class Animal():
    
    def __init__(self, name):#__init__
        self.name = name
    def saySomething(self):
        print("I am" + self.name)
class dog(Animal):
    def saySomething(self):
        print("I am "+ self.name+",and I can bark")

dog = dog("Chiwawa")
dog.saySomething()       


# ## file I/O in python:

# In[22]:

myFile = open("poem.txt","w")
myFile.write("hello world")
myFile.close()


# ## collection in python:

# In[39]:

alist =[]
alist.append("a")
alist.append("b")
alist.append("c")
print(alist)


# ## numbers in python:

# In[40]:

# integer numbers
num = 100
num = int('100')

#floating point numbers
f = 1.01
f = float("1.01")

#null
special = None


# In[50]:

print(type(num))
print(type(f))
print(special)


# ## tuples in python:

# In[52]:

aTuple =()
aTuple =(5)#cause error
aTuple =(5,)


# In[54]:

print(aTuple)
print(aTuple[0])


# ## sets in python:

# In[4]:

aSet = set()
aSet = set("one")#a包含三個字母
aSet = set(['one','two','three'])

#iterate over set
for v in aSet:
    print(v)


# In[12]:

bSet = set(['three','four','five'])

#union
cSet = aSet | bSet
print('cSet:',cSet)

#intersection
dSet = aSet & bSet
print('dSet:',dSet)

#find elements in aSet not in bSet
eSet = aSet.difference(bSet)
print('eSet:',eSet)

#add element
bSet.add("six")
print('bSet:',bSet)

## dictionaries in Python:


# In[22]:

#create an empty dictionary
phonebook = ()
phonebook = {"Mike":"555-1111",
            "Lucy":"555-2222",
            "Jack":"555-3333"}
phonebook

#iterate over dic
for key in phonebook:
    print(key,phonebook[key])
    


# In[23]:

#add an element
phonebook["Mary"]='555-6666'


# In[24]:

#delete an element
del phonebook["Mike"]


# In[27]:

#get number of elements
count = len(phonebook)
print(count)


# In[30]:

#can have different typess
phonebook['Susan'] = (1,2,3,4)

#return all keys
print(phonebook.keys())
#delete all the elements
phonebook.clear()


# In[ ]:



