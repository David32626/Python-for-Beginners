from pikachu_better import Pikachu
from eevee_better import Vaporeon, Flareon

class Game:
    def __init__(self, first_poke, second_poke):
        self.winner = ''
        self.first_poke = first_poke
        self.second_poke = second_poke

    def fight(self):
        first_poke = self.first_poke
        second_poke = self.second_poke
        first_poke_hp = self.first_poke.poke_hp
        second_poke_hp = self.second_poke.poke_hp

        while first_poke_hp >= 0 and second_poke_hp >= 0:
            if first_poke_hp or second_poke_hp >= 0:
                print ('first_poke_hp: {}'.format(first_poke_hp))
                first_poke_hp = first_poke_hp - second_poke.first_skill()[1]
                print ('second_poke_hp: {}'.format(second_poke_hp))
                second_poke_hp = second_poke_hp - first_poke.first_skill()[1]
            if first_poke_hp > second_poke_hp:
                self.winner = first_poke.poke_name
            else:
                self.winner = second_poke.poke_name
            
def main():
    pikachu = Pikachu('pikachu', 'Eletric', 30, 30, 30, 30)
    vaporeon = Vaporeon('vaporeon', 'Water', 30, 30, 30, 50)
    game = Game(pikachu, vaporeon)
    game.fight()
    print ('The winner is: {}'.format(game.winner))


if __name__ == '__main__':
    main()