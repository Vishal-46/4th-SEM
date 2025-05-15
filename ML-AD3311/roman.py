class IntegerToRoman:
    def __init__(self, number):
        self.number = number

    def to_roman(self):
        val = [
            1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1
        ]
        syms = ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"
        ]
        num = self.number
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // val[i]):
                roman_num += syms[i]
                num -= val[i]
            i += 1
        return roman_num
num = int(input("Enter an integer: "))
converter = IntegerToRoman(num)
print(f"Roman numeral: {converter.to_roman()}")
