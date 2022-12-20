class Hero:
    hp = 100
    def __init__(self,name,abyliti):
        self.name=name
        self.abyliti=abyliti

    print('it is super hero:')
    def __str__(self):
     return f' name is {self.name}\n' \
            f' abyliti is {self.abyliti}\n' \
            f' health is {self.hp}'

hero = Hero('Jotaro','Starplatinum')
print(hero)

class Hero_super:


    def __str__(self):
        return f' name is {self.name}\n' \
               f' abyliti is {self.abyliti}\n' \
               f' health is {self.hp}'
