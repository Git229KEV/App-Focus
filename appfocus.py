import tkinter as tk
import time
import ctypes
import pyautogui
import keyboard

class FocusApp:
    def __init__(self, master):
        self.master = master
        master.title("Focus App")
        master.geometry("300x100")

        self.label = tk.Label(master, text="Focus App - Click Start to begin")
        self.label.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_focus)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_focus, state=tk.DISABLED)
        self.stop_button.pack()

    def start_focus(self):
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        # Disable Alt+Tab
        keyboard.block_key('alt')
        keyboard.block_key('tab')

        # Set focus for a fixed period (in seconds)
        focus_time = 10  # Change this to your desired focus time
        end_time = time.time() + focus_time

        while time.time() < end_time:
            # Set focus on this app
            self.master.focus_force()
            self.master.update()
            time.sleep(0.1)

        # After the time is up, re-enable the Start button and Alt+Tab
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

        # Re-enable Alt+Tab
        keyboard.unblock_key('alt')
        keyboard.unblock_key('tab')

    def stop_focus(self):
        # Placeholder for stopping focus (optional)
        pass

def main():
    root = tk.Tk()
    app = FocusApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
