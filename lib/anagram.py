# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()

#creates a list of letters in alphabetic order.
    def match(self, word_list):
        sorted_word = sorted(self.word)

#loop through all words in the given list
        matches = []
        for candidate in word_list:
            if candidate.lower() != self.word and sorted(candidate.lower()) == sorted_word:
                matches.append(candidate)

        return matches

anagram = Anagram("listen")
#list 
print(anagram.match(["enlist", "google", "inlets", "banana"]))
        

        


