import csv
import json

# Ваш код для завдань нижче:
# import csv
#
# valid_transactions = []
# with open("files/transactions.csv", "r", encoding="utf-8") as file:
#     reader = csv.DictReader(file)
#     suma=0
#     for row in reader:
#         if row["status"]=="success":
#             try:
#                 suma += float( row["amount"])
#                 valid_transactions.append(row)
#             except:
#                 print(f"Unsupported value {row['amount']}")
# print(suma)
#
# with open ("files/valid_transactions.csv", "w", encoding="utf-8", newline='') as file:
#     writer =csv.DictWriter(file, fieldnames=valid_transactions[0].keys())
#     writer.writeheader()
#     writer.writerows(valid_transactions)

# users_new=[]
# with open ("files/users.json", "r", encoding="utf-8" ) as f:
#     users=json.load(f)
#     print(users)
#
#     for user in users:
#         if user["balance"]>1000:
#             users_new.append({"id": user["id"], "balance": user["balance"], "status": user.get("VIP", "VIP")})
#         else:
#             users_new.append({"id": user["id"], "balance" : user["balance"], "status" : "regular"})
# print(users_new)

import json
with open("files/users.json", "r", encoding="utf-8") as file:
    users = json.load(file)
for user in users:
    user["balance"] += 50
with open("files/users_bonus.json", "w", encoding="utf-8") as file:
    json.dump(users, file, indent=4, ensure_ascii=False)

