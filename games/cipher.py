alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

message = input("Ange meddelande:	")

encrypted = ''

for letter in message:
	encrypted = encrypted + alphabet[alphabet.index(letter) + 1]

print("Encrypted: ", encrypted)