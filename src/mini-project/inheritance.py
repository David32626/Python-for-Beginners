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
    david_jiang = Parent("Jiang", "blue")
    print (david_jiang.last_name)
    david_jiang.show_info()
    print("----------------------------")

    andy_jiang = Child("Jiang", "blue", 3)
    print (andy_jiang.last_name)
    print (andy_jiang.toys)
    andy_jiang.show_info()

if __name__ == '__main__':
    main()