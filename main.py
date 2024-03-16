from replit import db


def opcao1():
  print("Cadastro de Cliente")
  codigo = input("Digite o código do cliente: ")
  db['Clientes'][codigo] = {
      "codigo": codigo,
      "Nome": input("Nome:"),
      "Endereço": input("Endereço:"),
      "Cidade": input("Cidade:"),
      "Cep": input("Cep:"),
      "Telefone": input("Telefone:"),
  }


def opcao2():
  print("Mostrando clientes Cadastrados"),
  print(db['Clientes'])


def opcao3():
  print("Você escolheu a opção 3")


def opcao4():
  print("Você escolheu a opção 4")


def opcao5():
  print("Você escolheu a opção 5")


def finalizar():
  print("O aplicativo será finalizado")
  exit()


def exibir_menu():
  print("\nMenu:")
  print("1. Cadastrar Cliente")
  print("2. Mostrar Clientes")
  print("3. Opção 3")
  print("4. Opção 4")
  print("5. Opção 5")
  print("6. Sair")


while True:
  exibir_menu()
  escolha = input("Escolha uma opção: ")

  if escolha == '1':
    opcao1()
  elif escolha == '2':
    opcao2()
  elif escolha == '3':
    opcao3()
  elif escolha == '4':
    opcao4()
  elif escolha == '5':
    opcao5()
  elif escolha == '6':
    finalizar()
  else:
    print("Opção inválida. Por favor, escolha uma opção válida.")
