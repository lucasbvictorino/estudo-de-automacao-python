import pyautogui
import time


print(30*'=')
contato = input('Digite o nome do contato alvo: ')
pesquisa = input('Digite o nome da imagem: ')
print(30*'=')

pyautogui.PAUSE = 1.25
#Pesquisa
pyautogui.click(x=123, y=1056)
pyautogui.write('google chrome')
pyautogui.press('enter')
time.sleep(1)
#Escolher gmail
pyautogui.click(x=1054, y=573)
#Abrir aba
pyautogui.hotkey('ctrl', 't')
pyautogui.write('{}'.format(pesquisa))
pyautogui.press('enter')
#imagens google
pyautogui.click(x=315, y=187)
pyautogui.click(x=123, y=396)

#pyautogui.click(x=349, y=424)
pyautogui.rightClick(x=1490, y=422)
pyautogui.click(x=1548, y=650)
#mandando zap
pyautogui.hotkey('ctrl', 't')
pyautogui.write('whatsappweb')
pyautogui.press('enter')
pyautogui.click(x=307, y=383)
time.sleep(5)
pyautogui.click(x=325, y=172)
pyautogui.write('{}'.format(contato))
pyautogui.press('enter')
pyautogui.PAUSE = 0.1
for i in range(0, 1):
    pyautogui.hotkey('ctrl', 'v')
#pyautogui.press('enter')







