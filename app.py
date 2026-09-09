from pessoas import Pessoa, Investigador, Suspeito, Testemunhas 
from depoimentos import Depoimentos


# lista_casos = []
# n = 1

# caso_da_lapa = Caso()

# while True:
#     alterar = int(input("\nMENU INVESTIGAÇÃO\n1 - Criar Caso\n2- Gerenciar Casos"))
#     if alterar == 1:
#         nome_do_caso = input("Digite o nome do caso: ")
#         nome_do_caso = Caso()
#         lista_casos.append(nome_do_caso)
#     elif alterar == 2:
#         escolher_caso = int(input(f"{lista_casos}\nDIGITE O NUMERO DO CASO, OS CASOS É NUMERADO EM ORDEM, COMEÇA DO 0. "))
#         print("\nCASO ACESSADO COM SUCESSO!")

#     alterar = int(input('''╔══════════════════════════════════════╗
#  ║          ECHO INVESTIGATION          ║
#  ╠══════════════════════════════════════╣
#  ║ 1. Gerenciar caso                    ║
#  ║ 2. Investigadores                    ║
#  ║ 3. Suspeitos                         ║
#  ║ 4. Testemunhas                       ║
#  ║ 5. Evidências                        ║
#  ║ 6. Depoimento                        ║
#  ║ 7. Linha do tempo                    ║
#  ║ 8. Analisar investigação             ║
#  ║ 9. Gerar relatório                   ║
#  ║ 0. Sair                              ║
#  ╚══════════════════════════════════════╝
#  '''))

#     alterar = int(input("\nMENU INVESTIGAÇÃO\n1 - Gerenciar caso\n2- Investigadores\n3 - Suspeitos\n4 - Testemunhas\n5 - Evidências\n6 - Depoimento\n"))

#     if alterar == 1: 
#         pass

#     elif alterar == 5:
#         pass

#     elif alterar == 6:
#         lista_casos[escolher_caso].get_depoimento()

#     elif alterar == 7:
#         escolha_linha_do_tempo = int(input("VOCE DESEJA ALTERAR OU VER A LINHA DO TEMPO? 1 - Alterar; 2 - Ver: "))
#         if escolha_linha_do_tempo == 1:
#             lista_casos[escolher_caso].set_linha_do_tempo()
#         elif escolha_linha_do_tempo == 2:
#             lista_casos[escolher_caso].get_linha_do_tempo()

#     elif alterar == 0:
#         print("MENU FECHADO!!!")
#         break

#     else:
#         print("Numero invalido.")

#     # if alterar == 1:
