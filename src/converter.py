"""
Converter integers for your text format.
"""

class Converter:

    low_numbers = [
        'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
        'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
        'dezesseis', 'dezessete','dezoito', 'dezenove'
    ]

    middle_numbers = [
        'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta',
        'oitenta', 'noventa'
    ]

    high_numbers = [
        'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos',
        'seicentos', 'setecentos', 'oitocentos', 'novecentos',
    ]

    negative_word = 'menos'

    def __init__(self, **kwargs):
        self.low_numbers = {k:v for k,v in zip(range(0, 20), self.low_numbers)}
        self.middle_numbers = {k:v for k,v in zip(range(2, 10), self.middle_numbers)}
        self.high_numbers = {k:v for k,v in zip(range(1, 10), self.high_numbers)}

    def translate_part(self, string, number):
        if number == 0: return ''
        if number == 100: return 'cem'
        if number < 20: return self.low_numbers[number]

        c = int(string[0])
        d = int(string[1])
        u = int(string[2])

        output = []

        if c != 0:
            output.append(self.high_numbers[c])
        if d != 0:
            output.append(self.middle_numbers[d])
            if u != 0:
                output.append(self.low_numbers[u])

        output = ' e '.join(output)
        return output

    def __split_string(self, string, length):
        return (string[0+i:length+i] for i in range(0, len(string), length))

    def translate(self, number):
        is_negative = False
        if number < 0:
            is_negative = True
            number = abs(number)

        self.validate(number)
        if number == 0: return 'zero'

        number = str(number)
        padding = 3 - len(number) % 3
        if padding < 3: number = '0' * padding + number

        parts = list(self.__split_string(number, 3))
        reversed(parts)

        output = ''
        if len(parts) == 2:
            hundreds_scale = self.translate_part(parts[0], int(parts[0]))
            thousands_scale = self.translate_part(parts[1], int(parts[1]))

            if thousands_scale != '':
                if hundreds_scale == 'um':
                    output =  f'mil e {thousands_scale}'
                else:
                    output =  f'{hundreds_scale} mil e {thousands_scale}'
            else:
                if hundreds_scale == 'um':
                    output =  f'mil'
                else:
                    output =  f'{hundreds_scale} mil'
        else:
            hundreds_scale = self.translate_part(parts[0], int(parts[0]))
            output = f'{hundreds_scale}'

        if is_negative:
            return f'{self.negative_word} {output}'
        return output

    def validate(self, number):
        if type(abs(number)) != int:
            raise Exception('Only integer numbers')
        if number < -99999 or number > 99999:
            raise Exception('Number out of range')
        return True
