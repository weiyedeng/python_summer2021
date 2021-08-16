## Write a function that counts how many vowels are in a word
## Raise a TypeError with an informative message if 'word' is passed as an integer
## When done, run the test in your script and see your results


def count_vowels(word):
    lowervowels = ['a','e','i','o','u']
    temp = 0
    try:
        word = word.lower()
        for i in range(0,len(word)):
            if word[i] in lowervowels:
                temp += 1
        return temp
    except: 
        raise TypeError("It's a word! It should not be passed as an integer!")

count_vowels("Amaan")    


