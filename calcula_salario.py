nome = input("Qual é o seu nome: ")
salario = float(input("Qual é o seu salário: "))
ano = int(input("Quanto anos você trabalha nessa empresa? "))
novo_salario = salario + (salario * 3/100)
novo_salario1 = salario + (salario * 12.5/100)
novo_salario2 = salario + (salario * 20/100)
if ano <= 3:
    print(f"Seu novo salário reajustado em 3% será de {novo_salario:.2f} reais.")
elif ano >= 3 and ano <= 10:
    print(f"Seu novo salário reajustado em 12.5% será de {novo_salario1:.2f} reais.")
elif ano > 10:
    print(f"Seu novo salário reajustado em 20% será de {novo_salario2:.2f} reais.")
print("Fim do programa")
