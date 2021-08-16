## 1. write the following functions
## 2. write a unittest class to test each of these functions once
## 3. Run it in this script

## Raising errors is more common when developing ------------------------

## These functions all take a single string as an argument.
## Presumably your code won't work for an int
## raise a built-in (or custom!) exception if fed an int


## make all characters capitalized
def shout(txt):
    try:
        txt.upper()
    except:
        raise TypeError(str.upper("This ain't a string"))
    return txt.upper()

## reverse all characters in string
def reverse(txt):
    try:
        txt[::-1]
        return txt[::-1]
    except:
        raise TypeError(str.upper("This ain't a string"))


## reverse word order in string
def reversewords(txt):
    words = txt.split()
    words.reverse()
    return flipped


## reverses letters in each word
def reversewordletters(txt):
    words = txt.split(" ")
    for word in words:
        reverse(word)
    



## Try/catch is more common when using
## someone else's code, scraping, etc. -----------------------------------

## Loop over this string and apply the reverse() function.
## Should throw errors if your exceptions are being raised!
## Write a try/catch to handle this.
 
string_list = ["hi", "hello there", 5, "hope this works", 100, "will it?"]

new_list = []
for string in string_list:
    try:
        new_list.append(reverse(string))
    except:
        if TypeError:
            new_list.append("not a string")
    

		
			
			
			
			
			
			

