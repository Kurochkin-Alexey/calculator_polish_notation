import math
import sys

class Mather:
    def __init__(self, expression):
        self.operation_priority = {
            '(': 0,
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
            '^': 3,
            '~': 4  # Унарный минус
        }
        self.infix_expr = expression
        self.postfix_expr = self.to_postfix(self.infix_expr + '\r')

    def get_string_number(self, expr, pos):
        str_number = ''
        while pos[0] < len(expr):
            num = expr[pos[0]]
            if num.isdigit() or num == '.':
                str_number += num
            else:
                pos[0] -= 1
                break
            pos[0] += 1
        return str_number
    
    def to_postfix(self, infix_expr):
        postfix_expr = ''
        stack = []

        i = 0
        while i < len(infix_expr):
            char = infix_expr[i]
            if char.isdigit():
                pos = [i]
                number = self.get_string_number(infix_expr, pos)
                postfix_expr += number + " "
                i = pos[0]
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix_expr += stack.pop()
                stack.pop()
            elif char in self.operation_priority:
                op = char
                if op == '-' and (i == 0 or (i > 1 and infix_expr[i-1] in self.operation_priority)):
                    op = '~'
                while stack and self.operation_priority[stack[-1]] >= self.operation_priority[op]:
                    postfix_expr += stack.pop()
                stack.append(op)
            i += 1

        while stack:
            postfix_expr += stack.pop()
        
        return postfix_expr
    
    def execute(self, op, first, second):
        if op == '+':
            operation = first + second
        elif op == '-':
            operation = first - second
        elif op == '*':
            operation = first * second
        elif op == '/':
            operation = first / second
        elif op == '^':
            operation = math.pow(first, second)
        return operation
    
    def calc(self):
        locals_stack = []
        i = 0
        while i < len(self.postfix_expr):
            char = self.postfix_expr[i]

            if char.isdigit():
                pos = [i]
                number = self.get_string_number(self.postfix_expr, pos)
                locals_stack.append(float(number))
                i = pos[0]
            elif char in self.operation_priority:
                if char == '~':
                    last = locals_stack.pop() if locals_stack else 0
                    locals_stack.append(self.execute('-', 0, last))
                    i += 1
                    continue

                second = locals_stack.pop() if locals_stack else 0
                first = locals_stack.pop() if locals_stack else 0
                if second == 0 and char == '/':
                    print("Деление на ноль")
                    return None

                locals_stack.append(self.execute(char, first, second))
            i += 1
        
        return locals_stack.pop() if locals_stack else 0

expression = sys.argv[1]
mather = Mather(expression)
result = mather.calc()
print(result)

# Проверка
# "15/(7-(1+1))*3-(2+(1+1))*15/(7-(200+1))*3-(2+(1+1))*(15/(7-(1+1))*3-(2+(1+1))+15/(7-(1+1))*3-(2+(1+1)))"
