'''
Class example
# Pikachu, Raichu
'''
class Pikachu:
    def __init__(self, poke_name, poke_type, poke_weight, poke_height, poke_cp, poke_hp):
        self.poke_name = poke_name
        self.poke_type = poke_type
        self.poke_weight = poke_weight
        self.poke_height = poke_height
        self.poke_cp = poke_cp
        self.poke_hp = poke_hp

    def first_skill(self):
        print ('Thunder Shock')
        return ('Thunder Shock', 3)

    def second_skill(self):
        print ('Thunder')
        return ('Thunder', 100)

def main():
    pikachu = Pikachu('pikachu', 'Eletric', 30, 30, 30, 30)
    print (pikachu.poke_name)
    pikachu.first_skill()
    pikachu.second_skill()
    pikachu.poke_name = 'hello'
    pikachu.poke_cp = 1000
    print (pikachu.poke_name)
    print (pikachu.poke_cp)

if __name__ == '__main__':
    main()