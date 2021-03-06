import re
import tkinter as tk
from tkinter import ttk
from view import view
class scheduleview(tk.Tk, view):
    PAD = 10
    BTN_CAPTION = [
        "Schedule",
        "test1",
        "test1",
        "Exit"
    ]
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self._make_mainFrame()
        self._make_title()
       
        
        
    def _make_mainFrame(self):
        self.mainFrame = ttk.Frame(self)
        self.mainFrame.pack(padx=self.PAD, pady=self.PAD)

    """
        Sets view's title.
    """
    def _make_title(self):
        title = ttk.Label(self.mainFrame, text="Schedule", font=("Helvetica", 20))
        title.pack(padx=self.PAD, pady=self.PAD)
        btn = ttk.Button(self.mainFrame, text="generate", command=lambda: self.controller.generateSchedule())
        btn.pack()
    def display(self):
        self.mainloop()
        # set the controller to view
        # set the controller to view
    
 