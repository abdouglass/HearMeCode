# Peanut Butter Jelly Time!

# First Goal: Create a program that can tell you whether or not you can make a peanut butter and jelly sandwich

# Second Goal: Modify that program to tell you: if you can make a sandwich, how many you can make 

# Third Goal: Modify that program to allow you to make open-face sandwiches if you have an odd number of slices of bread ( )

# Fourth Goal: Modify that program to tell you: if you're missing ingredients, which ones you need to be able to make your sandwiches

# Fifth Goal: Modify that program to tell you: if you have enough bread and peanut butter but no jelly, that you can make a peanut butter sandwich but you should take a hard, honest look at your life.  Wow, your program is kinda judgy.

jelly = raw_input("How much jelly?")
jelly = int(jelly)
pb = raw_input("How much pb?")
pb = int(pb)
bread = raw_input("How much bread?")
bread = int(bread)
sandwich = min(bread/2,jelly,pb)
if bread == 0:
    print "You don't have enough bread"
elif jelly == 0 and pb ==0:
    print "You don't have enough jelly or pb"
elif jelly == 0:
    print "You don't have enough jelly but can make a pb sandwich"
elif pb == 0:
    print "You don't have enough pb but can make a jelly sandwich"
elif bread == 1:
    print "You can make an open faced pb&j sandwich"
else:
    print "You can make {0} pb&j sandwich".format(sandwich)
