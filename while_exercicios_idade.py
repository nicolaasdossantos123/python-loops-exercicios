idade = 0

while idade != -1:
    idade = int(input("Digite sua idade (-1 para sair): "))

    if idade == -1:
     print("Programa encerrado")
    elif idade < 18:
       print("Menor de idade")
    elif idade > 18:
       print("Maior de idade")
    else:
       print("Idoso")
