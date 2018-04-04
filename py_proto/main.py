import random

ALPHABET = ['a', 'b', 'c']
CHALLENGE_LEN = 15



def make_challenge(len = 10):
	return ''.join([random.choice(ALPHABET) for _ in range(len)])

def make_rule(left_len = 3):
	left = ''.join([random.choice(ALPHABET) for _ in range(left_len)])
	right = ''.join([random.choice(ALPHABET) for _ in range(random.randint(1, left_len-1))])
	return (left, right)

challenge = make_challenge(len=CHALLENGE_LEN)
mr = lambda : make_rule(left_len=random.randint(2,4)) 

rules = [mr() for _ in range(5)]
while True:
	print(challenge)
	print('^  ' * (int(len(challenge) / 3)))
	print(''.join([(str(i) if i%3==0 else ' ') for i in range(0, len(challenge))]))
	rules[random.randint(0, len(rules)-1)] = mr()
	for i in range(len(rules)):
		rule = rules[i]
		print('({}) {} --> \t {}'.format(i+1, rule[0], rule[1]))
	try:
		x = input().strip().split(',')
		x = map(lambda x: int(x), x)
		x = tuple(x)
		print(x,'')
		r = rules[x[0]-1]
		sample = challenge[x[1]:x[1]+len(r[0])]
		if sample == r[0]:
			print('success! applied rule!')
			challenge = challenge[0:x[1]] + r[1] + challenge[x[1] + len(r[0]):]
		print('sample {}'.format(sample))
	except KeyboardInterrupt:
		exit(1)
	except Exception as e:
		print(e)
		pass