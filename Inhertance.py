class Parent ():
    def __init__(self, last_name, eye_color):
        print("parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("last name - "+ self.last_name)
        print("Eye Color - "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("child constuctor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("eye Color - "+self.eye_color)
        print("Number of toys-"+ self_number_of_toys)

#billy_cyrus = Parent("cyrus", "blue")
#print(billy_cyrus.eye_color)

miley_cyrus = Child("Cyrus", "blue", 5)
print(miley_cyrus.last_name)
print(miley_cyrus.number_of_toys)