import PySimpleGUI as sg

class TelaPython:
    def __init__(self):
        layout = [
            [sg.Text('Nome'), sg.Input()],
            [sg.Text('Idade'), sg.Input()],
            [sg.Button('Enviar')]
        ]

        janela = sg.Window("Dafos do Usuário").layout(layout)
        self.button, self.values = janela.Read()

    def Iniciar(self):
        print(self.values)


tela = TelaPython()
tela.Iniciar()