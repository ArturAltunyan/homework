human = {"name": "Artur", "surname": "Altunyan", "Age": 36}
print(human)
print(human["name"], human["surname"], human["Age"])
human["have_pet"] = True
del human["Age"]
print(human)