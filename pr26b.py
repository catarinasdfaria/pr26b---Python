print("----Programa Calculadora----")
n1=float(input("Introduza o primeiro número:"))
n2=float(input("Introduza o segundo número:"))
print("1-Soma\n2-Subtração\n3-Divisão\n4-Multiplicação")
opc=int(input("Seleciona a opção:"))
match opc:
    case 1:
        print("A soma é:",round(n1+n2,1))
    case 2:
        print("A subtração é:",round(n1-n2,1))
    case 3:
        if n2==0:
            print("Não é possível dividir por 0")
        else:
            print("A divisão é:",round(n1/n2,1))
    case 4:
        print("A multiplicação é:",round(n1*n2,1))
    case _:
        print("Opção inválida")
print("----Fim----")
