

def cryptic_sorter(strings: list[str]) -> list[str]:
	def test(x):
		return(len(x), x.lower(), x.isupper())
	return sorted(strings, key=test)

print(cryptic_sorter(["apple", "cat", "banana", "dog", "elephant"]))
print(cryptic_sorter(["aaa", "bbb", "AAA", "BBB"]))
print(cryptic_sorter(["hello", "world", "hi", "wo"]))
print(cryptic_sorter([]))
print(cryptic_sorter([""]))
