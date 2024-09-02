# def guessing_game():
#     secret =int(input("What is your secret number?"))
#     guess = None 
#     too_low = 0
#     too_high = 101 

#     while secret != guess:
#         guess = int((too_high + too_low) / 2)
#         print(f"Too low = {too_low}, Too high = {too_high}, guess = {guess}")

#         if guess > secret:
#             too_high = guess 
#         elif guess < secret:
#             too_low = guess 

# guessing_game() 

def is_palindrome():
    word = input("What is your word?: ")
    start = 0
    end = len(word)- 1
    while start != end:
        if word[start] == word[end]:
            start += 1
            end -= 1
        else:
            print("Not a palindrome!") 
            break  
    if start == end:
        print ("This is a palindrome!")  


is_palindrome() 