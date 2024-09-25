from Modelos.recondicionamento import Recondicionamento

class Moto:
    motos = []

    def __init__(self, nome, modelo, estado):
        self._nome = nome.upper()
        self._modelo = modelo.title()
        self.estado = estado
        self._ativo = False
        self._recondicionamento = []
        self._estado = []
        self._porcentagem = []
        Moto.motos.append(self)

    def __str__(self):
        return f'{self._nome} | {self._modelo} | {self.estado} | {self.ativo}'
    
    @classmethod
    def listar_motos(cls):
        print(''' 

███╗░░░███╗░█████╗░████████╗░█████╗░  ███╗░░░███╗░█████╗░██╗░░██╗
████╗░████║██╔══██╗╚══██╔══╝██╔══██╗  ████╗░████║██╔══██╗╚██╗██╔╝
██╔████╔██║██║░░██║░░░██║░░░██║░░██║  ██╔████╔██║███████║░╚███╔╝░
██║╚██╔╝██║██║░░██║░░░██║░░░██║░░██║  ██║╚██╔╝██║██╔══██║░██╔██╗░
██║░╚═╝░██║╚█████╔╝░░░██║░░░╚█████╔╝  ██║░╚═╝░██║██║░░██║██╔╝╚██╗
╚═╝░░░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝

████████╗███████╗░█████╗░███╗░░██╗░█████╗░██╗░░░░░░█████╗░░██████╗░██╗░█████╗░
╚══██╔══╝██╔════╝██╔══██╗████╗░██║██╔══██╗██║░░░░░██╔══██╗██╔════╝░██║██╔══██╗
░░░██║░░░█████╗░░██║░░╚═╝██╔██╗██║██║░░██║██║░░░░░██║░░██║██║░░██╗░██║███████║
░░░██║░░░██╔══╝░░██║░░██╗██║╚████║██║░░██║██║░░░░░██║░░██║██║░░╚██╗██║██╔══██║
░░░██║░░░███████╗╚█████╔╝██║░╚███║╚█████╔╝███████╗╚█████╔╝╚██████╔╝██║██║░░██║
░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚══╝░╚════╝░╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚═╝
''')
        print(f'{"Nome da Moto".ljust(18)} | {"Modelo da Moto".ljust(18)} | {"Estado da Moto".ljust(18)} | {"Ativo".ljust(18)}')
        print('----------------------------------------------------------------------------------------------------------------')
        for moto in cls.motos:
            print(f'{moto._nome.ljust(18)} | {moto._modelo.ljust(18)} | {moto.estado.ljust(18)} | {moto.ativo.ljust(40)} | {str(moto.media_porcentagem).ljust(18)}')
        print('----------------------------------------------------------------------------------------------------------------')

    @property
    def ativo(self):
        return '☑ A moto está ativa' if self._ativo else '☒ A moto não está ativada'
    
    def alterar_estado(self):
        self._ativo = not self._ativo

    def receber_recondicionamento(self, estado, porcentagem):
        recondicionamento = Recondicionamento(estado, porcentagem)
        self._recondicionamento.append(recondicionamento)

    @property
    def media_porcentagem(self):
        if not self._recondicionamento:
            return 0 
        soma_das_porcentagens = sum(recondicionamento._porcentagem for recondicionamento in self._recondicionamento)
        quantidade_moto = len(self._recondicionamento)
        media = round(soma_das_porcentagens / quantidade_moto, 1)
        return media
