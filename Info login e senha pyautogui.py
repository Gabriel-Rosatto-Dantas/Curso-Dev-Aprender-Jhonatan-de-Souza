import pyautogui

email = pyautogui.prompt(text='Digite seu email', title='Informações obrigatórias')
senha = pyautogui.password(text='Digite sua senha', title='Informações obrigatórias',mask='*')

pyautogui.moveTo(x=1066, y=100, duration=2)
pyautogui.click()
pyautogui.write(email)
pyautogui.press('Enter')
pyautogui.write(senha)

