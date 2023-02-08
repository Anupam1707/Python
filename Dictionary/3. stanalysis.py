#To read a sentence and then create a dictionary contains the frequency of
#letters and digits in the sentence. Ignore other symbols, if any.
#8/2/23
#stananalysis.py
#By Anupam Kanoongo

def freqdict(sentence):
    
    frequency = {}
    for char in sentence:
        
        if char.isdigit() or char.isalpha():
            frequency[char] = frequency.get(char, 0) + 1
            
    return frequency

sentence = input("Enter a sentence: ")

print("Frequency of letters and digits:", freqdict(sentence))
