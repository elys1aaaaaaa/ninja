
def num2word(number):
    ones_word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 

    teens_words = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    tens_word = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    word = " "

    if number > 99 or number < 0:
        print("Cannot...")
        return

    if (number < 10):
        return (ones_word[number])
    
    if (number >= 10 and number <= 19):
        return (teens_words[number-10])
    
    if (number >= 20 and number <= 99):
        d2 = number % 10
        d1 = int((number - d2)/10)
        return (tens_word[d1-2] + "-" +ones_word[d2])

 
a = 40
print (a)
print(num2word(a))
