import re
import time


class Regular_Exp(object):
    def __init__(self, regex, string, file_name=None):
        self.regex = regex
        self.str = string
        self.filename = file_name
        self.final_data = []

    def perform_regex(self):
        start = time.time()
        if type(self.str) != type(self.final_data):
            print("Checking the regex in data: ", self.str)
            result = re.search(self.regex, self.str)
            # <class 're.Match'>
            # print(type(result))
            # fetches the found string
            if result is not None:
                print(result.group())
            else:
                print("Not Found")
        else:
            for i in self.str:
                print("Checking the regex in list of data: ", i)
                # result = re.search(self.regex, i)
                # if result is not None:
                #     self.final_data.append(result.group())

                result = re.findall(self.regex, i.strip())
                if len(result) != 0:
                    self.final_data.extend(result)
            print(self.final_data)

        end = time.time()
        print("Execution Time: ", end - start)

    def read_the_file(self, ):
        with open(self.filename, "r") as fp:
            self.str = fp.readlines()
        print("Data read from file:\n", self.str)
        print("Type of data read from file is of type: ", type(self.str))
        self.perform_regex()

    def get_names(self):
        for i in self.final_data:
            x = re.split(":", i)
            print(x[1])


if __name__ == '__main__':
    input_string = "I am name:@Anand, Pursuing Grade:B.Tech in College:MRU, name:Prasad"
    regexp = r"name:\w+"
    obj = Regular_Exp(regexp, input_string, "anand")
    obj.perform_regex()
    obj.read_the_file()
    obj.get_names()
