#!/usr/bin/env python

import random
from sys import stdout

ALPHABET = ['O', 'L']
CHALLENGE_LEN = 15
RULE_MAX_LEFT = 4

class EmptyInputError(Exception):
	pass

def make_challenge(len):
	return ''.join([random.choice(ALPHABET) for _ in range(len)])

def make_rule(left_len, src):
	left = ''.join([random.choice(src) for _ in range(left_len)])
	right = ''.join([random.choice(ALPHABET) for _ in range(left_len-1)])
	return (left, right)

challenge = make_challenge(CHALLENGE_LEN)
rules = [make_rule((i % (RULE_MAX_LEFT)) + 1, challenge) for i in range(5)]
moves = 0
while len(challenge) > 0:
	print(challenge)
	print('^  ' * (int((len(challenge)+2) / 3)))
	for i in range(0, len(challenge), 3):
		stdout.write(str(i) + ' '*(2 if i < 10 else 1))
	print()
	for i in range(len(rules)):
		rule = rules[i]
		print('({}) {} | {}'.format(i+1, rule[0].ljust(RULE_MAX_LEFT), rule[1]))
	try:
		got = input().strip()
		if not got:
			print('EMPTY')
			raise EmptyInputError
		x = tuple(map(lambda x: int(x), got.split(',')))
		r_index = x[0]-1
		r = rules[r_index]
		rllen = len(r[0])
		sample = challenge[x[1]:x[1]+rllen]
		if sample == r[0]:
			print(challenge)
			challenge = (
				challenge[0:x[1]]
				+ r[1]
				+ challenge[x[1] + rllen:]
			)
			rules[r_index] = make_rule(rllen+1 if rllen != RULE_MAX_LEFT else 1, challenge)
		moves += 1
	except KeyboardInterrupt: exit(1)
	except EmptyInputError:
		challenge += random.choice(ALPHABET)
		moves += 1
	except (ValueError, IndexError):
		print("Parsing failed! Give input in form `M,N` for rule M at index N")
print("you won in {} moves! Your score is {}".format(moves, int()))