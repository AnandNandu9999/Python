ITEM = obj.check_item("name")


class Dict:
    def __init__(self):
        self.Mydict = {
            "name": "ford",
            "model": "mustang",
            "year": 1991,
            # dictionary should not contain duplicate items
            # if any duplicate item is present,
            "year": 1992,
            "year": 1993
        }

    def print_dict(self):
        print(self.Mydict)

    def get_value_using_key(self):
        print(self.Mydict["name"])

    def get_value_using_getmethod(self):
        print(self.Mydict.get("model"))

    def add_items(self, key, value):
        self.Mydict[str(key)] = value
        print(self.Mydict)

    def print_keys_in_dict(self):
        print(self.Mydict.keys())

    def print_values_in_dict(self):
        print(self.Mydict.values())

    def print_items(self):
        print(self.Mydict.items())

    def check_item(self, key):
        if key in self.Mydict:
            print("True, key {} present in dictionary".format(key))
        else:
            print("False, key {} is not present in dictionary".format(key))


obj = Dict()
obj.print_dict()
obj.get_value_using_key()
obj.get_value_using_getmethod()
obj.add_items("colors", ["white", "red", "green"])
obj.print_keys_in_dict()
obj.print_values_in_dict()
obj.print_items()
obj.check_item("name")

