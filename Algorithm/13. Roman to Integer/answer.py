class Solution(object):
    roman_number = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    def romanToInt(self, s):
        array_list = list(s)[::-1]
        result = 0
        last_value = 0

        for i in array_list :
            if(self.roman_number[i] < last_value) :
                result = result - self.roman_number[i]
            else:
                result = result + self.roman_number[i]

            last_value = self.roman_number[i]

        print(result)
        return result
        
        