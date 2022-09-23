import requests
from tkinter import *

def pegar_cotacoes():

    requisicao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    requisicao_dic = requisicao.json()
    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_bct = requisicao_dic['BTCBRL']['bid']

    texto = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_bct}'''
    texto_cotacao["text"] = texto


janela = Tk()
janela.title("Cotação Atual das Moedas")
janela.geometry("300x200")
texto_orientacao = Label(janela, text="Clique no botão para ver as cotações das moedas")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)
botao_click = Button(janela, text="Buscar cotações Dóla/Euro/BTC", command=pegar_cotacoes)
botao_click.grid(column=0, row=1, padx=10, pady=10)
texto_cotacao = Label(janela, text="")
texto_cotacao.grid(column=0, row=2, padx=10, pady=10)

janela.mainloop()

