from Check import check_r
from Check import check_c
from Check import check_b
def fill(matrix,size_v,size_h):
    change = False 


    for row_n in range(size_v):

        for space_n in range(size_h):
            #print "row: " + str(row_n) + "space: " + str(space_n)

            if matrix[row_n][space_n] == 0: #if (piece in) matrix (in row_n in space_n) == 0 (Which means that the space is empty  
                
                print "space ==0"
                ges = guess(matrix,row_n,space_n) #the answer
                if ges != 0: # if ges did not return 0, basically that there is actually something there

                    print "the piece " + str(row_n+1) + " and " + str(space_n+1) + " which now is: " + str(matrix[row_n][space_n]) + "will be replaced with " + str(ges)   #the line lets the user know what will be replaced with what 
                    matrix[row_n][space_n] = ges #the matrix in that specific row in that specific space changes to the ges(guess)
                    #for i in matrix:
                     #   print i 
                    print matrix # Prints the new stuff
                    change = True 
                else:
                    pass
            else:
                pass #in a case in which the space we are looking at is already full
    return change 
    
def guess(matrix,row,space):
    ans = 0 #how many answers we found
    res = 0 #what the result is
    for num in range(1,10): #we pick a possible number
        if check_r(matrix,row,num): # if it fits in that row 
            if check_c(matrix,space,num): # and in that column
                if check_b(matrix,row,space,num):
                    print "we found a match!" # print "We found a match"
                    ans += 1 # ans resembles how many answers we found
                    res = num 
            else:
                pass
        else:
            pass
    
    if ans == 1: #in which we found only 1 answer (and therefor its correct)
        return res #we return the only result we got
    else: #In a case which we found none or more than one answer
        return 0     
    return 0        