def jogar():
    opcoes = {1: 'pedra', 2: 'papel', 3: 'tesoura'}

    while True:
        while True:
            escolha_jogador1 = input("Jogador 1, escolha (1 - Pedra, 2 - Papel, 3 - Tesoura): ")

            if escolha_jogador1 not in ['1', '2', '3']:
                print("Opção inválida! Escolha entre 1, 2 ou 3.")
                continue

            escolha_jogador1 = int(escolha_jogador1)

            escolha_jogador2 = input("Jogador 2, escolha (1 - Pedra, 2 - Papel, 3 - Tesoura): ")

            if escolha_jogador2 not in ['1', '2', '3']:
                print("Opção inválida! Escolha entre 1, 2 ou 3.")
                continue

            escolha_jogador2 = int(escolha_jogador2)

            print(f"Jogador 1 escolheu: {opcoes[escolha_jogador1]}")
            print(f"Jogador 2 escolheu: {opcoes[escolha_jogador2]}")

            if escolha_jogador1 == escolha_jogador2:
                print("Empate!")
            elif (escolha_jogador1 == 1 and escolha_jogador2 == 3) or \
                 (escolha_jogador1 == 2 and escolha_jogador2 == 1) or \
                 (escolha_jogador1 == 3 and escolha_jogador2 == 2):
                print("Jogador 1 ganhou!")
            else:
                print("Jogador 2 ganhou!")


            while True:
                jogar_novamente = input("Querem jogar novamente? (Sim/Não): ").strip().lower()
                if jogar_novamente == 'sim':
                    break
                elif jogar_novamente == 'não' or jogar_novamente == 'nao':
                    print("Jogo encerrado!")
                    return
                else:
                    print("Resposta inválida! Por favor, digite 'Sim' ou 'Não'.")

jogar()
