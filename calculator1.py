num1 = int(input("digite o primeiro digito: "))
num2 = int(input("digite o segundo digito: "))
operacao = input("digite a operação: ")

match operacao:
    case '+':
        res = num1 + num2
    case '-':
        res = num1 - num2
    case '*':
        res = num1 * num2
    case '/':
        res = num1 / num2
    
print(f"sua resposta é: {res}") 