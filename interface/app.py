import tkinter as tk
from tkinter import ttk, messagebox
from scr.translator import run_translate, LANGUAGES


color_dark_gray1 = '#2e2e2e'
color_dark_gray2 = '#333333'
color_dark_gray3 = '#4d4d4d'
color_dark_gray4 = '#cccccc'
color_dark_gray5 = '#e6e6e6'
color_dark_gray6 = '#fafafa'


class App(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('App')
        self.resizable(width=False, height=False)
        #self.geometry('500x300')
        
        self.frame1 = ttk.Frame(self)
        self.frame1.pack(fill='both', expand=True)
        self.frame2 = ttk.Frame(self)
        self.frame2.pack(fill='both', expand=True)

        # create a label title and put it in the frame
        self.label_title = ttk.Label(self.frame1, text='Trrtrrtf Translator', style='TLabel', font=('helvetica bold', 15))
        self.label_title.pack(side='top', fill='both', expand=True, padx=10, pady=10)

        # create a label and put it in the frame
        self.cbx_from = ttk.Combobox(self.frame1, values=['Auto Detect'] + list(LANGUAGES.values()), state='readonly')
        self.cbx_from.current(0)
        self.cbx_from.pack(side='left', fill='both', expand=True, padx=10, pady=10)

        # create a label and put it in the frame
        self.cbx_to = ttk.Combobox(self.frame1, values=list(LANGUAGES.values()), state='readonly')
        self.cbx_to.current(0)
        self.cbx_to.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        
        # create a label and put it in the frame
        self.btn_swap = tk.Button(self.frame1, text='X', command=lambda: self.swap(), width=3, font=('helvetica', 12), borderwidth=0, relief='flat', 
        background=color_dark_gray3, activebackground=color_dark_gray3, foreground=color_dark_gray5, activeforeground=color_dark_gray5, bd=0)
        self.btn_swap.pack(side='bottom', fill='both', expand=True, padx=10, pady=10)
        
        # create a label and put it in the frame
        self.text_from = tk.Text(self.frame2, width=40, height=15, background=color_dark_gray3, foreground=color_dark_gray5, font=('helvetica', 12), bd=0)
        self.text_from.pack(side='left', fill='both', expand=True, padx=10, pady=10)
        
        # create a label and put it in the frame
        self.text_to = tk.Text(self.frame2, width=40, height=15, state='disabled', background=color_dark_gray3, foreground=color_dark_gray5, 
        font=('helvetica', 12), bd=0)
        self.text_to.pack(side='right', fill='both', expand=True, padx=10, pady=10)
        
        # create a label and put it in the frame
        self.style = ttk.Style()
        self.style.configure('TFrame', background=color_dark_gray1)
        self.style.configure('TCombobox', font=('helvetica', 20), background=color_dark_gray3)
        self.style.configure('TLabel', font=('helvetica bold', 15), background=color_dark_gray3, foreground=color_dark_gray5, anchor='center', labelmargin=20)
        
        

        self.translate()


    def swap(self):
        from_lang = self.cbx_from.get()
        to_lang = self.cbx_to.get()

        if from_lang != 'Auto Detect':
            self.cbx_from.set(to_lang)
            self.cbx_to.set(from_lang)
        else:
            pass


    def translate(self):
        from_lang = self.cbx_from.get()
        to_lang = self.cbx_to.get()
        text = self.text_from.get(1.0, 'end')

        if len(text) > 1:
            for key, value in LANGUAGES.items():
                if value == from_lang:
                    from_lang = key
                if value == to_lang:
                    to_lang = key

            if from_lang != 'Auto Detect':
                translated = run_translate(text=text, from_lang=from_lang, to_lang=to_lang)
            else:
                translated = run_translate(text=text, to_lang=to_lang)
        
            try:
                self.text_to.config(state='normal')
                self.text_to.delete(1.0, 'end')
                self.text_to.insert('end', translated)
                self.text_to.config(state='disabled')

            except Exception as e:
                messagebox.showerror('Error', e)

        self.after(ms=1000, func=self.translate)

    
                

