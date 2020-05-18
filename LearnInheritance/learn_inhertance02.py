# testleaf - python, appium, devops, selenium.....


class Testleaf:

    def registration(self):
        print('details: ')

    def collect_fee(self):
        print('done')


class python(Testleaf):

    def agenda(self):
        print('agenda')


class data_science(python):

    def ds_info(self):
        print('ds')



class appium(Testleaf):

    def android_test_info(self):
        print('android')


per1 = python()
per1.registration()
per1.collect_fee()
per1.agenda()

print("*"* 25)

per2 = appium()
per2.registration()
per2.collect_fee()
per2.android_test_info()

print("*"* 25)

per3 = data_science()
per3.registration()
per3.collect_fee()
per3.agenda()
per3.ds_info()


# multilevel inheritance  -> data_science extends python extends testleaf