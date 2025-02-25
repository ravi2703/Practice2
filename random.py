import random
letters = ['a', 'b' 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
symbols = ['!', '@', '$', '*', '#', '%', '^', '~', '(', ')', '{', '}', '?']

nr_letters = int(input("how many letters do you want in password\n"))
nr_numbers = int(input(f"how many numbers do you want in password\n"))
nr_symbols = int(input(f"how many symbols do you want in password\n"))

password =" "
for char in range(0, nr_letters + 1):
      password += random.choice(letters)
      for char in range(1, nr_symbols + 1):
            password += random.choice(symbols)
            for char in range(1, nr_numbers + 1):
                  password += random.choice(numbers)
                  random.shuffle(letters)
                  random.shuffle(symbols)
                  random.shuffle(numbers)
                  print(password)'''

                  '''from array import *
                  my_array = [1,2,3,4,5]
                  my_array.append(6)
                  for i in my_array:
                       print(i)


                       my_array = array('i', [1,2,3,4,5])
                       c = my_array.tolist()
                       # [1, 2, 3, 4, 5]

                       lst=[[1,2,3],[4,5,6],[7,8,9]]
                       print(lst[0])
                       print(lst[1])

                       mydict = {}
                       print(mydict)
                       # {}
                       print(mydict.get("foo", "bar"))
                       # bar
                       print(mydict)
                       # {}
                       print(mydict.setdefault("foo", "bar"))
                       # bar
                       print(mydict)

                       from collections import ChainMap
                       fish = {'swin': "jelly", 'water': "blue"}
                       dog = {'bark': 'bow', 'breath': 'five'}

                       print(dict(ChainMap(fish, dog)))'''

                       mydict = {
                         'a': '1',
                           'b': '2'
                           }
                           a = (mydict.keys())
                           print(a)

                           dictionary = {'hello': 1234, 'world': 3456}
                           print(dictionary['hello'])
                           print(dictionary['world'])

                           from collections import OrderedDict
                           d = OrderedDict()
                           d['first'] = 1
                           d['second'] = 2
                           d['third'] = 3
                           for key in d:
                             print(key, d[key])
                             file = open('linux.py', 'r')
                             print(file.read())
                               
                               import psutil
                               cpu_usage = psutil.boot_time()
                               percentage = psutil.cpu_times_percent()
                               print(cpu_usage)
                               print(percentage)
