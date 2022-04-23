import re

regex = r"(<)?(\w+@\w+(?:\.\w+)+)(?(1)>|$)"

string = "hellde <anand@yahoo.com> kkasdasd"

out = re.search(regex, string)

# gives the starting position of the found string and
# the end of that founded string position
print(out.span())

# prints the founded string
print(out.group())

# prints the passed string to the function
print(out.string)
