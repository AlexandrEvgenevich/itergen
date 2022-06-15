nested_list = [['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None], ]


class Iterator:
	def __init__(self, x):
		self.list_1 = []
		for y in x:
			for z in y:
				if z not in self.list_1:
					self.list_1.append(z)

		self.a = self.list_1

	def __iter__(self):
		self.a = iter(self.list_1)
		self.stop_iter = 0
		return self

	def __next__(self):
		self.b = next(self.a)
		self.stop_iter += 1
		if self.stop_iter > len(self.list_1):
			raise StopIteration
		return self.b


for item in Iterator(nested_list):
	print(item)

flat_list = [item for item in Iterator(nested_list)]

print(flat_list)

nested_list = [['a', 'b', 'c'], ['d', 'e', 'f'], [1, 2, None], ]


def generator(x):
	list_1 = []
	for y in x:
		for z in y:
			if z not in list_1:
				list_1.append(z)
	yield from list_1


for item in generator(nested_list):
	print(item)
