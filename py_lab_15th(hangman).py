import random
word_list=["cat","dog","bird","tiger","lion","elephant","monkey","giraffe"]
guessed_letters=[]
guesses_left=6
word_to_guess=random.choice(word_list)
word_length=len(word_to_guess)
hidden_word=list("_"*word_length)
while guesses_left>0:
    print(f"\nYou have {guesses_left} guesses left!")
    print(f"The word is {''.join(hidden_word)}")
    print(f"You have guessed : {','.join(guessed_letters)}")
    guess=input("Enter a letter :").lower()
    if guess in word_to_guess:
        indices=[i for i, x in enumerate(word_to_guess) if x==guess]
        for index in indices:
            hidden_word[index]=guess
        if "_" not in hidden_word:
            print("\nCongraulations!!! You have found the word successfully")
