# Can you make Python print out the song for 99 bottles of beer on the wall?

# Note: You can use range() in three different ways

beers = raw_input("How many beers do you have?")
beers = int(beers)

for current in range(beers, 0, -1):
    print "{0} bottles of beer on the wall, {0} bottles of beer.  Take one down, pass it around, {1} bottles of beer on the wall".format(current, current - 1)

#while beers > 0:
 #   print "{0} bottles of beer on the wall, {0} bottles of beer.".format(beers)
  #  beers = beers - 1
   # print "  Take one down and pass it around. {0} bottles of beer on the wall.".format(beers)


# First:
# range(5) will give you a list containing [0, 1, 2, 3, 4]
# In this case, range assumes you want to start counting at 0, and the parameter you give is the number to stop *just* short of.

# Second:
# range(5, 10) will give you a list containing [5, 6, 7, 8, 9]
# In this case, the two parameters you give to range() are the number to start at and the number to stop *just* short of.
# Helpful mnemonic: range(start, stop)

# Third:
# range(5, 15, 3) will give you a list containing [5, 8, 11, 14]
# In this case, the three parameters you give to range() are the number to start at, the number to stop *just* short of, and the number to increment each time by.
# Note that normally, the number to increment each time by is assumed to be 1.  (In other words, you add 1 each time through.)
# That's why it goes [0, 1, 2, 3, 4] unless you specify that third parameter, called the step.
# Helpful mnemonic: range(start, stop, step)

# Using range() and a loop, print out the song. 
