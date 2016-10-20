'''
Inheritance example
# Eevee(Normal), Vaporeon(Water), Jolteon(Eletric), Flareon(Fire)
'''

class Vaporeon:
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

    def get_cp(self):
        return self.__cp
    
    def set_cp(self, poke_cp):
        self.__cp = poke_cp

    def first_skill(self):
        print ('Water Gun')
        return 40

    def second_skill(self):
        print ('Hydro Pump')
        return 100

class Flareon:
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

    def get_cp(self):
        return self.__cp
    
    def set_cp(self, poke_cp):
        self.__cp = poke_cp

    def first_skill(self):
        print ('Ember')
        return 50

    def second_skill(self):
        print ('Fire Blast')
        return 100


def main():
    vaporeon = Vaporeon('vapor', 'Water', 30, 30, 250, 200)
    flareon = Flareon('flar', 'Fire', 30, 30, 350, 230)
    vaporeon.first_skill()
    flareon.first_skill()

if __name__ == '__main__':
    main()