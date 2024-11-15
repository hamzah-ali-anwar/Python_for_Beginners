dictionary = {"a": 1, "b": 2, "c": 3}
print(dictionary["c"])
print(dictionary["b"])
print(dictionary["a"])

birth_years = {"Alice": 1990, "Bob": 1991, "Charlie": 1992}
if 1991 in birth_years:
    print(birth_years[1991])
else:
    print("Not found")

print(birth_years.get("Alice"))