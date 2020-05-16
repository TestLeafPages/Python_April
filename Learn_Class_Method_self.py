class testleaf:

    mentors_name= ['Babu', 'Gopi', 'Balaji', 'Divya']      # class varialbe

    def stu_info(self, name, course, exp):
        print(self)
        print(f'The person {name} interested to join in {course} course and his overall exp is {exp}')

    def selenium(self):
        return f'trainer for {self.mentors_name[0]}'

    def appium(self):
        return f'trainer for {self.mentors_name[1]}'


    def more_info(self):
        print(self)
        print('more details')


per1 = testleaf()
print(per1.selenium())

print(per1)


