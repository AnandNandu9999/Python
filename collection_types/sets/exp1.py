thisset = {"apple", "banana", "orange"}

print(thisset)

new_set = {"hello", "kiwi"}

thisset.update(new_set)
print(thisset)

list_data = ["pineapple", "mango", "grapes"]

thisset.update(list_data)
print(thisset)

thisset.add("NewFruit")
print(thisset)
