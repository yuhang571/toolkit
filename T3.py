happy = True
if happy is False:
    print("I am happy")
print("This will print regardless of the value of happy")

happy = True
very_happy = True

if happy is True:
    print("I am happy")                         # <-- four-spaces indentation
    if very_happy is True:                      # <-- four-spaces indentation
        print("Actually, I'm really happy!")    # <-- eight-spaces indentation

happy = 5
if happy:
    print("I am happy") # I am happy

happy = 0
if happy:
    print("I am happy") # <-- will not be printed

less_than_test = "That" < "This"
print(f'"That" < "This" yields {less_than_test}')
greater_than_test = "That" > "This"
print(f'"That" > "This" yields {greater_than_test}')

var1 = 'a'
var2 = 'a'
print(var1 is var2) # --> True
print(var1 == var2) # --> True

var3 = ['a']
var4 = ['a']
print(var3 is var4) # --> False
print(var3 == var4) # --> True # Choosing between == and is can be quite difficult at first so lets keep it simple:
# Use is only to test if something is either None, True, or False. For everything else, use ==.

b = False
if b is True:
   print("b is True")
else:
   print("b is not True")

a = 0
b = True
if a != 0:              # !=  is inequality
   print("a is non-zero")
elif b is True:
   print("b is True")
elif a < 0 and b is True:
   print("a is negative and b is True")
else:
   print("None of the conditions above hold")

a = -1
b = True
if a != 0:
   print("a is non-zero")
elif b is True:
   print("b is True") # 虽然也对，但是只有一个回答 从上开始只要对一个下面就不用看了。
elif a < 0 and b is True:
   print("a is negative and b is True")
else:
   print("None of the conditions above hold") 。

happy = True
if happy is True:
    pass

x = 0
y = 0
if x > 0 and y is True:
    pass
elif x <= 0 and y is True:
    pass
else:
    pass


