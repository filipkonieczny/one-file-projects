#!/usr/bin/env python


# this program removes vowels from a given sentence


# variables
vowels = ["a", "e", "i", "o", "u", "y"]


# main
print("\nThis program removes vowels from a given sentence. Enjoy.\n\n")


while True:
	without_vowels = ""

	sentence = raw_input("Remove vowels from this sentence: ")


	# remove vowels
	for letter in sentence:
		if letter.lower() not in vowels:
			without_vowels += letter


	# print the result
	print("\nSentence before: %s" % sentence)
	print("Sentence after: %s" % without_vowels)


	# ask the user if he wants to do this again
	again = raw_input("\nWould you like to go again?(y/n): ")
	again = again.lower()

	while again != "y" and again != "n":
		print("\nPlease decide \"y\" or \"n\".")

		again = raw_input("Would you like to go again?(y/n): ")
		again = again.lower()


	if again == "n":
		break

	else:
		print("\nLet's do this!!\n\n")


print("\n\nKILL ALL VOWELS\n\n")