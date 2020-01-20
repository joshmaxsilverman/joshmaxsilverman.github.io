wordsFile = "538Words.txt"

# Return sorted tuple of distinct letters in the word
def lettersIn(word):
  letters = list(set(word))
  letters.sort()
  return tuple(letters)

# Get list of bee-possible words
wordsList = []
with open(wordsFile,'r') as wordsFile:
  for word in wordsFile:
    word = word[:-1] # pare trainling newline character
    if len(word) >= 4 and len(set(word)) <=7 and not 's' in word:
      wordsList.append(word)

print ":hi"