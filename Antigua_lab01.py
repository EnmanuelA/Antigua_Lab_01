###Enmanuel Antigua
##    #Lab Assignment 1
##
###################################### 2.2 ######################################

#asking user to input number of lines
k = int(input("Please enter the number of lines you would like: "))

numOfLines=k
bBlocks = '#'

for k in range (1, numOfLines+1):
    #produce the output line for index k --> repeat k times the building block
    s = k * bBlocks

    #print the output line
    print(s) 

###################################### 2.3 ######################################

numOfLines=k 
bBlocks = '#'

for k in range (1, numOfLines+1):
    #produce the output line for index k --> repeat k times the building block

    numOfSpaces= numOfLines - k

    s = numOfSpaces * " " + (2*k- 1)* bBlocks

    #print the output line
    print(s)


