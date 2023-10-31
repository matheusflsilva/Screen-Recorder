import customtkinter
import pyautogui
import cv2
import numpy as np
import keyboard

app = customtkinter.CTk()
app.geometry('300x150')
app.title('Screen Recorder')
app.iconbitmap('icone/icone.ico')
customtkinter.set_appearance_mode('dark')

def gravar():
    fps = 20
    tamanho_tela = tuple(pyautogui.size())
    codec = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter('video.avi', codec, fps, tamanho_tela)

    while True:
        frame = pyautogui.screenshot()
        frame = np.array(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        video.write(frame)
        if keyboard.is_pressed('esc'):
            break

    video.release()
    cv2.destroyAllWindows()

botao = customtkinter.CTkButton(app, text='Gravar', command=gravar)
botao.pack(padx=10, pady=10)
texto = customtkinter.CTkLabel(app, text='ESC para finalizar a gravação.')
texto.pack(padx=10, pady=10)
app.mainloop()
