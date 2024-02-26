import string
#inicialização do tabuleiro(introdução de estruturas e de cálculos algébricos para colocação dos caracteres que formam o tabuleiro)
alfabeto = list(string.ascii_uppercase[:10])
def inicializar_tabuleiro():
  jogo = [[" " for i in range(23)] for j in range(23)]
  alfabeto = list(string.ascii_uppercase[:10])
  for i in range(23):
      for j in range(23):
          if i == 0 or i == 22:
              for j in range(2, 22, 2):
                  s = 0.5 * j -1
                  s = int(s)
                  jogo[i][j] = alfabeto[s]
          elif i % 2 == 1:
              for j in range (1, 23, 2):
                  jogo[i][j] = "+"
              for j in range(2, 22, 2):
                  jogo[i][j] = "-"
          elif i % 2 == 0:
              if i in range(2, 22, 2):
                  for j in range(1, 23, 2):
                      jogo[i][j] = "|"
              if i in range(4, 24, 4):
                  for j in range(4, 24, 4):
                      jogo[i][j] = "#"
              if i in range(2, 22, 4):
                  for j in range(2, 22, 4):
                      jogo[i][j] = "#"
              if i in range(2, 22, 2):
                  for j in range(0, 44, 22):
                      jogo[i][j] = int(i * 0.5 -1)
              if i == 2 or i == 6:
                  for j in range(4, 24, 4):
                      jogo[i][j] = "o"
              if i == 4:
                  for j in range(2, 22, 4):
                      jogo[i][j] = "o"
              if i == 16 or i == 20:
                  for j in range(2, 22,4):
                      jogo[i][j] = "@"
              if i == 18:
                  for j in range(4, 24, 4):
                      jogo[i][j] = "@"
  return jogo
def exibir_jogo(jogo): #Função para exibição do tabuleiro(substituir os caracteres por espaços vazios)
  for i in range(23):
    temp = str(jogo[i])
    temp = temp.replace("'", "")
    temp = temp.replace("]", "")
    temp = temp.replace("[", "")
    temp = temp.replace(",", "")
    print(temp)
def decifrar_jogadas(x): #Função para a "decifrar" as jogadas(Função para identificar e separar a entrada dos caracteres ou "jogadas", facilitando a leitura dos movimentos)
  cili, cflf = x.split("--")
  ci = cili[0:1]
  li = cili[1:2]
  cf = cflf[0:1]
  lf = cflf[1:2]
  for a in range(10):
    if ci == alfabeto[a]:
      ci = a * 2 + 2
    if cf == alfabeto[a]:
      cf = a * 2 + 2
  li = int(li) * 2 + 2
  lf = int(lf) * 2 + 2
  return ci, li, cf, lf

jogo = inicializar_tabuleiro()

def validar_jogadas_cima(ci, li, cf,lf): #Função para validar e realizar as jogadas dos jogadores que usam "o"(Função analisa os casos de jogadas inválidas para as peças comuns e damas, retornando "jogada inválida" caso for verdade, caso não, realiza-se a troca de caracteres)
  comida=0
  comeu=0
  if jogo[li][ci] != "o" and jogo[li][ci] != "O":
    print("jogada inválida")
    return False, jogo, comeu
  elif jogo[li][ci] == "o":
    if abs(ci - cf) != 2 or abs(li - lf) != 2 or jogo[lf][cf] != " " or (li > lf) :
      if li < lf:
        if abs(ci - cf) == 4 and abs(li -lf) == 4 and (jogo[lf - 2][cf - 2] == "@" or jogo[lf - 2][cf - 2] == "&" or jogo[lf - 2][cf + 2] == "@" or jogo[lf - 2][cf + 2] == "&" ) and jogo[lf][cf] == " ":
          jogo[li][ci] = " "
          jogo[lf][cf] = "o"
          if jogo[lf - 2][cf - 2] == "@" or jogo[lf - 2][cf - 2] == "&":
            jogo[lf - 2][cf - 2] = " "
            comeu += 1
          elif jogo[lf - 2][cf + 2] == "@" or jogo[lf - 2][cf + 2] == "&":
            jogo[lf - 2][cf + 2] = " "
            comeu+=1
          return True, jogo, comeu

        else:
          print("Jogada inválida")
          return False, jogo, comeu
      if li > lf:
        if abs(ci - cf) == 4 and abs(li -lf) == 4 and (jogo[lf + 2][cf - 2] == "@" or jogo[lf + 2][cf - 2] == "&" or jogo[lf + 2][cf + 2] == "@" or jogo[lf + 2][cf + 2] == "&" ) and jogo[lf][cf] == " ":
          jogo[li][ci] = " "
          jogo[lf][cf] = "o"
          if jogo[lf + 2][cf - 2] == "@" or jogo[lf + 2][cf - 2] == "&":
            jogo[lf + 2][cf - 2] = " "
            comeu += 1
          elif jogo[lf + 2 ][cf + 2] == "@" or jogo[lf + 2][cf + 2] == "&":
            jogo[lf + 2][cf + 2] = " "
            comeu+=1
          return True, jogo, comeu

        else:
          print("jogada inválida")
          return False, jogo, comeu
    else:
      jogo[li][ci] = " "
      jogo[lf][cf] = "o"
      return True, jogo, comeu

  elif jogo[li][ci] == "O":
    x = 0
    comida = 0
    erro = 0
    if ci == cf or li == lf or jogo[lf][cf] != " ":
      print("Jogada inválida")
      return False, jogo, comeu
    elif li > lf and ci > cf:
      for l in range(li - 2 , lf, -2 ):
        if jogo[l][ci-x-2] == "@" or jogo[l][ci-x-2] == "&":
          comida += 1
          xi = l
          yi = ci-x-2
        elif jogo[l][ci-x-2] == "o" or jogo[l][ci-x-2] == "O":
          erro += 1
        x += 2
      if erro > 0 or comida > 1:
        print("Jogada inválida")
        return False, jogo, comeu
      else:
        jogo[li][ci] = " "
        jogo[lf][cf] = "O"
        if comida == 1:
          jogo[xi][yi] = " "
          comeu+=1
        return True, jogo, comeu



    elif li > lf and ci < cf:
      for l in range(li - 2, lf, -2):
        if jogo[l][ci+x+2] == "@" or jogo[l][ci+x+2] == "&":
          comida += 1
          xi = l
          yi = ci+x+2
        elif jogo[l][ci+x+2] == "o" or jogo[l][ci+x+2] == "O":
          erro += 1
        x += 2
      if erro > 0 or comida > 1:
        print("Jogada inválida")
        return False, jogo, comeu
      else:
        jogo[li][ci] = " "
        jogo[lf][cf] = "O"
        if comida == 1:
          jogo[xi][yi] = " "
          comeu+=1
        return True, jogo, comeu



    elif li < lf and ci > cf:
      for l in range(li + 2, lf, 2):
        if jogo[l][ci-x-2] == "@" or jogo[l][ci-x-2] == "&":
          comida += 1
          xi = l
          yi = ci-x-2
        elif jogo[l][ci-x-2] == "o" or jogo[l][ci-x-2] == "O":
          erro += 1
        x += 2
      if erro > 0 or comida > 1:
        print("Jogada inválida")
        return False, jogo, comeu
      else:
        jogo[li][ci] = " "
        jogo[lf][cf] = "O"
        if comida == 1:
          jogo[xi][yi] = " "
          comeu+=1
        return True, jogo, comeu


    elif li < lf and ci < cf:
        for l in range(li + 2, lf, 2):
          if jogo[l][ci+x+2] == "@" or jogo[l][ci+x+2] == "&":
            comida += 1
            xi = l
            yi = ci+x+2
          elif jogo[l][ci+x+2] == "o" or jogo[l][ci+x+2] == "O":
            erro += 1
          x += 2
        if erro > 0 or comida > 1:
          print("Jogada inválida")
          return False, jogo, comeu
        else:
          jogo[li][ci] = " "
          jogo[lf][cf] = "O"
          if comida == 1:
            jogo[xi][yi] = " "
            comeu+=1
          return True, jogo, comeu



def validar_jogadas_baixo(ci, li, cf,lf): #Função para validar e realizar as jogadas dos jogadores que usam "@"(Função analisa os casos de jogadas inválidas para as peças comuns e damas, retornando "jogada inválida" caso for verdade, caso não, realiza-se a troca de caracteres)
  comida = 0
  comeu=0
  if jogo[li][ci] != "@" and jogo[li][ci] != "&":
    print("jogada inválida")
    return False, jogo, comeu
  elif jogo[li][ci] == "@":
    if abs(ci - cf) != 2 or abs(li - lf) != 2 or jogo[lf][cf] != " " or (li < lf) :
      if li > lf:
        if abs(ci - cf) == 4 and abs(li -lf) == 4 and (jogo[lf + 2][cf - 2] == "o" or jogo[lf + 2][cf - 2] == "O" or jogo[lf + 2][cf + 2] == "o" or jogo[lf + 2][cf + 2] == "O") and jogo[lf][cf] == " ":
          jogo[li][ci] = " "
          jogo[lf][cf] = "@"
          if jogo[lf + 2][cf - 2] == "o" or jogo[lf - 2][cf - 2] == "O":
            jogo[lf + 2][cf - 2] = " "
            comeu += 1
          elif jogo[lf + 2][cf + 2] == "o" or jogo[lf - 2][cf + 2] == "O":
            jogo[lf + 2][cf + 2] = " "
            comeu += 1
          return True, jogo, comeu

        else:
          print("Jogada inválida")
          return False, jogo, comeu
      if li < lf:
        if abs(ci - cf) == 4 and abs(li -lf) == 4 and (jogo[lf - 2][cf - 2] == "o" or jogo[lf - 2][cf - 2] == "O" or jogo[lf - 2][cf + 2] == "o" or jogo[lf - 2][cf + 2] == "O") and jogo[lf][cf] == " ":
          jogo[li][ci] = " "
          jogo[lf][cf] = "@"
          if jogo[lf - 2][cf - 2] == "o" or jogo[lf - 2][cf - 2] == "O":
            jogo[lf - 2][cf - 2] = " "
            comeu += 1
          elif jogo[lf - 2][cf + 2] == "o" or jogo[lf - 2][cf + 2] == "O":
            jogo[lf - 2][cf + 2] = " "
            comeu+=1
          return True, jogo, comeu

        else:
          print("Jogada inválida")
          return False, jogo, comeu
    else:
      jogo[li][ci] = " "
      jogo[lf][cf] = "@"
      return True, jogo, comeu

  elif jogo[li][ci] == "&":
    if ci == cf or li == lf or jogo[lf][cf] != " ":
      print("Jogada inválida")
      return False, jogo, comeu
    elif li > lf and ci > cf:
      for l in range(li - 2 , lf, -2 ):
        if jogo[l][ci-x-2] == "o" or jogo[l][ci-x-2] == "O":
          comida += 1
          xi = l
          yi = ci-x-2
        elif jogo[l][ci-x-2] == "@" or jogo[l][ci-x-2] == "&":
          erro += 1
        x += 2
      if erro > 0 or comida > 1:
        print("Jogada inválida")
        return False, jogo, comeu
      else:
        jogo[li][ci] = " "
        jogo[lf][cf] = "&"
        if comida == 1:
          jogo[xi][yi] = " "
          comeu+=1
        return True, jogo, comeu


    elif li > lf and ci < cf:
      for l in range(li - 2 , lf, -2 ):
        if jogo[l][ci+x+2] == "o" or jogo[l][ci+x+2] == "O":
          comida += 1
          xi = l
          yi = ci+x+2
        elif jogo[l][ci+x+2] == "@" or jogo[l][ci+x+2] == "&":
          erro += 1
        x += 2
      if erro > 0 or comida > 1:
        print("Jogada inválida")
        return False, jogo, comeu
      else:
        jogo[li][ci] = " "
        jogo[lf][cf] = "&"
        if comida == 1:
          jogo[xi][yi] = " "
          comeu+=1
        return True, jogo, comeu


    elif li < lf and ci > cf:
      for l in range(li + 2 , lf, 2 ):
        if jogo[l][ci-x-2] == "o" or jogo[l][ci-x-2] == "O":
          comida += 1
          xi = l
          yi = ci-x-2
        elif jogo[l][ci-x-2] == "@" or jogo[l][ci-x-2] == "&":
          erro += 1
        x += 2
      if erro > 0 or comida > 1:
        print("Jogada inválida")
        return False, jogo, comeu
      else:
        jogo[li][ci] = " "
        jogo[lf][cf] = "&"
        if comida == 1:
          jogo[xi][yi] = " "
          comeu+=1
        return True, jogo, comeu


    elif li < lf and ci < cf:
      for l in range(li + 2 , lf, 2 ):
        if jogo[l][ci+x+2] == "o" or jogo[l][ci+x+2] == "O":
          comida += 1
          xi = l
          yi = ci+x+2
        elif jogo[l][ci+x+2] == "@" or jogo[l][ci+x+2] == "&":
          erro += 1
        x += 2
      if erro > 0 or comida > 1:
        print("Jogada inválida")
        return False, jogo, comeu
      else:
        jogo[li][ci] = " "
        jogo[lf][cf] = "&"
        if comida == 1:
          jogo[xi][yi] = " "
          comeu+=1
        return True, jogo, comeu



#Função pra descobrir se tem alguma peça perto para comer, vejam se tá certo, esparei o de cima e o de baixo
def peca_pra_comer_obrigatoriamente_cima(ci, li, cf, lf):
  for l in range(23):
    for c in range(23):
      if cf == c and lf == l:
        continue
      if jogo[l][c] == 'o' or jogo[l][c] == 'O':
        if jogo[l][c] == 'o':
          if (jogo[l - 2][c - 2]=='@' or jogo[l - 2][c - 2]=="&") and jogo[l - 4][c - 4] == " " :
            print("Existe uma peça disponível para ser comida")
            return True
            break
          elif (jogo[l - 2][c + 2]=='@' or jogo[l - 2][c + 2]=="&") and jogo[l - 4][c + 4] == " " :
            print("Existe uma peça disponível para ser comida")
            return True
            break
          elif (jogo[l + 2][c - 2]=='@' or jogo[l + 2][c - 2]=="&") and jogo[l + 4][c - 4] == " " :
            print("Existe uma peça disponível para ser comida")
            return True
            break
          elif (jogo[l + 2][c + 2]=='@' or jogo[l + 2][c + 2]=="&") and jogo[l + 4][c + 4] == " " :
            print("Existe uma peça disponível para ser comida")
            return True
            break

        elif jogo[l][c] == "O":
          x = 0
          comida = 0
          erro = 0
          for j in range(l-2, 0, -2): #diagonal superior direita
            if (jogo[j][c+x+2] == "@" or jogo[j][c+x+2] == "&") and jogo[j-2][c+x+4] == " ":
              comida += 1
              break

            if (jogo[j][c+x+2] == "o" or jogo[j][c+x+2] == "O"):
              erro +=1
              break
            x += 2
          if comida > 0:
            print("Existe uma peça disponível para ser comida")
            return True
          comida = 0
          erro = 0
          x == 0
          for j in range(l-2, 0, -2): #diagonal superior esquerda
            if (jogo[j][c-x-2] == "@" or jogo[j][c-x-2] == "&") and jogo[j-2][c-x-4] == " ":
              comida += 1
              break
            if (jogo[j][c-x-2] == "o" or jogo[j][c-x-2] == "O"):
              erro += 1
              break
            x += 2
          if comida > 0:
            print("Existe uma peça disponível para ser comida")
            return True
          x == 0
          comida = 0
          erro = 0
          for j in range(l+2, 22, 2): #diagonal inferior direita
            if (jogo[j][c+x+2] == "@" or jogo[j][c+x+2] == "&") and jogo[j+2][c+x+4] == " ":
              comida += 1
              break
            if (jogo[j][c+x+2] == "o" or jogo[j][c+x+2] == "O"):
              erro += 1
              break
            x += 2
          if comida > 0:
            print("Existe uma peça disponível para ser comida")
            return True
          x == 0
          comida = 0
          erro = 0
          for j in range(l+2, 22, 2): #diagonal inferior esquerda
            if (jogo[j][c-x-2] == "@" or jogo[j][c-x-2] == "&") and jogo[j+2][c-x-4] == " ":
              comida += 1
              break
            if (jogo[j][c-x-2] == "o" or jogo[j][c-x-2] == "O"):
              erro += 1
              break
            x += 2
          if comida > 0:
            print("Existe uma peça disponível para ser comida")
            return True
  return False





def peca_pra_comer_obrigatoriamente_baixo(ci, li, cf, lf):

  for l in range(23):
    for c in range(23):
      if cf == c and lf == l:
        continue
      if jogo[l][c]== '@' or jogo[l][c]== '&':
        if jogo[l][c]== '@':
          if (jogo[l - 2][c - 2]=='o' or jogo[l - 2][c - 2]=="O") and jogo[l - 4][c - 4] == " ":
            print("Existe uma peça disponível para ser comida")
            return True
            break
          elif (jogo[l - 2][c + 2]=='o' or jogo[l - 2][c + 2]=="O") and jogo[l - 4][c + 4] == " ":
            print("Existe uma peça disponível para ser comida")
            return True
            break
          elif (jogo[l + 2][c - 2]=='o' or jogo[l + 2][c - 2]=="O") and jogo[l + 4][c - 4] == " ":
            print("Existe uma peça disponível para ser comida")
            return True
            break
          elif (jogo[l + 2][c + 2]=='o' or jogo[l + 2][c + 2]=="O") and jogo[l + 4][c + 4] == " ":
            print("Existe uma peça disponível para ser comida")
            return True
            break


        elif jogo[l][c] == "&":
          x = 0
          comida = 0
          erro = 0
          for j in range(l-2, 0, -2): #diagonal superior direita
            if (jogo[j][c+x+2] == "o" or jogo[j][c+x+2] == "O") and jogo[j-2][c+x+4] == " ":
              comida += 1
              break

            if (jogo[j][c+x+2] == "@" or jogo[j][c+x+2] == "&"):
              erro +=1
              break
            x += 2
          if comida > 0:
            print("Existe uma peça disponível para ser comida")
            return True
          comida = 0
          erro = 0
          x == 0
          for j in range(l-2, 0, -2): #diagonal superior esquerda
            if (jogo[j][c-x-2] == "o" or jogo[j][c-x-2] == "O") and jogo[j-2][c-x-4] == " ":
              comida += 1
              break
            if (jogo[j][c-x-2] == "@" or jogo[j][c-x-2] == "&"):
              erro += 1
              break
            x += 2
          if comida > 0:
            print("Existe uma peça disponível para ser comida")
            return True
          x == 0
          comida = 0
          erro = 0
          for j in range(l+2, 22, 2): #diagonal inferior direita
            if (jogo[j][c+x+2] == "o" or jogo[j][c+x+2] == "O") and jogo[j+2][c+x+4] == " ":
              comida += 1
              break
            if (jogo[j][c+x+2] == "@" or jogo[j][c+x+2] == "&"):
              erro += 1
              break
            x += 2
          if comida > 0:
            print("Existe uma peça disponível para ser comida")
            return True
          x == 0
          comida = 0
          erro = 0
          for j in range(l+2, 22, 2): #diagonal inferior esquerda
            if (jogo[j][c-x-2] == "o" or jogo[j][c-x-2] == "O") and jogo[j+2][c-x-4] == " ":
              comida += 1
              break
            if (jogo[j][c-x-2] == "@" or jogo[j][c-x-2] == "&"):
              erro += 1
              break
            x += 2
          if comida > 0:
            print("Existe uma peça disponível para ser comida")
            return True
  return False




# Função para verificar se uma peça comum se tornou uma dama, se verdade, substituindo as peças.
def verificar_se_dama():
  for num in range(23):
    if jogo[2][num] == '@':
      jogo[2][num] = '&'
  for num in range(23):
    if jogo[20][num] == 'o':
      jogo[20][num] = 'O'



def jogada_disponivel_cima(jogo):
  for linha in range(23):
    for coluna in range(23):
      if jogo[linha][coluna] == 'o':
        #if li>lf and ci>cf: 2 quadrante
          if (jogo[linha-2][coluna-2]=='&' or jogo[linha-2][coluna-2]=='@') and  jogo[linha-4][coluna-4]==' ':
            return True
        # li>lf and ci<cf  1 quadrante
          elif (jogo[linha-2][coluna+2]=='&' or jogo[linha-2][coluna+2]=='@') and  jogo[linha-4][coluna+4]==' ':
            return True
        # li<lf and ci>cf 3 quadrante
          elif ((jogo[linha+2][coluna-2]=='&' or jogo[linha+2][coluna-2]=='@') and  jogo[linha+4][coluna-4]==' ') or jogo[linha+2][coluna-2]==' ':
            return True
        # li<lf and ci<cf 4 quadrante
          elif ((jogo[linha+2][coluna+2]=='&' or jogo[linha+2][coluna+2]=='@') and  jogo[linha+4][coluna+4]==' ') or jogo[linha+2][coluna+2]==' ':
            return True
      elif jogo[linha][coluna] == 'O':
        #if li>lf and ci>cf: 2 quadrante
          if ((jogo[linha-2][coluna-2]=='&' or jogo[linha-2][coluna-2]=='@') and  jogo[linha-4][coluna-4]==' ') or  jogo[linha-2][coluna-2]==' ':
            return True
        # li>lf and ci<cf  1 quadrante
          if ((jogo[linha-2][coluna+2]=='&' or jogo[linha-2][coluna+2]=='@') and  jogo[linha-4][coluna+4]==' ') or jogo[linha-2][coluna+2]==' ':
            return True
        # li<lf and ci>cf 3 quadrante
          elif ((jogo[linha+2][coluna-2]=='&' or jogo[linha+2][coluna-2]=='@') and  jogo[linha+4][coluna-4]==' ') or jogo[linha+2][coluna-2]==' ':
            return True
        # li<lf and ci<cf 4 quadrante
          elif ((jogo[linha+2][coluna+2]=='&' or jogo[linha+2][coluna+2]=='@') and  jogo[linha+4][coluna+4]==' ') or jogo[linha+2][coluna+2]==' ':
             return True

  return False

def jogada_disponivel_baixo(jogo):
  for linha in range(23):
    for coluna in range(23):
      if jogo[linha][coluna] == '@':
        #if li>lf and ci>cf: 2 quadrante
          if ((jogo[linha-2][coluna-2]=='o' or jogo[linha-2][coluna-2]=='O') and  jogo[linha-4][coluna-4]==' ') or  jogo[linha-2][coluna-2]==' ':
            return True
        # li>lf and ci<cf  1 quadrante
          if ((jogo[linha-2][coluna+2]=='o' or jogo[linha-2][coluna+2]=='O') and  jogo[linha-4][coluna+4]==' ') or jogo[linha-2][coluna+2]==' ':
            return True
        # li<lf and ci>cf 3 quadrante
          if (jogo[linha+2][coluna-2]=='o' or jogo[linha+2][coluna-2]=='O') and  jogo[linha+4][coluna-4]==' ':
            return True
        # li<lf and ci<cf 4 quadrante
          if (jogo[linha+2][coluna+2]=='o' or jogo[linha+2][coluna+2]=='O') and  jogo[linha+4][coluna+4]==' ':
            return True
      elif jogo[linha][coluna] == '&':
        #if li>lf and ci>cf: 2 quadrante
          if ((jogo[linha-2][coluna-2]=='o' or jogo[linha-2][coluna-2]=='O') and  jogo[linha-4][coluna-4]==' ') or  jogo[linha-2][coluna-2]==' ':
            return True
        # li>lf and ci<cf  1 quadrante
          if ((jogo[linha-2][coluna+2]=='o' or jogo[linha-2][coluna+2]=='O') and  jogo[linha-4][coluna+4]==' ') or jogo[linha-2][coluna+2]==' ':
            return True
        # li<lf and ci>cf 3 quadrante
          elif ((jogo[linha+2][coluna-2]=='o' or jogo[linha+2][coluna-2]=='O') and  jogo[linha+4][coluna-4]==' ') or jogo[linha+2][coluna-2]==' ':
            return True
        # li<lf and ci<cf 4 quadrante
          elif ((jogo[linha+2][coluna+2]=='o' or jogo[linha+2][coluna+2]=='O') and  jogo[linha+4][coluna+4]==' ') or jogo[linha+2][coluna+2]==' ':
            return True

  return False