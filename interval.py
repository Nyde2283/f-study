from math import inf

class Interval:
	def __init__(self, begin: int | float, end, exclude_values = []) -> None:
		assert (type(begin) in (int, float)) or begin == -inf
		assert (type(end) in (int, float)) or begin == inf
		assert begin <= end
		
		self.begin = begin
		self.end = end
		self.excludes = []
		for e in sorted(exclude_values):
			if (self.begin < e < self.end) and (e not in self.excludes):
				self.excludes.append(e)

	def __str__(self) -> str:
		result = f'[{self.begin} '
		for e in self.excludes:
			result += f'|{e}| '
		result += f'-> {self.end}]'
		return result

	def __contains__(self, other):
		return self.begin <= other <= self.end and (other not in self.excludes)

	def __add__(self, other):
		assert type(other) == Interval
		a = self.begin
		b = self.end
		c = other.begin
		d = other.end

		if (c > b) or (d < a):
			raise ValueError
		if a < c: a = c
		if b > d: b = d
		excludes = self.excludes + other.excludes

		return Interval(a, b, excludes)