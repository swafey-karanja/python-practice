class last_name:

    def lastname(self , x):
        self.lastname = x
        print(str(self.lastname))


class name(last_name):

    def firstname(self , y):
        self.firstname = y
        print(str(self.firstname))

orewa = name()
orewa.firstname('satoru')
orewa.lastname('gojo')

