from main import Main

main = Main()

main.mostrar_menu()

while main.em_execucao == True:
    main.mostrar_menu()
    main.ler_opcao_menu()
