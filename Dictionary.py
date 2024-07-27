# Dictionary store data values in pairs.

dictionary1 = {"brand": "Ford",
               "model": "Mustang",
               "year": 1999,
               }
print(dictionary1)
print(dictionary1["year"])
print(dictionary1["model"])
print(dictionary1["brand"])
print(len(dictionary1))
print(type(dictionary1))

"""
{'brand': 'Ford', 'model': 'Mustang', 'year': 1999}
1999
Mustang
Ford
3
<class 'dict'>
"""

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

