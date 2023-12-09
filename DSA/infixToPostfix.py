# code to convert infix expression to postfix expression

# define stack and take input from user

stack = []

expression = input('enter the infix expression : ')
x = expression.replace(" ", "")
y = x.upper()

for i in y:
    stack.append(i)

print('expression entered : {}'.format(y))
print('stack formed : {}'.format(stack))

# infix to postfix processing

operandStack = []
operatorStack = []

postfixString = ''

operator_precedence = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2,
    '^' : 3
}

for i in stack:
    if i.isalpha():
        postfixString = postfixString + i
        
print('equivalent postfix expression : {}'.format(postfixString))