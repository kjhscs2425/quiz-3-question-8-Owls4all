import json
f = open("expenses.json")
stuff=json.load(f)
# read `expenses.json`
runningTotal=0
things=stuff["pet store"]
for item in things:
    runningTotal+=item['price']
# get and print total "price" for all expenses at the "pet store"
print(runningTotal)