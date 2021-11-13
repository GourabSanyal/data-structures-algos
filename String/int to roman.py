
def intToRom(num):
    if num > 3999:
        print("Number has to be lesser than 3999")
        return

    symbol = ["M", "CM", "D", "CD", "D", "XD",
              "L", "XL", "X", "IX", "V", "IV", "I"]
    value = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    roman = ''
    i = 0
    if num != 0:
        if value[i] <= num:
            roman += symbol[i]
            num = num - value[i]
    else:
        i = i + 1
    return num


num = 12
print(intToRom(num))
