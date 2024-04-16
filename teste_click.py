# iNSTALAR PIP INSTALL pyautogui E keyboard

import pyautogui
import time
import keyboard

# Função para obter e exibir as coordenadas do mouse
def show_mouse_position():
    current_mouse_position = pyautogui.position()
    print("Coordenadas do mouse:", current_mouse_position)
    
def obter_mouse():

    while True:
        # Exibe as coordenadas do mouse
        show_mouse_position()
        # Se a tecla 'q' for pressionada, saia do loop
        # Verifica se a tecla 'q' foi pressionada para sair do loop
        if keyboard.is_pressed('q'):
            break
        
        # Pausa o script por 3 segundos antes de verificar novamente
        time.sleep(3)
    print("Loop encerrado.")

# Tempo de espera entre cada ação para dar tempo ao navegador de responder
WAIT_TIME = 0.2

# Função para clicar em uma posição específica na tela
def click_position(x, y):
    pyautogui.click(x, y)
    # time.sleep(WAIT_TIME)

# Função para enviar texto
def send_text(text):
    pyautogui.write(text)
    # time.sleep(WAIT_TIME)

num_repeticoes = 7

def comecar_auto ():
    
    for _ in range(num_repeticoes):
        click_position(804, 491)
        send_text("desktop gamer")
        pyautogui.press('enter')
        pyautogui.hotkey('ctrl', 'tab')
        # Aguarda 1 segundo antes de repetir o loop
        # time.sleep(0.01)  
    

    
# obter_mouse()
comecar_auto()
print("Rodando...")
