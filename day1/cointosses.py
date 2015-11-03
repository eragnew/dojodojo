import random

print 'Starting the program...'

heads, tails = 0, 0

for i in range(5000):
	toss = round(random.random())
	if toss == 1:
		result = 'head'
		heads += 1
	else:
		result = 'tail'
		tails += 1
	print 'Attempt #%d: Throwing a coin... It\'s a %s! Got %d head(s) so far and %d tail(s) so far' % (i, result, heads, tails)

print 'Ending the program, thank you!'