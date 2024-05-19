import requests
from datetime import datetime
from dateutil import parser
import tkinter as tk

def obter_horario_da_internet(timezone):
    url = f'http://worldtimeapi.org/api/timezone/{timezone}'
    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        datetime_str = dados['datetime']
        datetime_obj = parser.isoparse(datetime_str)
        return datetime_obj
    else:
        return None

def atualizar_horario(cidade, timezone):
    horario = obter_horario_da_internet(timezone)
    if horario:
        labels[cidade].config(text=f'{cidade}: {horario.strftime("%Y-%m-%d %H:%M:%S")}')
    else:
        labels[cidade].config(text=f'{cidade}: Erro ao obter o horário')

root = tk.Tk()
root.title("Data/Hora Global")

timezones = {
    'Brasília': 'America/Sao_Paulo',
    'Nova York': 'America/New_York',
    'Paris': 'Europe/Paris',
    'Tóquio': 'Asia/Tokyo'
}

labels = {}
buttons = {}
for cidade, timezone in timezones.items():
    frame = tk.Frame(root)
    frame.pack(pady=12)
    labels[cidade] = tk.Label(frame, text=f'{cidade}: Clique para exibir', font=('Helvetica', 17))
    labels[cidade].pack(side=tk.LEFT)
    buttons[cidade] = tk.Button(frame, text=f' Atualizar ',
                                command=lambda c=cidade, t=timezone: atualizar_horario(c, t))
    buttons[cidade].pack(side=tk.RIGHT)

root.mainloop()
