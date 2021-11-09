
def intToRom(num):
    if num > 3999:
        print("Number has to be lesser than 3999")
        return

    symbol = ["M", "CM", "D", "CD", "D", "XD",
              "L", "XL", "X", "IX", "V", "IV", "I"]
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman = 0
    i = 0
    while num > 0:
        # division - set it to div
        div = num // value[i]
        # moduler - set it to num
        num = num % value[i]

        while div:
            # add the div to the roman
            roman = roman + symbol[i]
            # decrease the div by 1
            div = div - 1
        # increase the index by 1
        i = i + 1
        return num


num = 12
print(intToRom(num))
