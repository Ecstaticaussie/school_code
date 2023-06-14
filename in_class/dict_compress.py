from math import log2, ceil

remove_chars = ",.?/:;!&()".strip()
text = "".join([char for char in [*"What a start to this game. Belief from Morocco that they can take the game to Croatia. This is constant pressure from Morocco!"] if char not in ",.?/:;!&()"])

number_of_chars = len(text)
text_list = text.split()
unique_words = len(set(text_list))
print(unique_words)

uncompressed_size = number_of_chars * 16
compressed_size = unique_words * ceil(log2(unique_words))

print(f"Uncompressed size: {uncompressed_size} bits")
print(f"Compressed size: {compressed_size} bits")