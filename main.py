import os
import shutil
import time
import sys

def organizar_pasta(diretorio):
    if not os.path.exists(diretorio):
        print("Diretório não encontrado...")
        return
    extensao = {
        "Imagens" : [".jpg", ".png", ".gif", ".webp"],
        "Documentos" : [".pdf", ".docx", ".txt"], 
        "Planilhas" : [".xlsx", ".csv"]
    } # Extensões salvas no dicionário // suportadas para organização

    for arquivo in os.listdir(diretorio):
        # _ serve para desconsiderar variável que o método retornaria da biblioteca
        _, ext = os.path.splitext(arquivo)
        for categoria, lista_ext in extensao.items():
            if ext in lista_ext:
                pasta_categoria = os.path.join(diretorio, categoria)
                os.makedirs(pasta_categoria, exist_ok=True)
                shutil.move(os.path.join(diretorio, arquivo), os.path.join(pasta_categoria, arquivo))
                print(f"Movido {arquivo} para categoria {categoria}")

def organizador_layout():
    while True:  # Loop até o usuário escolher uma opção válida
        print("\nAbrindo organizador...")
        time.sleep(2)
        print("-----------------------")
        print("ORGANIZADOR DE ARQUIVOS")
        print("-----------------------")
        print("1 - Organizar pasta de downloads")
        print("0 - Encerrar programa")
        print("")
        
        opcao = input("Escolha a opção desejada: ").strip() # strip ignora espaços desnecessários
        
        # Verifica se a entrada não foi vazia
        if opcao == "":
            print("Nenhuma opção digitada. Tente novamente.")
            continue  # Volta para o início do loop
        
        # Verifica se a opção é um número inteiro
        if not opcao.isdigit():
            print("Entrada inválida! Por favor, insira um número.")
            continue  # Volta para o início do loop
        
        opcao = int(opcao)
        
        # Verifica se a opção está entre 0 e 1
        if opcao == 1:
            print("\nOrganizando...")
            organizar_pasta(r"C:\Users\Seu-nome-de-usuario\Downloads") #####  MODIFIQUE O CAMINHO PARA O SEU COMPUTADOR AQUI  #####
            print("")
            print("Pasta organizada com sucesso!")
            time.sleep(2) # Congelar execução para usuario ler a tela
            print("\nEncerrando...")
            time.sleep(2)
            sys.exit()
        elif opcao == 0:
            print("\nEncerrando...")
            time.sleep(2)
            sys.exit()
        else:
            print("Opção inválida! Tente novamente.")
            continue  # Volta para o início do loop

organizador_layout()