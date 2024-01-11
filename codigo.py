import pyautogui
import pandas as pd
import time

 
# pip install pyautogui

#clicar -> pyautogui.click
#escrever -> pyautogui.write
#apertar -> pyautogui.press
#       apertar -> pyautogui.press("win")
#       apertar -> pyautogui.hotkey("Ctrl", "C")

## Passo 1 - Entrar no sistema da empresa

pyautogui.PAUSE = 1

# aperta a tecla do windowns
pyautogui.press("win")

# Digitar nome do programa (chrome)
pyautogui.write("chrome")

# apertar enter 
pyautogui.press("enter")

# esperar 5 segundos
time.sleep(3)

# digitar o link
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)

# apertar enter 
pyautogui.press("enter")

# esperar 5 segundos
time.sleep(5)

## Passo 2 - Fazer Login

# clicar no campo e-mail
pyautogui.click(x=634, y=375)

# Digitar o e-mail
pyautogui.write("meu.email@gmail.com")

# clicar ou ir para o campo senha
pyautogui.press("tab")

# Digitar a senha
pyautogui.write("minhaSenha123")

# Ir para o botão logar e apertar enter
# pyautogui.press("tab")
# pyautogui.press("enter")

# Clica no botão logar
pyautogui.click(x=667, y=537)



## Passo 3 - Importar a base de dados
# pip install pandas numpy openpyxl

time.sleep(5)
tabela = pd.read_csv("produtos.csv")
# Se tivesse em outro caminho...
#tabela = pd.read_csv("C://Users...")

for linha in tabela.index:
    ## Passa 4 - Cadastrar Produto
    pyautogui.click(x=564, y=263)

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(obs)
    #pyautogui.write(str(obs))
    pyautogui.press("tab")

    # enviar produto
    pyautogui.press("enter")


    # Passo 5 - Repetir isso até base de dados
    pyautogui.scroll(5000)