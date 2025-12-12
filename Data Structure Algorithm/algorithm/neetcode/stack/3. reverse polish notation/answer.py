class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers = []

        for i in tokens:
                if i == "+":
                    first = numbers.pop()
                    second = numbers.pop()
                    numbers.append(second + first)
                elif i == "-":
                    first = numbers.pop()
                    second = numbers.pop()
                    numbers.append(second - first)
                elif i == "*":
                    first = numbers.pop()
                    second = numbers.pop()
                    numbers.append(second * first)
                elif i == "/":
                    first = numbers.pop()
                    second = numbers.pop()
                    numbers.append(int(second / first))
                else:
                    numbers.append(int(i))
            
        return numbers.pop()