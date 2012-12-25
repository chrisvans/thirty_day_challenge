# Exercises for chapter 2: Problems 2.1, 2.2, 2.3, and 2.4 in Think Python

# chrisvans - Chris Van Schyndel

#2.1

# zipcode = 02492
# print zipcode
# Results in an error because 9 is > 7, and an 8 (or more) would be 
# represented by a number in the next place up.
# Each value in each place represents a binary place number, 
# multiplied by the number provided.  So in this case, 
# zipcode = 02132
# The first 0 denotes that it is a binary number
# 0001 * 2 + 0010 * 3 + 0100 * 1 + 1000 * 2

#2.2

# 5 and x + 1 return nothing when run as a script.  It is evaluated but
# nothing is done with it.
# x = 5 sets the variable x to integer 5.
# As print statements, 5 outputs 5, x = 5 outputs an error ( cannot assign
# during print statement ), x + 1 outputs 6.


#2.3

# 1. 8.5 - float
# 2. 8.5 - float
# 3. 4 - integer
# 4. 11 - integer
# 5. ..... - string

#2.4

# 1. 523.5987755982989

# 2. $945.45 ( rounded up from .44999~)

bookprice = 24.95
discount = .60
shipping_first = 3
shipping_additional = .75
books = 60

subtotal = shipping_first + bookprice * books + shipping_additional * (books - 1)
final = subtotal * discount
final
# This offers an answer if the discount applies to shipping, which it wouldn't.
alternate_final = (bookprice * books) * discount + shipping_first + shipping_additional * 59
alternate_final
# This is the answer for a discount on books before shipping.

# 3. 7:30.06 am

starting_time = 6 + 52/60
# in hours

easy_pace = (8 + 15/60) / 60
tempo = (7 + 12/60) / 60
# in hours

hours = starting_time + easy_pace * 2 + tempo * 3
hours
# take the integer away from hours to find the minutes
minutes = hours - 7
minutes *= 60
# convert back to time measurement
seconds = minutes - 30
seconds *= 60
# concatenate for answer
answer = str(int(hours)) + ':' + str(int(minutes)) + '.' + str(int(seconds))
