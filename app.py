from utils import *
import sys

while True: #Loop principal do jogo
  if len(sys.argv) == 1: #Condicional para quando o arquivo é chamado sem o arquivo .txt, escolhendo o modo jxj
    while True:
      while True:
        jogo = inicializar_tabuleiro()
        exibir_jogo(jogo)
        jogador = input("Qual jogador vai iniciar\no de cima\n@ de baixo\n")
        if jogador == "o" or jogador == "O": # tirar o 'O' pq só se começa com 'o'
          while True:
            continuidade = jogada_disponivel_cima(jogo)
            if continuidade == False:
              print("O jogador de baixo é o vencedor!!!")
              break
            exibir_jogo(jogo)
            while True:
              verificar_se_dama()
              exibir_jogo(jogo)
              while True:
                x = input("Vez do jogador cima\nQual vai ser a sua jogada?\nUtilize o formato <COLUNA_INICIAL><LINHA_INICIAL>--<COLUNA_FINAL><LINHA_FINAL>\n")
                ci, li, cf, lf = decifrar_jogadas(x)
                validador, jogo, comeu = validar_jogadas_cima(ci, li, cf, lf)
                if validador == True:
                  break
              while True:
                if comeu == 1:
                  break
                if comeu != 1:
                  jogo[li][ci] =  jogo[lf][cf]
                  jogo[lf][cf] = " "
                  verificador = peca_pra_comer_obrigatoriamente_cima(ci, li, cf, lf)
                  if verificador == False:
                    jogo[lf][cf] = jogo[li][ci]
                    jogo[li][ci] = " "
                    break
                  while True:
                    x = input("Vez do jogador cima\nQual vai ser a sua jogada?\nUtilize o formato <COLUNA_INICIAL><LINHA_INICIAL>--<COLUNA_FINAL><LINHA_FINAL>\n")
                    ci, li, cf, lf = decifrar_jogadas(x)
                    validador, jogo, comeu = validar_jogadas_cima(ci, li, cf, lf)
                    if validador == True:
                      break
                    if comeu == 1:
                      break
                    jogo[li][ci] = jogo[lf][cf]
                    jogo[lf][cf] = " "
              if comeu == 0:
                break
            verificar_se_dama()
            continuidade = jogada_disponivel_baixo(jogo)
            if continuidade == False:
              print("O jogador de cima é o vencedor!!!")
              break
            exibir_jogo(jogo)
            while True:
              verificar_se_dama()
              exibir_jogo(jogo)
              while True:
                x = input("Vez do jogador baixo\nQual vai ser a sua jogada?\nUtilize o formato <COLUNA_INICIAL><LINHA_INICIAL>--<COLUNA_FINAL><LINHA_FINAL>\n")
                ci, li, cf, lf = decifrar_jogadas(x)
                validador, jogo, comeu = validar_jogadas_baixo(ci, li, cf, lf)
                if validador == True:
                  break
              while True:
                if comeu == 1:
                  break
                if comeu != 1:
                  jogo[li][ci] =  jogo[lf][cf]
                  jogo[lf][cf] = " "
                  verificador = peca_pra_comer_obrigatoriamente_baixo(ci, li, cf, lf)
                  if verificador == False:
                    jogo[lf][cf] = jogo[li][ci]
                    jogo[li][ci] = " "
                    break
                  while True:
                    x = input("Vez do jogador baixo\nQual vai ser a sua jogada?\nUtilize o formato <COLUNA_INICIAL><LINHA_INICIAL>--<COLUNA_FINAL><LINHA_FINAL>\n")
                    ci, li, cf, lf = decifrar_jogadas(x)
                    validador, jogo, comeu = validar_jogadas_baixo(ci, li, cf, lf)
                    if validador == True:
                      break
                    if comeu == 1:
                      break
                    jogo[li][ci] = jogo[lf][cf]
                    jogo[lf][cf] = " "
              if comeu == 0:
                break
            verificar_se_dama()

        elif jogador == "@":
          while True:
            continuidade = jogada_disponivel_baixo(jogo)
            if continuidade == False:
              print("O jogador de cima é o vencedor!!!")
              break
            exibir_jogo(jogo)
            while True:
              verificar_se_dama()
              exibir_jogo(jogo)
              while True:
                x = input("Vez do jogador de baixo\nQual vai ser a sua jogada?\nUtilize o formato <COLUNA_INICIAL><LINHA_INICIAL>--<COLUNA_FINAL><LINHA_FINAL>\n")
                ci, li, cf, lf = decifrar_jogadas(x)
                validador, jogo, comeu = validar_jogadas_baixo(ci, li, cf, lf)
                if validador == True:
                  break
              while True:
                if comeu == 1:
                  break
                if comeu != 1:
                  jogo[li][ci] = jogo[lf][cf]
                  jogo[lf][cf] = " "
                  verificador = peca_pra_comer_obrigatoriamente_baixo(ci, li, cf, lf)
                  if verificador == False:
                    jogo[lf][cf] = jogo[li][ci]
                    jogo[li][ci] = " "
                    break
                  while True:
                    x = input("Vez do jogador de baixo\nQual vai ser a sua jogada?\nUtilize o formato <COLUNA_INICIAL><LINHA_INICIAL>--<COLUNA_FINAL><LINHA_FINAL>\n")
                    ci, li, cf, lf = decifrar_jogadas(x)
                    validador, jogo, comeu = validar_jogadas_baixo(ci, li, cf, lf)
                    if validador == True:
                      break
                    if comeu == 1:
                      break
                    jogo[li][ci] = jogo[lf][cf]
                    jogo[lf][cf] = " "
              if comeu == 0:
                break
            verificar_se_dama()
            continuidade = jogada_disponivel_cima(jogo)
            if continuidade == False:
              print("O jogador de cima é o vencedor!!!")
              break
            exibir_jogo(jogo)
            while True:
              verificar_se_dama()
              exibir_jogo(jogo)
              while True:
                x = input("Vez do jogador de cima\nQual vai ser a sua jogada?\nUtilize o formato <COLUNA_INICIAL><LINHA_INICIAL>--<COLUNA_FINAL><LINHA_FINAL>\n")
                ci, li, cf, lf = decifrar_jogadas(x)
                validador, jogo, comeu = validar_jogadas_cima(ci, li, cf, lf)
                if validador == True:
                  break
              while True:
                if comeu == 1:
                  break
                if comeu != 1:
                  jogo[li][ci] = jogo[lf][cf]
                  jogo[lf][cf] = " "
                  verificador = peca_pra_comer_obrigatoriamente_cima(ci, li, cf, lf)
                  if verificador == False:
                    jogo[lf][cf] = jogo[li][ci]
                    jogo[li][ci] = " "
                    break
                  while True:
                    x = input("Vez do jogador de cima\nQual vai ser a sua jogada?\nUtilize o formato <COLUNA_INICIAL><LINHA_INICIAL>--<COLUNA_FINAL><LINHA_FINAL>\n")
                    ci, li, cf, lf = decifrar_jogadas(x)
                    validador, jogo, comeu = validar_jogadas_cima(ci, li, cf, lf)
                    if validador == True:
                      break
                    if comeu == 1:
                      break
                    jogo[li][ci] = jogo[lf][cf]
                    jogo[lf][cf] = " "
              if comeu == 0:
                break
            verificar_se_dama()

          testador = input("Você deseja reiniciar o jogo?\nDigite S para reiniciar e N para encerrar")
          if testador == "n" or testador == "N":
            break

  elif len(sys.argv) == 2: #Condicional para quando o arquivo é chamado com um arquivo .txt, escolhendo o modo computador
    linha = 0
    comidas_c = 0
    comidas_b = 0
    arquivo = open(sys.argv[1], "r")
    linhas = arquivo.readlines()
    arquivo.close()
    jogo = inicializar_tabuleiro()
    if linhas[0] == "C\n":
      exibir_jogo(jogo)
      while True:
        linha += 1
        if linhas[linha] == "\n":
          exibir_jogo(jogo)
          print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
          exit()
        continuidade = jogada_disponivel_cima(jogo)
        if continuidade == False:
          exibir_jogo(jogo)
          print("“O vencedor é o usuário de BAIXO.”")
          break
        while True:
          verificar_se_dama()
          while True:
            if linhas[linha] == "\n":
              exibir_jogo(jogo)
              print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
              exit()
            x = linhas[linha]
            ci, li, cf, lf = decifrar_jogadas(x)
            validador, jogo, comeu = validar_jogadas_cima(ci, li, cf, lf)
            if validador == True:
              break
            print("Existe um erro na linha %d" %(linha+1))
            linha += 1
          while True:
            if linhas[linha] == "\n":
              exibir_jogo(jogo)
              print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
              exit()
            if comeu == 1:
              comidas_c += 1
              break
            if comeu != 1:
              jogo[li][ci] = jogo[lf][cf]
              jogo[lf][cf] = " "
              verificador = peca_pra_comer_obrigatoriamente_cima(ci, li, cf, lf)
              if verificador == False:
                jogo[lf][cf] = jogo[li][ci]
                jogo[li][ci] = " "
                break
              print("Existe um erro na linha %d" %(linha+1))
              while True:
                linha += 1
                if linhas[linha] == "\n":
                  exibir_jogo(jogo)
                  print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
                  exit()
                x = linhas[linha]
                ci, li, cf, lf = decifrar_jogadas(x)
                validador, jogo, comeu = validar_jogadas_cima(ci, li, cf, lf)
                if validador == True:
                  break
                if comeu == 1:
                  comidas_c += 1
                  break
                jogo[li][ci] = jogo[lf][cf]
                jogo[lf][cf] = " "
                print("Existe um erro na linha %d" %(linha+1))
          if comeu == 0:
            break
          linha += 1

        continuidade = jogada_disponivel_baixo(jogo)
        if continuidade == False:
          exibir_jogo(jogo)
          print("O vencedor é o usuário de CIMA.")
          break
        while True:
          linha += 1
          verificar_se_dama()
          while True:
            if linhas[linha] == "\n":
              exibir_jogo(jogo)
              print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
              exit()
            x = linhas[linha]
            ci, li, cf, lf = decifrar_jogadas(x)
            validador, jogo, comeu = validar_jogadas_baixo(ci, li, cf, lf)
            if validador == True:
              break
            print("Existe um erro na linha %d" %(linha+1))
            linha += 1
          while True:
            if linhas[linha] == "\n":
              exibir_jogo(jogo)
              print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
              exit()
            if comeu == 1:
              comidas_b += 1
              break
            if comeu != 1:
              jogo[li][ci] = jogo[lf][cf]
              jogo[lf][cf] = " "
              verificador = peca_pra_comer_obrigatoriamente_baixo(ci, li, cf, lf)
              if verificador == False:
                jogo[lf][cf] = jogo[li][ci]
                jogo[li][ci] = " "
                break
              print("Existe um erro na linha %d" %(linha+1))
              while True:
                linha += 1
                if linhas[linha] == "\n":
                  exibir_jogo(jogo)
                  print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
                  exit()
                x = linhas[linha]
                ci, li, cf, lf = decifrar_jogadas(x)
                validador, jogo, comeu = validar_jogadas_baixo(ci, li, cf, lf)
                if validador == True:
                  break
                if comeu == 1:
                  comidas_b += 1
                  break
                jogo[li][ci] = jogo[lf][cf]
                jogo[lf][cf] = " "
                print("Existe um erro na linha %d" %(linha+1))
          if comeu == 0:
            break

    elif linhas[0] == "B\n" :
      while True:
        linha += 1
        if linhas[linha] == "\n":
          exibir_jogo(jogo)
          print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
          exit()
        continuidade = jogada_disponivel_baixo(jogo)
        if continuidade == False:
          exibir_jogo(jogo)
          print("“O vencedor é o usuário de CIMA.”")
          break
        while True:
          verificar_se_dama()
          while True:
            if linhas[linha] == "\n":
              exibir_jogo(jogo)
              print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
              exit()
            x = linhas[linha]
            ci, li, cf, lf = decifrar_jogadas(x)
            validador, jogo, comeu = validar_jogadas_baixo(ci, li, cf, lf)
            if validador == True:
              break
            print("Existe um erro na linha %d" %(linha+1))
            linha += 1
          while True:
            if linhas[linha] == "\n":
              exibir_jogo(jogo)
              print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
              exit()
            if comeu == 1:
              comidas_b += 1
              break
            if comeu != 1:
              jogo[li][ci] = jogo[lf][cf]
              jogo[lf][cf] = " "
              verificador = peca_pra_comer_obrigatoriamente_baixo(ci, li, cf, lf)
              if verificador == False:
                jogo[lf][cf] = jogo[li][ci]
                jogo[li][ci] = " "
                break

              print("Existe um erro na linha %d" %(linha+1))
              while True:
                linha += 1
                if linhas[linha] == "\n":
                  exibir_jogo(jogo)
                  print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
                  exit()
                x = linhas[linha]
                ci, li, cf, lf = decifrar_jogadas(x)
                validador, jogo, comeu = validar_jogadas_baixo(ci, li, cf, lf)
                if validador == True:
                  break
                if comeu == 1:
                  comidas_b += 1
                  break
                jogo[li][ci] = jogo[lf][cf]
                jogo[lf][cf] = " "
                print("Existe um erro na linha %d" %(linha+1))
          if comeu == 0:
            break
          linha += 1

        continuidade = jogada_disponivel_cima(jogo)
        if continuidade == False:
          exibir_jogo(jogo)
          print("O vencedor é o usuário de BAIXO.")
          break
        while True:
          linha += 1
          verificar_se_dama()
          while True:
            if linhas[linha] == "\n":
              exibir_jogo(jogo)
              print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
              exit()
            x = linhas[linha]
            ci, li, cf, lf = decifrar_jogadas(x)
            validador, jogo, comeu = validar_jogadas_cima(ci, li, cf, lf)
            if validador == True:
              break
            print("Existe um erro na linha %d" %(linha+1))
            linha += 1
          while True:
            if linhas[linha] == "\n":
              exibir_jogo(jogo)
              print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
              exit()
            if comeu == 1:
              comidas_c += 1
              break
            if comeu != 1:
              jogo[li][ci] = jogo[lf][cf]
              jogo[lf][cf] = " "
              verificador = peca_pra_comer_obrigatoriamente_cima(ci, li, cf, lf)
              if verificador == False:
                jogo[lf][cf] = jogo[li][ci]
                jogo[li][ci] = " "
                break
              jogo[li][ci] =  jogo[lf][cf]
              jogo[lf][cf] = " "
              print("Existe um erro na linha %d" %(linha+1))
              while True:
                linha += 1
                if linhas[linha] == "\n":
                  exibir_jogo(jogo)
                  print("Cima = <%d> / Baixo = <%d>" %(comidas_c, comidas_b))
                  exit()
                x = linhas[linha]
                ci, li, cf, lf = decifrar_jogadas(x)
                validador, jogo, comeu = validar_jogadas_cima(ci, li, cf, lf)
                if validador == True:
                  break
                if comeu == 1:
                  comidas_c += 1
                  break
                jogo[li][ci] = jogo[lf][cf]
                jogo[lf][cf] = " "
                print("Existe um erro na linha %d" %(linha+1))
          if comeu == 0:
            break