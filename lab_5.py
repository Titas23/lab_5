

"""
The program is going to translate a sentence captured as user input. 
We first read in the text file textese.txt
then from the text file we create a list of strings from each lines in the text file. 
Then create a dictionary from the list. 
Once the text file has been read into memory, we close the file. 


We then define a function for translating which involves splitting the user input (Sentence)
    into an array of strings("enjoy the excellent band tonight") ["enjoy", "the", "excellent", "band", "tonight"]

once we have the array of strings representing the user's input sentence, we loop through each words, find the key matching the word 
    and returns back the value tied to word in our dictionary. 

Print out the translated sentence to the user. 
"""

"""

main():
    set sentence = input()
    set dictionary = create_dictionary()
    translate(sentence, dictionary)

translate():
    words = for each of the word in the sentence
    for each words, translate the word
    print trasnlated sentence to user


create_dictionary():
    read in text file textese.txt
    create a list = each line from file
    close the file
    create a dictionary off of the list
    return the dictionary

main()

"""