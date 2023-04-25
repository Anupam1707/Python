#To read the details of a telephone data file and print systematically
#telepy.py
#25-4-23
#By Anupam Kanoongo

with open("tele.txt", "r") as t:
    dt = t.readlines()

print("S.No\t\tName\t\tTelephone")
for i in range(len(dt)):
    print(i+1,"\t\t" ,dt[i].split()[0] , "\t\t", dt[i].split()[1])


##Output
##S.No		Name		Telephone
##1 		 Arvind 		 1234567
##2 		 Sachin 		 7654321
##3 		 Anmol 		 1356723
