# Import the yfinance module
import yfinance
# Set the dates parameters
start = '2020-01-01'
end = None
# Download Qantas stock prices
tic = "QAN.AX"  # (Q1)
df = yfinance.download(tic, start, end, ignore_tz=True)  # (Q2)
print(df)  # (Q3)
df.to_csv('qan_stk_prc.csv')  # (Q4)
# Download Wesfarmers stock prices
tic = "WES.AX"  # (W1)
df = yfinance.download(tic, start, end, ignore_tz=True)  # (W2)
print(df)  # (W3)
df.to_csv('wes_stk_prc.csv')  # (W4)

# NOTE: You won't be able to execute this code in ED
import yfinance
start = '2020-01-01'
end = None
tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
    df = yfinance.download(tic, start, end, ignore_tz=True)
    print(df)
    tic_base = tic.lower().split('.')[0]
    df.to_csv(f'{tic_base}_stk_prc.csv')

tic = "QAN.AX"
# Convert the ticker to lower case
tic_base = tic.lower()              # --> 'qan.ax'
# Split the string into a list,
# using '.' as a separator
tic_base = tic_base.split('.')    # --> ['qan', 'ax']
# Fetch the first element of the list
tic_base = tic_base[0]            # --> 'qan'

for v in ("string", True, 1):
    print(v)
# string
# True
# 1

tickers = set()
tickers.add("QAN.AX")
tickers.add("QAN.AX")
tickers.add("WES.AX")
for tic in tickers:
    print(tic)
# WES.AX
# QAN.AX

d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for key in d:
    print(key)
# beauty
# truth
# red wheelbarrow
# 5

d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for val in d.values():
    print(val)
# True
# True
# 100000
# fingers

d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for key_value_tuple in d.items():
    print(f"key_value_tuple is {key_value_tuple}")
    # Unpacking
    key, value = key_value_tuple
    print(f"KEY: {key} VALUE: {value}")
# key_value_tuple is ('beauty', True)
# KEY: beauty VALUE: True
# key_value_tuple is ('truth', True)
# KEY: truth VALUE: True
# key_value_tuple is ('red wheelbarrow', 100000)
# KEY: red wheelbarrow VALUE: 100000
# key_value_tuple is (5, 'fingers')
# KEY: 5 VALUE: fingers

d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for key, value in d.items():
    print(f'KEY: {key} VALUE: {value}')
# KEY: beauty VALUE: True
# KEY: truth VALUE: True
# KEY: red wheelbarrow VALUE: 100000
# KEY: 5 VALUE: fingers

for i in range(0, 5):      # same as (0, 5, 1) defaults is 1.
    print(f"i is now {i}")
# i is now 0
# i is now 1
# i is now 2
# i is now 3
# i is now 4

for i in range(5):    # (5) is shortcut to range(0, stop)
    print("i is now {}".format(i))

for even in range(0, 9, 2):
    print("even is now {}".format(even))
# even is now 0
# even is now 2
# even is now 4
# even is now 6
# even is now 8

for i in range(5, 0):
    print("This will not execute because start is greater than stop.")
for i in range(5, 0, -1):
    print("This message will self-destruct in {} secs...".format(i))
# 5
# 4
# 3
# 2
# 1

letters = ["a", "b", "c", "d", "e"]
print(f"letters = {letters}")
i = 0
for x in letters:
    print(f"letters[{i}] --> {x}")
    i += 1
# letters = ['a', 'b', 'c', 'd', 'e']
# letters[0] --> a
# letters[1] --> b
# letters[2] --> c
# letters[3] --> d
# letters[4] --> e

letters = ["a", "b", "c", "d", "e"]
for tup in enumerate(letters):
    print(tup)
# (0, 'a')
# (1, 'b')
# (2, 'c')
# (3, 'd')
# (4, 'e')

letters = ["a", "b", "c", "d", "e"]  # same as 140 line to 151 line.
print(f"letters = {letters}")
for i, x in enumerate(letters):
    print(f"letters[{i}] --> {x}")

d = {
    "beauty": True,
    "truth": True,
    "red wheelbarrow": 100000,
    5: "fingers",
    }
for i, tup in enumerate(d.items()): # "for i, tup in enumerate(d.items(), start=1000):"
    print(f'Iteration {i} gives {tup}')
# Iteration 0 gives ('beauty', True) # "Iteration 1000 gives ('beauty', True)"
# Iteration 1 gives ('truth', True)
# Iteration 2 gives ('red wheelbarrow', 100000)
# Iteration 3 gives (5, 'fingers')

the_sum = 0
for i in range(1,101):          # for loop
   the_sum = the_sum + i
print(the_sum)
# 5050

the_sum = 0
i = 1
while i <= 100:                # while loop
    the_sum = the_sum + i
    i = i + 1
print(the_sum)
# 5050

years = [2018, 2019, 2020]
months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May",
    "Jun",
    "Jul",
    "Aug",
    "Sep",
    "Oct",
    "Nov",
    "Dec",
    ]

for year in years:
   for month in months:
       print("Year: {}, Month: {}".format(year, month))
# Year: 2018, Month: Jan
# Year: 2018, Month: Feb
# ..... shenglue
# Year: 2020, Month: Nov
# Year: 2020, Month: Dec

sum_of_evens = 0
for i in range(1,101):
    if i % 2 == 0: # i is even
        sum_of_evens = sum_of_evens + i
print(f'Sum of evens is {sum_of_evens}')
# Sum of evens is 2550

sum_of_evens = 0
for i in range(1,101):
    print(f'Loop is on {i}')
    if i % 2 == 1:      # i is odd
        continue              # 如果条件达成就返回
    print(f'    summing the value of {i}')
    sum_of_evens = sum_of_evens + i
print(f'Sum of evens is {sum_of_evens}')
# Loop is on 1
# Loop is on 2
#     summing the value of 2
# Loop is on 3
# Loop is on 4
#     summing the value of 4
# .....
# Loop is on 97
# Loop is on 98
#     summing the value of 98
# Loop is on 99
# Loop is on 100
#     summing the value of 100
# Sum of evens is 2550

the_sum = 0
for i in range(1,101):
    if i % 2 != 0 and i % 3 != 0 and i % 7 != 0 and i % 13 !=0:
        print(f'    the_sum is {the_sum}')
        the_sum = the_sum + i
print(f'Sum is {the_sum}')
#     the_sum is 0
#     the_sum is 1
#     the_sum is 6
# ......
#     the_sum is 1199
# Sum is 1296

the_sum = 0                 # same as line 249 to line 260
for i in range(1,101):
    if i % 2 == 0:
        continue
    if i % 3 == 0:
        continue
    if i % 7 == 0:
        continue
    if i % 13 == 0:
        continue
    print(f'    the_sum is {the_sum}')
    the_sum = the_sum + i
print(f'Sum is {the_sum}')

fib_current = 1
fib_prior = 0
while fib_current < 10000:
    print(f'Fibonacci value is {fib_current}')
    fib_current, fib_prior = fib_current + fib_prior, fib_current
print(f'First Fibonacci value greater than 10,000 is {fib_current}')

fib_current = 1
fib_prior = 0
while fib_current < 10000:
    print(f'Fibonacci value is {fib_current}')
    fib_current, fib_prior = fib_current + fib_prior, fib_current
print(f'First Fibonacci value greater than 10,000 is {fib_current}')

# Fibonacci value is 1
# Fibonacci value is 1
# Fibonacci value is 2
# Fibonacci value is 3
# .....
# Fibonacci value is 1597
# Fibonacci value is 2584
# Fibonacci value is 4181
# Fibonacci value is 6765
# First Fibonacci value greater than 10,000 is 10946

fib_current = 1           # same as line 276 to line 299
fib_prior = 0
while True:
    print(f'Fibonacci value is {fib_current}')
    fib_current, fib_prior = fib_current + fib_prior, fib_current
    if fib_current >= 10000:
        break    # 如果条件达成，就结束。
print(f'First Fibonacci value greater than 10,000 is {fib_current}')

for x in range(0, 4):
    print(f"Outer loop: x = {x}")
    for y in range(0,4):
        print(f"    Start of Inner loop: y = {y}")
        if x + y >= 4:
            print(f"    x = {x} and y ={y} have sum >= 4, continuing to next y value")
            continue
        elif (x + y) % 2 != 0:
            print(f"    x = {x} and y = {y} have non-even sum, continuing to next y value")
            continue
        print(f"    x = {x} and y = {y} have even sum less than 4")

for x in range(0, 4):
    print(f"Outer loop: x = {x}")
    for y in range(0,4):
        print(f"    Start of Inner loop: y = {y}")
        if y > x:
            print(f"    y = {y} > x = {x}, breaking out of inner loop")
            break
        elif x + y >= 4:
            print(f"    x = {x} and y ={y} have sum >= 4, continuing to next y value")
            continue
        elif (x + y) % 2 != 0:
            print(f"    x = {x} and y = {y} have non-even sum, continuing to next y value")
            continue
        print(f"    x = {x} and y = {y} have even sum less than 4")


for even in range(0, 10, 2):
    print(even)
    if even > 2:
        break
# 0
# 2
# 4


for odd in range(1, 10, 2):
    for even in range(0, 10, 2):
        if even > 2:
            break
    print(even, odd)
# 4 1
# 4 3
# 4 5
# 4 7
# 4 9

for even in range(0, 10, 2):
    print(even)
    if even > 2:
        continue
    print(even, odd)
# 0
# 2
# 4
# 6
# 8

for even in range(0, 10, 2):
    if even > 2:
        continue
    print(even)
# 0




