from die import Die

dice = Die()
for i in range(10):
    dice.roll_die()

print()

dice = Die(10)
for i in range(10):
    dice.roll_die()

print()

dice = Die(20)
for i in range(10):
    dice.roll_die()
