class Solution:
    def intToRoman(self, num: int) -> str:
        # symbol = ['M','D','C','L','X','V','I']
        # mapping = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M',\
        #           0:'0', 4:'IV', 9:'IX', 49:''}
        
        res = ""
        while num > 0:
            if num//1000 > 0:
                res += 'M'
                num -= 1000
            elif (num+100)//1000 > 0:
                res += 'CM'
                num %= 100
            elif num//500 > 0:
                res += 'D'
                num -= 500
            elif (num+100)//500 > 0:
                res += 'CD'
                num %= 100
            elif num//100 > 0:
                res += 'C'
                num -= 100
            elif (num+10)//100 > 0:
                res += 'XC'
                num %= 10
            elif num//50 > 0:
                res += 'L'
                num -= 50
            elif (num+10)//50 > 0:
                res += 'XL'
                num %= 10
            elif num//10 > 0:
                res += 'X'
                num -= 10
            elif (num+1)//10 > 0:
                res += 'IX'
                num %= 1
            elif num//5 > 0:
                res += 'V'
                num -= 5
            elif (num+1)//5 > 0:
                res += 'IV'
                num %= 1
            else:
                res += 'I'
                num -= 1
        return res
                