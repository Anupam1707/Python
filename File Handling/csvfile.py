import csv

with open("Sports.csv","w", newline = "") as fh:
    writer = csv.writer(fh, delimiter = "\t")
    writer.writerow(["Sport", "Competition", "Prize Won"])
    state = True
    while state == True:
        for recno in range(100):
            print(f"Record {recno}")
            sport = str(input("Sport : "))
            comp = str(input("Competition : "))
            prize = str(input("Prize : "))
            writer.writerow([sport, comp, prize])

with open("Sports.csv","r", newline = "") as fh:
    reader = csv.reader(fh, delimiter= "\t")
    for rec in reader:
        print(rec)
