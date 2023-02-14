from tkinter import *
from tkinter import messagebox
from tkinter import ttk

janela = Tk("Gerenciador de Tarefas")
janela.configure(bg='black')
janela.title("Gerenciador de Tarefas")
janela.attributes('-alpha', 0.8)
janela.geometry('600x400')
janela.resizable(True, True)
janela.configure(bg='#333')

style = ttk.Style()
style.theme_use('clam')
style.configure('.', relief='flat', background='#333', foreground='#fff', font=('Helvetica', 12), borderwidth=30 )
style.configure('.', background='#333', foreground='#fff', font=('Helvetica', 12), borderwidth=10)
style.configure('TListbox', background='#fff', foreground='#333', font=('Helvetica', 20))
style.configure('Botao.TButton', background='#310638', foreground='#fff', font=('Helvetica', 12))
style.configure('RoundedWindow.Toplevel',  borderwidth=10, relief='flat', background='#333')

style = ttk.Style()
style.theme_use('clam')
style.configure('.', relief='flat', background='#333', foreground='#fff', font=('Helvetica', 12), borderwidth=30 )
style.configure('.', background='#333', foreground='#fff', font=('Helvetica', 12), borderwidth=10)
style.configure('TListbox', background='#fff', foreground='#333', font=('Helvetica', 20))
style.configure('Botao.TButton', background='#310638', foreground='#fff', font=('Helvetica', 12))

class Tarefa:
  def __init__(self, tarefa):
    self.tarefa = tarefa

tarefas = []

def adicionar_tarefa(event=None):
  tarefa = entry_tarefa.get()
  tarefas.append(Tarefa(tarefa))
  atualizar_lista_tarefas()
  entry_tarefa.delete(0, END)

def excluir_tarefa(event):
  selecionada = listbox_tarefas.curselection()
  if selecionada:
    indice = int(selecionada[0])
    tarefas.pop(indice)
    atualizar_lista_tarefas()

def atualizar_lista_tarefas():
  listbox_tarefas.delete(0, END)
  for tarefa in tarefas:
    listbox_tarefas.insert(END, f"{tarefa.tarefa}")

    
def editar_tarefa(indice):
    selecionada = listbox_tarefas.curselection()
    if selecionada:
        tarefa_editar = tarefas[indice].tarefa
        entry_tarefa.delete(0, END)
        entry_tarefa.insert(0, tarefa_editar)
        tarefas.pop(indice)
        atualizar_lista_tarefas()


def excluir_tarefas_selecionadas():
  selecionadas = listbox_tarefas.curselection()
  if selecionadas:
    for indice in selecionadas[::-1]: 
      tarefas.pop(indice)
    atualizar_lista_tarefas()
    
label_tarefa = Label(janela, height=1, text="Notas:", relief='flat', background='#333', foreground='#fff', font=('Helvetica', 35) )
entry_tarefa = Entry(janela, width=40, relief='flat', background='#333', foreground='#fff', font=('Helvetica', 12))
listbox_tarefas = Listbox(janela, height=10, width=155, relief='flat', background='#333', foreground='#fff', font=('Helvetica', 20))
scrollbar_tarefas = Scrollbar(janela, orient=VERTICAL)
botao_adicionar = Button(janela, text="Adicionar", command=adicionar_tarefa)
botao_excluir = Button(janela, text="Excluir", command=excluir_tarefas_selecionadas)
botao_adicionar = ttk.Button(janela, text="Adicionar", command=adicionar_tarefa, style='Botao.TButton')
botao_excluir = ttk.Button(janela, text="Excluir", command=excluir_tarefas_selecionadas, style='Botao.TButton')

label_tarefa.grid(row=0, column=0, padx=6, pady=5, sticky=NSEW)
entry_tarefa.grid(row=0, column=1, padx=6, pady=5, sticky=NSEW)
listbox_tarefas.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=NSEW)
scrollbar_tarefas.grid(row=1, column=3, pady=3, sticky=NSEW)
botao_adicionar.grid(row=4, column=0, padx=5, pady=5, sticky=NSEW)
botao_excluir.grid(row=4, column=1, padx=5, pady=5, sticky=NSEW)


def excluir_tarefas(event=None):
    excluir_tarefas_selecionadas()
listbox_tarefas.bind("<Delete>", excluir_tarefa)


janela.bind("<Return>", adicionar_tarefa)


janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.columnconfigure(2, weight=1)
janela.rowconfigure(1, weight=1)

janela.attributes('-alpha', 0.9)
item_selecionado = None

def on_select(event):
  global item_selecionado
  item_selecionado = listbox_tarefas.nearest(event.y)

def on_drag(event):
  listbox_tarefas.yview_scroll(-1 * (event.delta // 120), "units")

def on_release(event):
  item_final = listbox_tarefas.nearest(event.y)

  if item_selecionado is not None and item_final is not None and item_final != item_selecionado:
    tarefa = tarefas.pop(item_selecionado)
    tarefas.insert(item_final, tarefa)
    atualizar_lista_tarefas()

listbox_tarefas.bind("<Button-1>", on_select)
listbox_tarefas.bind("<B1-Motion>", on_drag)
listbox_tarefas.bind("<ButtonRelease-1>", on_release)
listbox_tarefas.bind("<Double-Button-1>", lambda event: editar_tarefa(listbox_tarefas.curselection()[0]))

mainloop()
