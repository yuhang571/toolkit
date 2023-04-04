import yfinance
start = '2020-01-01'
end = None
tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    print(df)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')

tic = 'QAN.AX'                        #                       (1)
tic = tic.lower()                     # --> 'qan.ax'          (2)
tic_base = tic.split('.')[0]          # --> 'qan'             (3)
csv_name = f'{tic_base}_stk_prc.csv'  # --> 'qan_stk_prc.csv' (4)
print(csv_name)                       #                       (5)

def mk_csv_name(tic):
    tic = tic.lower()
    tic_base = tic.split('.')[0]
    csv_name = f'{tic_base}_stk_prc.csv'
    return csv_name

def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)

def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)
# Call the function
res = qan_tic()           # (5b)
# QAN.AX

# Define a function called `qan_tic`
def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)
# Call the function
qan_tic()                 # (5)
# QAN.AX

# Define a function called `qan_tic`
def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    return tic            # (4)     <-- Function will exit here!
    print(tic)            # (3)     <-- Will not be printed!
# Call the function
res = qan_tic()           # (5b)

# Define a function called `qan_tic`
def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
# Call the function
res = qan_tic()           # (5b)
# QAN.AX

# Define a function called `qan_tic`
def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
# Call the function
res = qan_tic()           # (5b)
print(res)                # --> None


def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
# Call the function
res = qan_tic()           # (5b)
print(res)                # --> None
# QAN.AX
# None

def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)
print(qan_tic)
# <function qan_tic at 0x7f359e53bd90>

def qan_tic():
    tic = "QAN.AX"        # <-- local
    print(tic)
    return tic
tic = "WES.AX"            # <-- global

def qan_tic():            # (1)
    tic = "QAN.AX"        # (2)
    print(tic)            # (3)
    return tic            # (4)
tic = "WES.AX"            # (5)
print(tic)                # (6)
qan_tic()                 # (7)
# WES.AX
# QAN.AX

def qan_tic():            # (1)
    print(tic)            # (3)
    return tic            # (4)
tic = "WES.AX"            # (5)
print(tic)                # (6)
qan_tic()                 # (7)
# WES.AX
# WES.AX

def mk_csv_name(tic):                   # (1)
    tic = tic.lower()                   # (2)
    tic_base = tic.split('.')[0]        # (3)
    return f'{tic_base}_stk_prc.csv'    # (4)
name = mk_csv_name('QAN.AX')            # (5)
print(name)                             # (6)

def mk_csv_name(tic, show=True):
    tic = tic.lower()
    tic_base = tic.split('.')[0]
    name = f'{tic_base}_stk_prc.csv'
    if show is True:
        print(name)
    return name
name = mk_csv_name('QAN.AX')

evens = []
for x in range(1_000_000 + 1):
    if x % 2 == 0:
        evens.append(x)
print(evens[:10])
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

evens = [x for x in range(1_000_000 + 1) if x % 2 == 0] # same as line 127 to line 132
print(evens[:10])

pairs = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]
# Create an empty dictionary
dic = {}                      # (1)
# Iterate over each tuple in `pairs` and update the dictionary
for key, value in pairs:      # (2)
    dic.update({key:value})   # (3)
print(dic)
# {'a': 1, 'b': 2, 'c': 3}

pairs = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]
# This WILL work
dic = {key:value for key, value in pairs}    # same as line 137 to line 148
print(dic)

# Create a dictionary
dic = {'a': 1, 'b': 2, 'c': 3}
# Create a list of (key, val) tuples called `pairs`
pairs = []
for key, value in dic.items( ):
    pairs.append((key,value))
print(pairs)
# [('a', 1), ('b', 2), ('c', 3)]

# Start with a dictionary
dic = {'a': 1, 'b': 2, 'c': 3}    # same as line 159 to line 166
# Create a list of (key, val) using list comprehensions:
pairs = [(key,value) for key,value in dic.items( )]
print(pairs)

# Start with a dictionary
dic = {'a': 1, 'b': 2, 'c': 3}
# Create a set comprehension with the keys from `dic`
keys = {key for key in dic}
print(f'The type of {keys} is {type(keys)}')
# The type of {'b', 'c', 'a'} is <class 'set'>

# Some data (list of tuples)
data = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]
# Create a dict comprehension
dic = {k:v for k, v in data}
print(f'`dic` is {dic}')
print(f'type(dic) is: {type(dic)}')
# Create a list comprehension
lst = [(k, v) for k, v in data]
print(f'`lst` is {lst}')
print(f'type(lst) is {type(lst)}')
# Create a set comprehension
st = {k for k, v in data}
print(f'`st` is {st}')
print(f'type(st) is {type(st)}')
# `dic` is {'a': 1, 'b': 2, 'c': 3}
# type(dic) is: <class 'dict'>
# `lst` is [('a', 1), ('b', 2), ('c', 3)]
# type(lst) is <class 'list'>
# `st` is {'a', 'b', 'c'}
# type(st) is <class 'set'>

# Some data (list of tuples)
data = [
  ('a', 1),
  ('b', 2),
  ('c', 3),
  ]
# Is this a tuple comprehension?
not_a_tup = (k for k, v in data)
print(f'The type of `(k for k, v in data)` is {type(not_a_tup)}')
# The type of `(k for k, v in data)` is <class 'generator'>

# This function returns an `int` instance
def add(a,b):
    return a + b
# This function returns a `NoneType` instance
def useless( ):
    pass
# This function returns a `list` instance
def mk_a_list(a, b):
    return [a, b]

# list comprehension --> `list` instance
lst = [i for i in range(10_000_000)]
# Generator expression --> generator
gen = (i for i in range(10_000_000))