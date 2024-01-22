class Conv:
    def __init__(self):
        self.val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4, 1
        ]

        self.syb = [
            'M', 'CM', 'D', 'CD',
            'C', 'XC', 'L', 'XL',
            'X', 'IX', 'V', 'IV',
            'I'
        ]

    def to_roman(self, num):
        result = []
        for value, symbol in zip(self.val, self.syb):
            while num // value != 0:
                num %= value
                result += [symbol]

        return "".join(result)


print('Converted:', Conv().to_roman(44))
