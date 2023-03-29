import ttkbootstrap as ttk

class Test(ttk.Window):
    def __init__(self):
        super().__init__()
        self.withdraw()
        ttk.Label(self, text="Main").pack()

class TopTest(ttk.Toplevel):
    def __init__(self,app):
        super().__init__()
        self.app = app
        ttk.Label(self, text="TOP").pack()
        self.after(2000,self.done)

    def done(self):
        self.destroy()
        self.app.deiconify()


if __name__ == '__main__':
    test = Test()
    toptest = TopTest(test)
    toptest.mainloop()