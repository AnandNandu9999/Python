import re


class Filter:
    def __init__(self, str, regex):
        self.str = str
        self.regex = regex

    def check_regexx(self):
        res = re.search(r"{}".format(self.regex), self.str)
        if res:
            return True
        else:
            return False


# fp = open("anand", 'r')

# regex = re.search(r"name:.*", fp.readlines())

str = "Its raining now"
# regexx = "^Its"
regexx = r"ain\B"

obj = Filter(str, regexx)
print(obj.check_regexx())
