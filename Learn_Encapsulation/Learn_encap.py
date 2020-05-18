class testleaf:

    mentors = ['B', 'G', 'B', 'D']
    __value = None

    def get_info(self):
        print('public')


    def __get_private_info(self):
        print('private')


    def get_value(self):
        return testleaf.__value

    def set_value(self, val):
          testleaf.__value = val


    def get_private_methods(self):
        testleaf.__get_private_info(self)





test = testleaf()
print(test.mentors)
test.get_info()
print(test.get_value())
test.set_value(100)

print(test.get_value())
test.get_private_methods()
