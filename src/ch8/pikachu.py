'''
Class example
# Pikachu, Raichu
'''
class Pikachu:
    def __init__(self, poke_name, poke_type, poke_weight, poke_height, poke_cp, poke_hp):
        self.name = poke_name
        self.type = poke_type
        self.weight = poke_weight
        self.height = poke_height
        self.cp = poke_cp
        self.hp = poke_hp

    def first_skill(self):
        print ('Thunder Shock')
        self.second_skill()
        return 60

    def second_skill(self):
        print ('Thunder')
        return 100

def main():
    pikachu = Pikachu('pika', 'Eletric', 30, 30, 300, 100)
    print ("name = ",pikachu.name)
    print ("cp = ",pikachu.cp)
    pikachu.first_skill()
    pikachu.second_skill()
    pikachu.name = 'chu'
    pikachu.cp = 1000
    print ("name = ",pikachu.name)
    print ("cp = ",pikachu.cp)

if __name__ == '__main__':
    main()