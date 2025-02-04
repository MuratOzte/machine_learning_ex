from pynput.keyboard import Controller
import threading
import time
import keyboard

kb = Controller()
running = False


def press_space():
    global running
    while running:
        kb.press(" ")
        kb.release(" ")
        time.sleep(0.5)


def toggle_bot():
    global running
    if running:
        print("Bot durduruldu!")
        running = False
    else:
        print("Bot başlatıldı!")
        running = True
        threading.Thread(target=press_space, daemon=True).start()


keyboard.add_hotkey("ctrl+*", toggle_bot)
keyboard.add_hotkey("ctrl+-", lambda: exit())
      
keyboard.wait()              
 