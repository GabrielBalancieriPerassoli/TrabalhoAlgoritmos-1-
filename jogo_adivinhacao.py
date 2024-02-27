import random
random.seed(0)

lim_inf = 1
lim_sup = 100
dicas = 1
tentativa = 1

numero_sorteado = random.randint(lim_inf, lim_sup)

print("\nEste programa simula um jogo de adivinhação!")

while(True):

    if(lim_inf == lim_sup):
        print(f"\nEntão só restou {numero_sorteado}! Logo você esgotou suas chances!\n")
        break

    try:
        numero_digitado = int(input(f"\nQual é o seu chute? "))

    except ValueError:
        print("O valor digitado não é um número. Digite um número por favor.")
        continue
    
    if not((lim_inf <= numero_digitado) and (numero_digitado <= lim_sup)):
        print(f"Palpite inválido! Considere o Intervalo de [{lim_inf}, {lim_sup}]")
        continue

    if(numero_digitado > 0):

        if(numero_digitado == numero_sorteado):
            print(f"\nO número era {numero_sorteado}!")
            print(f"Você acertou na {tentativa} tentativa\n")

            jogar_novamente = input("Deseja jogar de novo? (S/N): ").upper()

            if(jogar_novamente == 'SIM' or jogar_novamente == 'S'):

                lim_inf = 1
                lim_sup = 100
                tentativa = 1
                dicas = 1
                numero_sorteado = random.randint(lim_inf, lim_sup)
                continue
            else:
                break

        elif(not(numero_digitado < lim_inf) and not(numero_digitado > lim_sup)):

            if(numero_digitado > numero_sorteado):
                lim_sup = numero_digitado - 1
                print(f"Errou!")
                if(tentativa % 2 == 0):
                    print(f"Dica número {dicas}: o número sorteado é menor que {numero_digitado}")
                    dicas += 1 
                tentativa += 1

            elif(numero_digitado < numero_sorteado):
                lim_inf = numero_digitado + 1
                print(f"Errou!")
                if(tentativa % 2 == 0):
                    print(f"Dica número {dicas}: o número sorteado é maior que {numero_digitado}")
                    dicas += 1
                tentativa += 1