{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## hello world in python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "hello world\n"
     ]
    }
   ],
   "source": [
    "print(\"hello world\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## string operations in python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['compare', 'Python', 'with', 'Java']\n"
     ]
    }
   ],
   "source": [
    "a = \"compare Python with Java\"\n",
    "print( a.split())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## control flow in python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "=10\n"
     ]
    }
   ],
   "source": [
    "condition =10\n",
    "#if\n",
    "if condition > 10:\n",
    "    print(\">10\")\n",
    "elif condition == 10:\n",
    "    print(\"=10\")\n",
    "else:\n",
    "    print(\"<10\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10\n",
      "9\n",
      "8\n",
      "7\n",
      "6\n",
      "5\n",
      "4\n",
      "3\n",
      "2\n"
     ]
    }
   ],
   "source": [
    "#while\n",
    "while condition >1:\n",
    "    print(condition)\n",
    "    condition = condition-1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "1\n"
     ]
    }
   ],
   "source": [
    "#switch\n",
    "def f(x):\n",
    "    return{\n",
    "        1:1,\n",
    "        2:2,\n",
    "    }[x]\n",
    "print(f(condition))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "123456789"
     ]
    }
   ],
   "source": [
    "#for\n",
    "for x in range(1,10):\n",
    "    print(x,end=\"\")"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## class&inheritance in python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "I am Chiwawa,and I can bark\n"
     ]
    }
   ],
   "source": [
    "class Animal():\n",
    "    \n",
    "    def __init__(self, name):#__init__\n",
    "        self.name = name\n",
    "    def saySomething(self):\n",
    "        print(\"I am\" + self.name)\n",
    "class dog(Animal):\n",
    "    def saySomething(self):\n",
    "        print(\"I am \"+ self.name+\",and I can bark\")\n",
    "\n",
    "dog = dog(\"Chiwawa\")\n",
    "dog.saySomething()       "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## file I/O in python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "myFile = open(\"poem.txt\",\"w\")\n",
    "myFile.write(\"hello world\")\n",
    "myFile.close()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## collection in python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['a', 'b', 'c']\n"
     ]
    }
   ],
   "source": [
    "alist =[]\n",
    "alist.append(\"a\")\n",
    "alist.append(\"b\")\n",
    "alist.append(\"c\")\n",
    "print(alist)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## numbers in python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# integer numbers\n",
    "num = 100\n",
    "num = int('100')\n",
    "\n",
    "#floating point numbers\n",
    "f = 1.01\n",
    "f = float(\"1.01\")\n",
    "\n",
    "#null\n",
    "special = None"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'int'>\n",
      "<class 'float'>\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(type(num))\n",
    "print(type(f))\n",
    "print(special)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## tuples in python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "aTuple =()\n",
    "aTuple =(5)#cause error\n",
    "aTuple =(5,)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "(5,)\n",
      "5\n"
     ]
    }
   ],
   "source": [
    "print(aTuple)\n",
    "print(aTuple[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## sets in python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "two\n",
      "three\n",
      "one\n"
     ]
    }
   ],
   "source": [
    "aSet = set()\n",
    "aSet = set(\"one\")#a包含三個字母\n",
    "aSet = set(['one','two','three'])\n",
    "\n",
    "#iterate over set\n",
    "for v in aSet:\n",
    "    print(v)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "cSet: {'three', 'five', 'four', 'two', 'one'}\n",
      "dSet: {'three'}\n",
      "eSet: {'two', 'one'}\n",
      "bSet: {'three', 'five', 'four', 'six'}\n"
     ]
    }
   ],
   "source": [
    "bSet = set(['three','four','five'])\n",
    "\n",
    "#union\n",
    "cSet = aSet | bSet\n",
    "print('cSet:',cSet)\n",
    "\n",
    "#intersection\n",
    "dSet = aSet & bSet\n",
    "print('dSet:',dSet)\n",
    "\n",
    "#find elements in aSet not in bSet\n",
    "eSet = aSet.difference(bSet)\n",
    "print('eSet:',eSet)\n",
    "\n",
    "#add element\n",
    "bSet.add(\"six\")\n",
    "print('bSet:',bSet)\n",
    "\n",
    "## dictionaries in Python:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mike 555-1111\n",
      "Lucy 555-2222\n",
      "Jack 555-3333\n"
     ]
    }
   ],
   "source": [
    "#create an empty dictionary\n",
    "phonebook = ()\n",
    "phonebook = {\"Mike\":\"555-1111\",\n",
    "            \"Lucy\":\"555-2222\",\n",
    "            \"Jack\":\"555-3333\"}\n",
    "phonebook\n",
    "\n",
    "#iterate over dic\n",
    "for key in phonebook:\n",
    "    print(key,phonebook[key])\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#add an element\n",
    "phonebook[\"Mary\"]='555-6666'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "#delete an element\n",
    "del phonebook[\"Mike\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "3\n"
     ]
    }
   ],
   "source": [
    "#get number of elements\n",
    "count = len(phonebook)\n",
    "print(count)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "dict_keys(['Lucy', 'Jack', 'Mary', 'Susan'])\n"
     ]
    }
   ],
   "source": [
    "#can have different typess\n",
    "phonebook['Susan'] = (1,2,3,4)\n",
    "\n",
    "#return all keys\n",
    "print(phonebook.keys())\n",
    "#delete all the elements\n",
    "phonebook.clear()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
