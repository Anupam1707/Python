#To print the pascal's triangle with n rows

#pascaltri.py

#24-3-23

#By Anupam Kanoongo



print("Welcome to the Pascal's Triangle Printer")

print()


def pascal(n):

    row = [1]

    for i in range(n):

        for a in range(n - len(row)):
            print(" ", end = " ")
            
        print(*row)

        
        row = [1] + [row[j] + row[j+1] for j in range(i)] + [1]


n = int(input("Enter Number of Rows : "))

pascal(n)



##Output

##Welcome to the Pascal's Triangle Printer
##
##Enter Number of Rows : 5
##    1
##   1 1
##  1 2 1
## 1 3 3 1
##1 4 6 4 1
