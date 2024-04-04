import pyautogui
from time import sleep
import pyperclip

# Utilizar o CMD com a função mouseinfo para capturar com facilidade as posições do mouse na tela
 # pip install mouse info
 # from mouseinfo import mouseInfo
 # mouseInfo()

# Click personalizado

""" pyautogui.click(x=1611,y=507, clicks=1000,interval=1,button='left',duration=2)

# Click na posição atual (com botão esquerdo)

pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')

# Utilizar funções ja prontas do pyautogui

pyautogui.rightClick()
pyautogui.doubleClick()
pyautogui.tripleClick()
 """
 
# Desafio mover arquivo entre pastas

""" for i in range(9):
    pyautogui.moveTo(321,282,duration=0.4)
    pyautogui.dragTo(284,855,duration=0.4,button='left')  """
    
# Desafio mover scroll mouse

""" pyautogui.moveTo(1555,491, duration=2)
pyautogui.scroll(-2200) """

# Desafio escrever com pyautogui usando biblioteca pyperclip p/ caractere especial

def escrever_frase(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('Ctrl', 'v')

pyautogui.click(1251,151, duration=2)
pyautogui.click()
sleep(1)
escrever_frase('Automação é incrível!')