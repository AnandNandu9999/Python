from regex.exp1 import Regular_Exp


string = "Hello, Anand email is adonga@qti.qualcomm.com asdas"
regex = r"\w+\@[\w+\W]+\bcom"
filename = "email_data"

obj = Regular_Exp(regex, string, filename)
obj.read_the_file()


