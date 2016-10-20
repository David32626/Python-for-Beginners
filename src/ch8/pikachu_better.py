'''
Class example
We can do better
'''

class Pikachu:
    def __init__(self, poke_name, poke_type, poke_weight, poke_height, poke_cp, poke_hp):
        self.name = poke_name
        self.__type = poke_type
        self.__weight = poke_weight
        self.__height = poke_height
        self.__cp = poke_cp
        self.__hp = poke_hp
    
    def get_name(self):
        return self.name
    
    def set_name(self, poke_name):
        self.__name = poke_name

    def get_hp(self):
        return self.__hp
    
    def set_hp(self, poke_hp):
        self.__hp = poke_hp

    def get_cp(self):
        return self.__cp
    
    def set_cp(self, poke_cp):
        self.__cp = poke_cp

    def first_skill(self):
        print ('Thunder Shock')
        return 60

    def second_skill(self):
        print ('Thunder')
        return 100

def main():
    pikachu = Pikachu('pika', 'Eletric', 30, 30, 300, 100)
    print ("name = ",pikachu.name)
    #print (pikachu.__cp)
    print("cp = ",pikachu.get_cp())

    pikachu.name = 'chu'
    print ("name = ",pikachu.name)

    pikachu.__cp = 1000
    print (pikachu.__cp)
    print("cp = ",pikachu.get_cp())
    pikachu.set_cp(400)
    print("cp = ",pikachu.get_cp())

if __name__ == '__main__':
    main()