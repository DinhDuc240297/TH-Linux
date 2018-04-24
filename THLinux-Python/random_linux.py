import random
x = random.randrange(0, 101, 2)
if x <= 30:
	print "Between 0 - 30"
elif x <= 60:
	print "Between 31 - 60"
elif x <= 90:
	print "Between 61 - 90"
else:
	print "game over"

