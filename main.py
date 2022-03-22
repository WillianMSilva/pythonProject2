import time
import pyautogui
import pyperclip


#time.sleep(5)
#localização = pyautogui.position()
#print('{}'.format(localização))


print('====== Plugados ======')

user = input('Insira o Usuário: ')
senha = input('Insira a senha: ')

pyautogui.hotkey('win')
pyautogui.write('chrome')
pyautogui.press('enter')
#pyautogui.hotkey('win', 'd')
#pyautogui.click(x = 38, y = 322, clicks = (2))
time.sleep(5)
pyautogui.click(x=948, y=65, clicks = (2))
#pyautogui.click(x=776, y=107, clicks = (1))

time.sleep(1)
pyperclip.copy('plugadosead.fiqueligadonews.com.br')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press('enter')
time.sleep(4)
pyautogui.click(x=1082, y=297, clicks = (1))
time.sleep(1)
pyautogui.click(x=1028, y=566, clicks = (1))
pyautogui.press('tab')
pyautogui.write(user)
pyautogui.press('enter')
time.sleep(5)
pyautogui.press('tab')
pyautogui.write(senha)
pyautogui.press('enter')


