import csv
import json

# Ваш код для завдань нижче:
import csv

valid_transactions = []
with open("files/transactions.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    suma=0
    for row in reader:
        if row["status"]=="success":
            try:
                suma += float( row["amount"])
                valid_transactions.append(row)
            except:
                print(f"Unsupported value {row['amount']}")
print(suma)

with open ("files/valid_transactions.csv", "w", encoding="utf-8", newline='') as file:
    writer =csv.DictWriter(file, fieldnames=valid_transactions[0].keys())
    writer.writeheader()
    writer.writerows(valid_transactions)

    