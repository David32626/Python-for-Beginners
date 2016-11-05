class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print ("Last name: " + self.last_name)
        print ("Eye color: " + self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        print ("Child Constructor Called")
        super().__init__(last_name, eye_color)
        self.toys = toys
    
    # method overriding
    def show_info(self):
        print ("Last name: " + self.last_name)
        print ("Eye color: " + self.eye_color)
        print ("Number of toys: " + str(self.toys))
    
def main():
    david_lee = Parent("Lee", "blue")
    print (david_lee.last_name)
    david_lee.show_info()
    print("----------------------------")

    andy_lee = Child("Lee", "blue", 3)
    print (andy_lee.last_name)
    print (andy_lee.toys)
    andy_lee.show_info()

if __name__ == '__main__':
    main()