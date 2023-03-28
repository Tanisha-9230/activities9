'''Problem 2:

Chit Chat Application - Function:

(a) In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friends.

Write a function that takes as input the,

message and checks whether the number of letters is less than 200 or above. If the length of the information is less than 200, the chat should be returned.


If the length of the chat is greater than 200, data consisting of only the first 200 characters should be returned.'''

def chat(message):
     if len(message)<200: 
        return message
     else:
        return message[:200]
print(chat("In few chit-chat programs, there is a limitation on the number of letters that you can send to your family and friendsWrite a function that takes as input the,message and checks whether the number of letters is less than 200 or above."))


'''(b) How one can check if the restriction is on a number of words rather than letters?
Write a function that allows a message with only 30 words'''

def word(message):
    total = len(message.split( ))
    if total > 30:
        print("Error:Invalid message, having more than 30 words")
    else:
        print("Valid message")
      
    return total
print(word("How one can check if the restriction is on a number of words rather than letters rite a function that allows a message with only 30 words, write a program of this problem"))




