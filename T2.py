string1 = "Monty Python's Flying Circus"
string2 = 'I like the "Dead Parrot" sketch'
string3 = '''When Cleese says: 
  "Now that's what I call a dead parrot" '''

test = 1 == 1 and 1 > 2
print(test) # false 更多例子 比如or。

x = 1
print(type(x))          # <class 'int'>
xstr = '1'
print(type(xstr))       # <class 'str'>
test = x == xstr        # --> False
print(test)
print(type(test))       # <class 'bool'>

# Try it!
'3' * 2   # --> '33'


x = str.lower('ABC')
print(x)            # --> 'abc' 也可以反过来 upper和lower
y = 'abc'.upper()
print(y)            # --> 'ABC'

weird_case = "My fUnNy tYpEcAsE sTrInG"

# First convert the string to uppercase:
weird_case_upper = weird_case.upper()       # --> "MY FUNNY TYPECASE STRING"
# Then, convert the uppercase version to lowercase
weird_case_lower = weird_case_upper.lower() # --> "my funny typecase string"


weird_case = "My fUnNy tYpEcAsE sTrInG"
# Convert the string to upper case and then to lower case
weird_case_lower = weird_case.upper().lower() # --> "my funny typecase string"

weird_case = "My fUnNy tYpEcAsE sTrInG"
weird_case_fn = weird_case.lower        # --> <built-in method lower of str object at xxxx>
print(weird_case_fn()) # --> "my funny typecase string"

"Hi".center(40)  # --> '                   Hi                   '
"Hi".center(40, '-') # --> '-------------------Hi------------------ -'

a = True  # f的用法
b = 5
print(f"The value of a is {a} and the value of b is {b}") # --> The value of a is True and the value of b is 5

a = True
b = 5
print("The value of a is {} and the value of b is {}".format(a , b)) # --> The value of a is True and the value of b is 5

#2.7 Lists(有序，可变，可重复), Tuples(有序，不可变，可重复), Sets(无序，可变，不可重复), Dictionaries(无序，可变，不可重复)

lst = [1, 2, 3]
print(lst) # [1, 2, 3]
t = type(lst) # --> <class 'list'>
print(t)

lst = [1, "string", True, None]
print(type(lst)) # --> <class 'list'>
# a list is not a primitive type because it is not a string, int, float, or bool.

lst_a = [1, "string", True, None]
lst_b = ["a" , lst_a]
print(lst_b) # ['a', [1, 'string', True, None]]

lst = [1, "string", True, None]
print(f"The item at index 0 is {lst[0]}") # The item at index 0 is 1
print(f"The item at index 1 is {lst[1]}") # The item at index 1 is string
print(f"The item at index 2 is {lst[2]}")
print(f"The item at index 3 is {lst[3]}")
lst = [1, "string", True, None]
print(f"The item at index -4 is {lst[-4]}") # The item at index 0 is 1
print(f"The item at index -3 is {lst[-3]}")
print(f"The item at index -2 is {lst[-2]}")
print(f"The item at index -1 is {lst[-1]}")

lst = ["a", "b", "c", "d", "e", "f"]
print(f"The slice from index 1 through 4 is {lst[1:4]}" ) # The slice from index 1 through 4 is ['b', 'c', 'd']
print(f"The slice from index -5 through -2 is {lst[-5:-2]}" ) # The slice from index -5 through -2 is ['b', 'c', 'd']
lst = ["a", "b", "c", "d", "e", "f"]
print(f"lst[:3] gives {lst[:3]}") # lst[:3] gives ['a', 'b', 'c']
print(f"lst[0:1000] gives {lst[0:1000]}") # lst[0:1000] gives ['a', 'b', 'c', 'd', 'e', 'f']

lst_a = [1]
lst_b = [2, 3]
lst_a.extend(lst_b) # --> lst_a now is [1, 2, 3]
print(lst_a)
lst_a.append(lst_b) # --> lst_a now is [1, [2, 3] ]
print(lst_a)

lst = [1, True, None]
print(f"lst is originally {lst}")
lst.insert(1, "string")       # lst is now [1, "string", True, None]
print(f"After insertion, lst is now {lst}")

lst = [1, "string", True, None, True]
print(f"Original lst is {lst}")
lst.remove(True)
print(f"lst after removing the first True is {lst}")  # 这块不是remove第一个True吗， 为什么去掉了第0位。Boolean里1是ture，0是false。
lst.pop(2)
print(f"lst after removing the element CURRENTLY at index 2 is {lst}")
lst.pop()
print(f"lst after removing the CURRENT last element is {lst}")

lst = [1, "string", True, None, True]
no_of_items =len(lst)
print(f"lst has {no_of_items} items")

t = ("word", 5, False) #和lst差不多

# Create a tuple with two elements
tup = (1, 2)
# unpack the tuple into two variables:
(a, b) = tup
# print
print(f"`a` is {a} and `b` is {b}")

a, b, c = 1, True, "word"
a, b, c = (1, True, "word")
(a, b, c) = 1, True, "word"
(a, b, c) = (1, True, "word")

a = ( 1 , True , "word" ) # a is (1, True, "word")
# Explicit parentheses does not force Python to co unt variables being unpacked
(a) = (1, True, "word") # a is (1, True, "word")

s = {1, 2, 3, 3, 3, 3} # --> {1, 2, 3}

empty_set = set()

s = set()
s.add("QAN.AX")   # s is {"QAN.AX"}
s.add("WES.AX")   # s is {"QAN.AX", "WES.AX"}
s.add("CBA.AX")   # s is {"QAN.AX", "WES.AX", "CBA.AX"}
s.add("CBA.AX")   # s is {"QAN.AX", "WES.AX", "CBA.AX"} (so no change)
print(f"After adding objects, s is {s}")
s.remove("CBA.AX") # s is {"QAN.AX", "WES.AX"}
print(f"After removing 'CBA.AX', s is {s}")

s = {1, 2, 3}
1 in s # --> True
4 in s # --> False
1 not in s # --> False
4 not in s # --> True
n_of_elements = len(s)
print(f"s contains {n_of_elements} objects")

prc_dic = {
  '2020-01-02': 7.1600,
  '2020-01-03': 7.1900,
  '2020-01-06': 7.0000,
  '2020-01-07': 7.1000,
  '2020-01-08': 6.8600,
  '2020-01-09': 6.9500,
  '2020-01-10': 7.0000,
  '2020-01-13': 7.0200,
  '2020-01-14': 7.1100,
  '2020-01-15': 7.0400,
  }
print(prc_dic)
# Ask for the value stored under '2020-01-02'
prc_dic['2020-01-02'] # --> 7.16
prc_dic[7.1600] # --> KeyError: 7.16
prc_dic['2020-01-16'] = 6.9200
print(f"prc_dic now has a value for 2020-01-16: {prc_dic}")

d = {}      # --> {}
d = dict()  # --> {}

dic = {'a':1 , 'b':1}
number_of_keys = len(dic)
print(f"dic has {number_of_keys} keys")  # dic has 2 keys

d = {"a": 1}
d["a"] = 2
print(f"After overwriting, d is now {d}" ) # After overwriting, d is now {'a': 2}

d_update_with_dict = {'a': 1, 'b': 2}
d_update_with_dict.update({'a': 2, 'c': 3 })
print(f"After update d_update_with_dict is {d_update_with_dict}") # After update d_update_with_dict is {'a': 2, 'b': 2, 'c': 3}
d_update_with_list = {'a': 1, 'b': 2 }
d_update_with_list.update([('a', 3), ('c', 5 )])
print(f"After update d_update_with_list is {d_update_with_list}") # After update d_update_with_list is {'a': 3, 'b': 2, 'c': 5}

d = {'a': 1, 'b': 2 }
d.pop('a')
print(f"After popping 'a', d is now {d}") # After popping 'a', d is now {'b': 2}

dic = {'a': 2, 'a': 2, 'a': 2, 'a': 1 , 'a' : 1}
print(dic) # {'a': 1}

# After Python 3.6, order of insertion is preserved
dic = {1: 'first', 2: 'second', 3: 'third'}
# This will insert the 0 key at the end
dic[0] = 'fourth'
# This will NOT insert the key at the end because 1 exists
dic[1] = 'new first'
# Also, this does not return the first element of the dic
# because it was inserted at the end
print(dic) # {1: 'new first', 2: 'second', 3: 'third', 0: 'fourth'}

lst1 = ['a']
print(f'This is lst1: {lst1}')
lst2 = ['b', lst1]
print(f'This is lst2: {lst2}') # This is lst2: ['b', ['a']]
lst2[1].append('c')
print(f"This is lst2 after modifying it: {lst2}") # This is lst2 after modifying it: ['b', ['a', 'c']]
print(f"This is lst1 after modifying lst2: {lst1}") # This is lst1 after modifying lst2: ['a', 'c']

lst1 = ['a']
print(f'This is lst1: {lst1}')
lst3 = ['b', ['a']]
print(f'This is lst3: {lst3}') # This is lst3: ['b', ['a']]
lst3[1].append('c')
print(f"This is lst3 after appending 'c': {lst3}") # This is lst3 after appending 'c': ['b', ['a', 'c']]
print(f"This is lst1 after modifying lst3: {lst1}") # This is lst1 after modifying lst3: ['a']

' some text '.strip() # some text 去头去尾的空格。