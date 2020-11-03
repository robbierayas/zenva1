# Python language basics 7
# Classes and objects
# Class fields, methods, and constructors
# Object instantiation

class GameCharacter:

    speed = 5

    def __init__(self, name, width, height, x_pos, y_pos):
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    def move(self, by_x_amount, by_y_amount):
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount


character_0 = GameCharacter('char_0', 50, 100, 100, 100)
print(character_0.name)
character_0.name = 'char_1'
print(character_0.name)
character_0.move(50, 100)
print(character_0.x_pos)
print(character_0.y_pos)


# subclasses, superclasses, inheritance
class PlayerCharacter(GameCharacter):

    speed = 10

    def __init__(self, name, x_pos, y_pos):
        super().__init__(name, 100, 100, x_pos, y_pos)

    def move(self, by_y_amount):
        super().move(0, by_y_amount)


player_character = PlayerCharacter('Pchar', 100, 100)
print(player_character.name)
player_character.move(100)
print(player_character.x_pos)