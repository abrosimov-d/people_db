import tkinter as tk
from tkinter import ttk

class Dialog():
    def __init__(self):
        self.WIDTH = 40
        self.BG = '#13222e'
        self.BG3 = '#1a1c23'
        self.BG2 = '#36383e'
        self.FG = '#bfc0c2'
        self.FF = 'Consolas'

        self.SIZES = [
            {'name': 'S', 'WIDTH': 40, 'geometry': '600x160'},
            {'name': 'L', 'WIDTH': 25, 'geometry': '400x200'},
            {'name': 'XL', 'WIDTH': 25, 'geometry': '400x400'},
            {'name': 'XXL', 'WIDTH': 40, 'geometry': '800x650'},
            {'name': 'XXXL', 'WIDTH': 60, 'geometry': '1400x800'},
            #{'name': 'XL', 'WIDTH': 25, 'geometry': '800x800'},
        ]

        self.FONT = (self.FF, 16)
        self.BIGFONT = (self.FF, 22, 'bold')
        self.SMALLFONT = (self.FF, 12, 'bold')
        self.XXLFONT = (self.FF, 32, 'bold')
        self.root = tk.Tk()
        self.root.geometry('100x100')
        self.root.option_add("*Font", self.FONT) 
        self.root.config(bg=self.BG)
        self.elements = []
        self.notebook = None
        self.toolbar = None
        self.frame = self.root

    def template(self, template):
        lines = template.split('\n')
        for line in lines:
            data = line.split(',')
            if len(data) > 2:
                element = {}
                element['type'] = data[0].strip()
                element['text'] = data[1].strip()
                element['id'] = int(data[2])
                element['values'] = data[3:]
                self.elements.append(element)
        for element in self.elements:
            expand = False
            fill = None
            anchor = None
            pady = 5
            ipady = 5
            match element['type']:
                case 'size':
                    for size in self.SIZES:
                        if element['text'] == size['name']:
                            self.WIDTH = size['WIDTH']
                            self.root.geometry(size['geometry'])
                    
                case 'button':
                    element['object'] = tk.Button(self.frame, text=element['text'], width=self.WIDTH, command=lambda id=element['id']:self.on_event_click(id), bg=self.BG3, fg=self.FG, relief="flat", bd=0, cursor='hand2')
                    element['object'] .bind("<Enter>", self.on_enter) 
                    element['object'] .bind("<Leave>", self.on_leave)
                case 'input':
                    element['object'] = tk.Entry(self.frame, text=element['text'], width=self.WIDTH, bg=self.BG2, fg=self.FG, relief="flat", bd=-1)
                    element['object'].bind("<KeyRelease>", lambda key, id=element['id']: self.on_event_key(key, id))
                case 'password':
                    element['object'] = tk.Entry(self.frame, text=element['text'], width=self.WIDTH, bg=self.BG2, fg=self.FG, relief="flat", bd=0, show='*')
                    element['object'].bind("<KeyRelease>", lambda key, id=element['id']: self.on_event_key(key, id))
                case 'separator':
                    element['object'] = tk.Frame(self.frame, width=self.WIDTH, bg=self.BG)
                case 'label':
                    element['object'] = tk.Label(self.frame, text=element['text'], width=self.WIDTH, bg=self.BG, fg=self.FG)
                case 'xlabel':
                    element['object'] = tk.Label(self.frame, text=element['text'], width=self.WIDTH, bg=self.BG, fg=self.FG, font=self.XXLFONT)
                case 'slabel':
                    element['object'] = tk.Label(self.frame, text=element['text'], width=self.WIDTH+20, bg=self.BG, fg=self.FG, font=self.SMALLFONT)
                    pady = 0
                    ipady = 0
                case 'treeview':
                    style = ttk.Style()
                    style.theme_use("default")
                    style.configure("Treeview", background=self.BG, foreground=self.FG, fieldbackground=self.BG, font=self.FF, rowheight=25, borderwidth=0, relief='flat')
                    style.configure("Treeview.Heading", background=self.FG, foreground=self.BG, fieldbackground=self.BG2, relief='flat', rowheight=30, font=self.FONT)
                    #style.layout("Treeview", [ ("Treeview.field", {"sticky": "nswe", "border": "1", "children": [ ("Treeview.padding", {"sticky": "nswe", "children": [ ("Treeview.treearea", {"sticky": "nswe"}) ]}) ]}) ]) 
                    element['object'] = ttk.Treeview(self.frame, show='headings')
                    element['object']["columns"] = element['values']
                    for column in element['values']:
                        element['object'].heading(column, text=column)
                    
                    fill=tk.BOTH
                    expand = True
                case 'header':
                    element['object'] = tk.Label(self.frame, text=element['text'], width=self.WIDTH, bg=self.BG, fg=self.FG, font=self.BIGFONT, anchor='w')
                    anchor = 'w'
                case 'combo':
                    style = ttk.Style()
                    style.theme_use("default")
                    style.configure("TCombobox", background=self.BG, foreground=self.FG, fieldbackground=self.BG2, font=self.FONT, rowheight=25, borderwidth=0, relief='flat')
                    style.map("TCombobox", fieldbackground=[("readonly", self.BG)], foreground=[("readonly", self.FG)], background=[("readonly", self.BG)])
                    element['object'] = ttk.Combobox(self.frame, width=self.WIDTH, values=element['values'], state='readonly', cursor='hand2')
                    element['object'].set(element['values'][0])
                    element['object'].bind("<<ComboboxSelected>>", lambda e=element['object']:element['object'].selection_clear())
                #case 'image':
                    #image = Image.open('.\\assets\\error.png')
                    #image = tk.PhotoImage(image)
                    #element['object'] = ttk.Label(self.root, image=image)
                case 'tab':
                    style = ttk.Style() 
                    style.theme_use('default')
                    style.configure('TNotebook', background=self.BG, fieldbackground=self.BG2, font=self.FF, relief='flat', borderwidth=0)
                    style.layout('TNotebook.Tab', [])

                    if self.toolbar == None:
                        self.toolbar = tk.Frame(self.root, bg=self.BG)
                        self.toolbar.pack(side=tk.LEFT, anchor='n', fill='x')

                    button1 = tk.Button(self.toolbar, text=element['text'], font=self.BIGFONT, command=lambda id=int(element['values'][0]):self.on_event_click(id), bg=self.BG3, fg=self.FG, relief="flat", bd=0, cursor='hand2')
                    button1.pack(side=tk.TOP, anchor='w',)
                    button1.bind("<Enter>", self.on_enter) 
                    button1.bind("<Leave>", self.on_leave)

                    if self.notebook == None:
                        self.notebook = ttk.Notebook(self.root, style='TNotebook')
                        self.notebook.pack(fill='both', expand=True, anchor='e', side = tk.RIGHT)
                    self.frame = tk.Frame(self.notebook, bg=self.BG, bd=0, relief='flat')
                    self.frame.pack(fill='both')#, expand=True)
                    self.notebook.add(self.frame, text='qwe')#, state='hidden')
                    pass

                case _:
                    pass
            if 'object' in element:
                element['object'].pack(pady=pady, expand=expand, anchor=anchor, fill=fill, ipady=ipady)

    def get_element_by_id(self, id):
        result = None
        for element in self.elements:
            if element['id'] == id:
                result = element
                break
        return result
    
    def set_data_to_treeview(self, id, data):
        tree = self.get_element_by_id(id)
        if tree != None:
            for item in data:
                tree['object'].insert('', 'end', values=item)

    def on_event_click(self, id):
        self.event_listener('click', id, None)

    def on_event_key(self, event, id):
        element = self.get_element_by_id(id)
        element['text'] = element['object'].get()
        self.event_listener('key', id, event)

    def set_event_listner(self, listener):
        self.event_listener = listener

    def get_text_by_id(self, id):
        element = self.get_element_by_id(id)
        element['text'] = element['object'].get()
        return element['text']
    
    def set_text_by_id(self, id, text):
        element = self.get_element_by_id(id)
        element['text'] = text

        if element['type'] in ('label', 'xlabel', 'slabel'):
            element['object'].configure(text=text)
        else:
            element['object'].delete(0, tk.END)
            element['object'].insert(0, text)

    def run(self):
        self.root.mainloop()

    def on_enter(self, event):
        event.widget.config(bg=self.BG2)

    def on_leave(self, event):
        event.widget.config(bg=self.BG3)

    def get_selected_index_by_id(self, id):
        element = self.get_element_by_id(id)
        return element['object'].current()

    def set_enable_by_id(self, id, enable):
        element = self.get_element_by_id(id)
        element['object'].config(state = tk.NORMAL if enable else tk.DISABLED)

    def set_active_tab(self, index):
        self.notebook.select(index)