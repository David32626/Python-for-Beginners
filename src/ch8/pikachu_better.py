'''
Class example
We can do better
'''

class Pikachu:
    def __init__(self, poke_name, poke_type, poke_weight, poke_height, poke_cp, poke_hp):
        self.__poke_name = poke_name
        self.__poke_type = poke_type
        self.__poke_weight = poke_weight
        self.__poke_height = poke_height
        self.__poke_cp = poke_cp
        self.__poke_hp = poke_hp
    
    @property
    def poke_name(self):
        return self.__poke_name
    
    @poke_name.setter
    def poke_name(self, poke_name):
        self.__poke_name = poke_name

    @property
    def poke_hp(self):
        return self.__poke_hp
    
    @poke_hp.setter
    def poke_hp(self, poke_hp):
        self.__poke_hp = poke_hp

    def first_skill(self):
        print ('Thunder Shock')
        return ('Thunder Shock', 3)

    def second_skill(self):
        print ('Thunder')
        return ('Thunder', 100)

def main():
    pikachu = Pikachu('pikachu', 'Eletric', 30, 30, 30, 30)
    pikachu.first_skill()
    pikachu.second_skill()
    print (pikachu.poke_name)
    
    pikachu.poke_name = 'kobe'
    print (pikachu.poke_name)



if __name__ == '__main__':
    main()