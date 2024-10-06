capital={"UK":"London",
         "Japan":"Toyko",
         "China":"Beijing",
         "Italy":"Rome",
         "switzerland":"Bern"}
#accessing values
print(capital["Italy"])
print(capital.get("poland"))

#get the list of keys
print(capital.keys())

#getting list of values
print(capital.values())

#adding/changing value
capital["France"]="Paris"

print(capital)

capital["UK"]="England"

print(capital)
