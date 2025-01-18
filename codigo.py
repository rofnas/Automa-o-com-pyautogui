import pyautogui
import time
import pandas as pd
import openpyxl

pyautogui.PAUSE = 0.5

#pyautogui.click -> escrever
#pyautogui.press -> pressionar uma tecla
#pyautogui.write -> escrever
#pyautogui.hotkey -> atalho de teclado (ctrl, C))

# Passo 1: Abrir o sistema da empresa
# Abrir o Google Chrome
# Apertar a tecla win 

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")


# Entrar no link do        Sistema: https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")


# pedir para o computador esperar 3 segundos
time.sleep(3)


# Passo 2: Fazer login

pyautogui.click(x=391, y=375)
time.sleep(5)
pyautogui.write("rofnas@gmail.com")

pyautogui.press("tab")
pyautogui.write("senha")

pyautogui.press("tab")
pyautogui.press("enter")



# Passo 3: Importar a base de dados dos produtos


tabela = pd.read_csv("produtos.csv")

print(tabela)

time.sleep(2)

# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o passo 4 até acabar todos os produtos


for linha in tabela.index:


    pyautogui.click(x=387, y=257)



    # codigo 
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")  

    #  marca 
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")  

    #  tipo  
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")  


    # categoria 
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")  

    # preco_unitario  
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")  


    # custo    
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")  

    # obs
    obs = str(tabela.loc[linha, "obs"])     
    
    if obs != "nan":
        pyautogui.write(obs)
    
    pyautogui.press("tab")  

    pyautogui.press("enter")

    pyautogui.scroll(5000)






