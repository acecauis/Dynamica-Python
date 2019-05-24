import tkinter as tk


class ButtonCanvas(tk.Canvas):
    def __init__(self, display):
        tk.Canvas.__init__(self, display.root,
                           width=display.button_canvas_width, height=display.button_canvas_height,
                           bd=0, highlightthickness=0)

        self.display = display

        self.button_height = 2
        self.button_width = 8

        self.next_button = None
        self.run_button = None
        self.save_button = None
        self.quit_button = None

        self.create_buttons()

    def create_buttons(self):

        self.next_button = tk.Button(self, text="Next", fg="black",
                                     height=self.button_height, width=self.button_width,
                                     command=self.display.next_turn)
        self.next_button.grid(row=0, column=0, sticky=tk.W)

        self.run_button = tk.Button(self, text="Run", fg="black",
                                    height=self.button_height, width=self.button_width,
                                    command=self.display.run_game)
        self.run_button.grid(row=0, column=1, sticky=tk.W)

        self.save_button = tk.Button(self, text="Save", fg="black",
                                     height=self.button_height, width=self.button_width,
                                     command=self.display.save_game)
        self.save_button.grid(row=0, column=2, sticky=tk.W)

        self.quit_button = tk.Button(self, text="Quit", fg="black",
                                     height=self.button_height, width=self.button_width,
                                     command=self.display.quit_game)
        self.quit_button.grid(row=0, column=3, sticky=tk.E)
