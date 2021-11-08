# def the sentance
def reverse(sentance):
    # split the sentacne by space
    splitted = sentance.split(' ')
    # reverse and join by space
    reversed_sentance = ' '.join(reversed(splitted))
    # return the object
    return reversed_sentance


if __name__ == "__main__":
    input = "I am a developer"
    print(reverse(input))
