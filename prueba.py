class Person:
    name = ''
    school = ''
     
    def print_name(self):
        print(self.name)
         
    def print_school(self):
        print(self.school)
     
jorge = Person()
jorge.name = 'Jorge'
jorge.school = 'Universidad de la vida'
jorge.print_name()
jorge.print_school()