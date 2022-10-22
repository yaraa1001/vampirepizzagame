class Monster(object):
    eats= 'food'
    def __init__(self, name, mons_id):
        self.name = name
        self.id = mons_id

    def speak(self):
        print(self.name + ' Speaks my id is ' + str(self.id))
    def eat(self,meal):
        if meal == self.eats:
            print('yum!')
        else:
            print('blech')

my_monster = Monster('Spooky Snack', 1)
baba_m = Monster('baba', 2)
my_monster.speak()
baba_m.speak()
my_monster.eat('apple')