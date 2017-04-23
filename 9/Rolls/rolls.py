from random import randint

class Die(object):
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        print("Your side is " + str(randint(1, self.sides)))


six_cube = Die()
attempt = 10

while attempt != 0:
    six_cube.roll_die()
    attempt -= 1

print("\nNow you roll ten cube:")
attempt = 10
ten_cube = Die(10)
while attempt != 0:
    ten_cube.roll_die()
    attempt -= 1

print("\nNow you roll twenty cube:")
attempt = 10
ten_cube = Die(20)
while attempt != 0:
    ten_cube.roll_die()
    attempt -= 1
