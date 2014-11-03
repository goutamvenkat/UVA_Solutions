class Node(object):
	def __init__(self, num):
		self.num = num
		self.pile = num
		self.above = None
		self.below = None

def return_to_initial(block):
	if not block: return
	return_to_initial(block.above)
	block.below.above = None
	block.below = None
	block.pile = block.num

def main():
	n = input()
	blocks = [Node(i) for i in xrange(n)]
	while True:
		string = raw_input()
		if string == 'quit': break
		command, a, com2, b = string.split()
		a = int(a)
		b = int(b)
		if a != b and blocks[a].pile != blocks[b].pile:
			if command == 'move':
				if com2 == 'onto': 
					move_onto(blocks[a], blocks[b])
				else:
					move_over(blocks[a], blocks[b])
			else:
				if com2 == 'onto':
					pile_onto(blocks[a], blocks[b])
				else:
					pile_over(blocks[a], blocks[b])


	print_blocks(blocks)

def move_onto(a, b):
	if a.below: a.below.above = None
	return_to_initial(a.above)
	return_to_initial(b.above)
	b.above = a
	a.pile = b.pile
	a.below = b

def move_over(a, b):
	if a.below: a.below.above = None
	while b.above: b = b.above
	return_to_initial(a.above)
	b.above = a
	a.pile = b.pile
	a.below = b

def pile_onto(a, b):
	if a.below: a.below.above = None
	return_to_initial(b.above)
	b.above = a
	a.below = b
	while a: 
		a.pile = b.pile
		a = a.above

def pile_over(a, b):
	if a.below: a.below.above = None
	while b.above: b = b.above
	b.above = a
	a.below = b
	while a: 
		a.pile = b.pile
		a = a.above

def print_blocks(blocks):
	for i in xrange(len(blocks)):
		print '{}:'.format(i),
		if not blocks[i].below:
			temp = blocks[i]
			while temp:
				print ' {}'.format(temp.num),
				temp = temp.above
		print

if __name__=='__main__':
	main()