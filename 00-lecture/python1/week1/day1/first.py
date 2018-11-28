# Set myNumber to 42 . Set myName to your name. Now swap myNumber into myName & vice versa.
my_number = 42
my_name = "Wes"
# temp = my_name
# my_name = my_number
# my_number = temp

my_number, my_name = (my_name, my_number)

# print(my_name, my_number)


my_tuple = ("thing one", "thing two")
my_tuple = "something else"
# print(my_tuple)

# given lowNum , highNum , mult , print multiples of mult from highNum down to lowNum , using a FOR . For (2,9,3) , print 963 (on successive lines).

def flexible_countdown(low_num, high_num, mult):
  for i in range(high_num, low_num - 1, -1):
    if i % mult == 0:
      print(i)

# flexible_countdown(2, 15, 4)

def flex_while(low_num, high_num, mult):
  i = high_num
  while i >= low_num:
    if i % mult == 0:
      print(i)
    i -= 1

# flex_while(2, 15, 4)

demo = ['string', 10, 10.1, True, ("hi", "hey"), ["woah"], {"key": "value"}]

for value in demo:
  print(type(value))
  if isinstance(value, str) == True:
    print("We found a string!")