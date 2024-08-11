def sort_sentence_alphabetically(sentence):

	#Split the sentence into words
 	words = sentence.split()

	# Sort the words alphabetically
 	sorted_words = sorted(words)

 	# Join the sorted words to form the sorted sentence
 	sorted_sentence = ' '.join(sorted_words)

 	return sorted_sentence

# Example usage

input_sentence = "This is a sample sentence to be sorted alphabetically."
result = sort_sentence_alphabetically(input_sentence)
print("Original Sentence:", input_sentence)
print("Sentence after sorting alphabetically:", result)
