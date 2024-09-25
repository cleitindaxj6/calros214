from Modelos.Moto import Moto

moto_honda = Moto('Honda', 'CB 500F', 'Novo')
moto_yamaha = Moto('Yamaha', 'MT-07', 'Novo')
moto_suzuki = Moto('Suzuki', 'GSX-R750', 'Novo')

moto_honda.alterar_estado()
moto_suzuki.receber_recondicionamento('Paraguai', 200)
moto_suzuki.receber_recondicionamento('Brasil', 1.000)
moto_suzuki.receber_recondicionamento('Argentina', 192.498)

def main():
    Moto.listar_motos()

if __name__ == '__main__':
    main()
