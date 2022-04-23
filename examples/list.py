our_list = ['one', 'two', 'three']
our_dict = {'a': 'google', 'b': 'amazon', 'c': 'nasa','d': 'elon'}
our_list_dict = [our_dict]

for value in our_list:
    print(value)

for key, value in our_dict.items():
    print(value)

print(our_list_dict)
for i in our_list_dict:
    for key, value in i.items():
        print(value)