#Emma Collins              10/23/23
#COM S 127 Section F

#word_replaccement = wordSwap
#

import random


def wordSwap(sentence):
    words = sentence.split()
    word_swap = {}
    unique_words = set()

    for word in words:
        if word not in unique_words:
            unique_words.add(word) 
            swap_word = random.choice(words)
            word_swap[word] = swap_word
    
    return word_swap

            
def main():
    sentence = input("Enter a sentance: ")
    word_swap = wordSwap(sentence)

    print("Word Replacement:")
    for key, value in word_swap.items():
        print(f" '{key}': '{value}'")

    words = sentence.split()
    new_sentence = " ".join(word_swap.get(word,word) for word in words)

    print("New Sentence:")
    print(new_sentence)

if __name__=="__main__":
    main()





   