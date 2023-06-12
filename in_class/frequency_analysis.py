from collections import Counter

top_5_letters = {"e":12.49, "t":9.28, "a":8.04, "o":7.64, "i":7.57}
cipher_text = input("Enter the cipher text: ").lower().strip()
total_chars = len(cipher_text)
reapeted_chars = Counter(cipher_text)

reapeted_chars_percent = {letter: reapeted_chars[letter]/total_chars*100 for letter in reapeted_chars}

sorted_repeated_chars = {key: val for key, val in sorted(reapeted_chars_percent.items(), key=lambda ele: ele[1], reverse=True)}

print(sorted_repeated_chars)