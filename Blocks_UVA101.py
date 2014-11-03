class Node(object):
	def __init__(self, num):
		self.num = num
		self.pile = num
def main():
	n = input()
	blocks = dict((i, [Node(i)]) for i in xrange(n))
	while True:
		string = raw_input()
		if string == 'quit': break
		command, com2, a, b = string.split()
		if a != b:
			pile_a = blocks[Node(a).pile]
			pile_b = blocks[Node(b).pile]
			if command == 'move':
				if com2 == 'onto': 
					move_onto(pile_a, pile_b, blocks)
				else:
					move_over(pile_a, pile_b, blocks)

	print_blocks(n, blocks)

def move_onto(pile_a, pile_b, blocks):
	moving_blocks_a = pile_a[pile_a.index(Node(a)) + 1:]
	moving_blocks_b = pile_b[pile_b.index(Node(b)) + 1:]
	if moving_blocks_a:
		for i in moving_blocks_a:

def print_blocks(n, blocks):
	for i in xrange(n):
		print '{}: {}\n'.format(i, printList(blocks[i]))

def printList(lst):
	s = ''
	if not lst:
		return 
	for i in lst:
		s += (str(i.num) + ' ')
	return s[:-2]

if __name__=='__main__':
	main()