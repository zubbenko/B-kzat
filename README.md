# B-kzat 

class SuperHero:
    people = 'people'

    def __init__ (self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def name(self):
        return (f'Имя нашего героя{self.name}')

    def hp(self):
        self.health_points *= 2
        return (f'Здоровье нашего героя{self.health_points}')

    def __str__(self):
        return (f'Его прозвище {self.nickname} \n'
                f'Его суперспособность {self.superpower} \n'
                f'Его количество здоровья {self.health_points}')

    def __len__(self):
        return len(f'{self.catchphrase}')


Hunter = SuperHero("Anthony Edward Stark", "Hunter", "weapon,physical weakness", "100", "develop your own path to success")

print(Hunter)
print(Hunter.hp())
print(Hunter.__len__())
print(Hunter.catchphrase)
