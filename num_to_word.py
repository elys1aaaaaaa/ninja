

def num2word(number):
    ones_word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] 

    teens_words = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

    tens_word = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    hundreds_word = ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
    word = " "


    if number > 99 or number < 0:
        print("Cannot...")
        return

    if (number < 10):
        return (ones_word[number])
    
    if (number == 10 or number == 20 or number == 30 or number == 40 or number == 50 or number == 60 or number == 70 or number == 80 or number == 90):
        return (tens_word[number//10-1])
    
    if (number >= 10 and number <= 19):
        return (teens_words[number-10])
    
    if (number >= 20 and number <= 99):
        d2 = number % 10
        d1 = int((number - d2)/10)
        return (tens_word[d1-2] + "-" +ones_word[d2])

def num3words(number):

    hundreds_word = ["one hundred", "two hundred", "three hundred", "four hundred", "five hundred", "six hundred", "seven hundred", "eight hundred", "nine hundred"]
    word = ""

    if (number < 99):
        return num2word(number)
    if (number >=100 and number <=999):
        d3 = number//100
        word = hundreds_word[d3-1]

    
    remainder = number - (d3*100)
    print (remainder)
    return word + " and " + num2word(remainder)

        


a = 97
print (a)
print(num3words(a))
