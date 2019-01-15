from Create import create
from Guess import fill
print "Hello"


matrix = create()


more = True 
while more:
    if fill(matrix,9,9):
        pass
    else:
        more = False 
for row in matrix:
    print row
