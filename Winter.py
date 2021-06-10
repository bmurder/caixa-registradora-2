import os 

def clear():
    print("\n" * 40)
fundo = '\033[1;104m'
negrito = '\033[;1m'
vermelho = '\033[1;31m'
branco = '\033[1;97m'
print(f'fundo: {fundo}')
os.system('clear')
while True:
    print(f'{vermelho}------ winter -------')
    n = 1
    total = 0
    print(f'{branco}')

    while True:
        preco = float(input("Produto {}: R$ ".format(n)))
        n += 1
        total += preco
        if preco == 0:
            break

    print("------------------------------------")

    print("Total: R$ {:.2f} ".format(total))
    dinheiro = float(input("Dinheiro: R$ "))
    print("Troco: R$ {:.2f}".format(dinheiro - total))

    print("------------------------------------")

    reset = input("pressione 0 para reset, 1 para encerrar: ")
    if reset == "0":
        clear()
        continue
    else:
        clear()
        print("Encerrando caixa...")
        break