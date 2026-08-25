def menu():
    while True:
        print("\n--- MENU DE OPÇÕES ---")
        print("1. Exibir números de 1 a 10")
        print("2. Exibir números pares de 1 a 20")
        print("3. Exibir tabuada")
        print("4. Sair")

        opcao = input("Escolha uma opção (1-4): ")

        if opcao == "1":
            print("\nNúmeros de 1 a 10:")
            for i in range(1, 11):
                print(i, end=" ")
            print()

        elif opcao == "2":
            print("\nNúmeros pares de 1 a 20:")
            for i in range(1, 21):
                if i % 2 == 0:
                    print(i, end=" ")
            print()

        elif opcao == "3":
            num = int(input("\nDigite um número para ver a tabuada: "))
            print(f"Tabuada do {num}:")
            for i in range(1, 11):
                print(f"{num} x {i} = {num * i}")

        elif opcao == "4":
            print("\nSaindo do programa... Até mais!")
            break
        else:
            print("\nOpção inválida! Tente novamente.")

menu()