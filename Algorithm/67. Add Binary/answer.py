class Solution(object):
    def convertBinarytoDecimal(self, num):
        square = len(num) - 1
        i = 0
        value = 0
        while i < len(num):
            value += int(num[i]) * (2 ** (square - i))
            i += 1
        return value

    def convertDecimaltoBinary(self, num):
        num = int(num)
        value = ""

        if num == 0:
            value = "0"
            return value

        while num > 0:
            value = str(num % 2) + value
            num = num // 2
    
        return value
        
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a = self.convertBinarytoDecimal(a)
        b = self.convertBinarytoDecimal(b)

        print(a + b)

        result = self.convertDecimaltoBinary(a + b)

        return result
        
# Alternate Solution
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """  
        a=int(a,2)
        b=int(b,2)
        sum=a+b
        return bin(sum)[2:]