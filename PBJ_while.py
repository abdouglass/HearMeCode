# Goal #1: Write a new version of the PB&J program that uses a while loop.  Print "Making sandwich #" and the number of the sandwich until you are out of bread, peanut butter, or jelly.

# Example:
# bread = 4
# peanut_butter = 3
# jelly = 10

# Output:
# Making sandwich #1
# Making sandwich #2
# All done; only had enough bread for 2 sandwiches.

# Goal #2: Modify that program to say how many sandwiches-worth of each ingredient remains.

# Example 2:
# bread = 10
# peanut_butter = 10
# jelly = 4

# Output:
# Making sandwich #1
# I have enough bread for 4 more sandwiches, enough peanut butter for 9 more, and enough jelly for 3 more.
# Making sandwich #2
# I have enough bread for 3 more sandwiches, enough peanut butter for 8 more, and enough jelly for 2 more.
# Making sandwich #3
# I have enough bread for 2 more sandwiches, enough peanut butter for 7 more, and enough jelly for 1 more.
# Making sandwich #4
# All done; I ran out of jelly.

jelly = raw_input("How much jelly?")
jelly = int(jelly)
pb = raw_input("How much pb?")
pb = int(pb)
bread = raw_input("How much bread?")
bread = int(bread)
sandwich = min(bread/2,jelly,pb)
CurrentSandwich = 1
currentBread = bread/2
currentPB = pb
currentJelly = jelly


while sandwich > 0:
    currentBread = currentBread - 1
    currentPB = currentPB - 1
    currentJelly = currentJelly - 1
    print "Making sandwich #{0}.  I have enough bread for {1} more sandwiches, enough peanut butter for {2} more sandwiches, and enough jelly for {3} more sandwiches".format(CurrentSandwich,currentBread,currentPB,currentJelly)    
    CurrentSandwich = CurrentSandwich + 1
    sandwich = sandwich - 1
    if currentJelly == 0:
        print "You need more jelly"
    if currentBread == 0:
        print "You need more bread."
    if currentPB == 0:
        print "You need more peanut butter."
print "You don't have enough supplies."
