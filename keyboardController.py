import platform
import os

class KeyboardController:
    def __init__(self):
        self.system = platform.system()
        self.is_wayland = (self.system == 'Linux' and 
                          os.environ.get('XDG_SESSION_TYPE') == 'wayland')
        
        if not self.is_wayland:
            import pyautogui
            self.pyautogui = pyautogui

        if self.is_wayland:
            import subprocess
            subprocess.Popen(["ydotoold"])
        
    def type(self, text, interval=0.0):
        if self.is_wayland:
            import subprocess
            subprocess.run(['ydotool', 'type', text])
        else:
            self.pyautogui.write(text, interval=interval)
    
    def press(self, key):
        if self.is_wayland:
            import subprocess
            # Simple implementation - type single chars
            subprocess.run(['ydotool', 'type', key])
        else:
            self.pyautogui.press(key)
    
    def hotkey(self, *keys):
        if self.is_wayland:
            import subprocess
            # This would need proper key code mapping
            print(f"Hotkey {keys} not fully implemented for Wayland")
        else:
            self.pyautogui.hotkey(*keys)
