from pikachu_better import Pikachu
from pokemon_better import Vaporeon

class Game:
    def __init__(self):
        self.winner = ''

    def fight(self, first_poke, second_poke):
        first_poke_hp = first_poke.get_hp()
        second_poke_hp = second_poke.get_hp()

        while first_poke_hp >= 0 and second_poke_hp >= 0:
            if first_poke_hp or second_poke_hp >= 0:
                print ('first_poke_hp: {}'.format(first_poke_hp))
                first_poke_hp -= second_poke.first_skill()

                print ('second_poke_hp: {}'.format(second_poke_hp))
                second_poke_hp -= first_poke.first_skill()

            if first_poke_hp > second_poke_hp:
                self.winner = first_poke.name
            else:
                self.winner = second_poke.name
            
def main():
    pikachu = Pikachu('pika', 'Eletric', 30, 30, 300, 150)
    vaporeon = Vaporeon('vapor', 'Water', 30, 30, 250, 200)
    game = Game()
    game.fight(pikachu, vaporeon)
    print ('The winner is: {}!!!!'.format(game.winner))


if __name__ == '__main__':
    main()