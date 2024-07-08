from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Gourmet')
# restaurante_mexicano = Restaurante('Mexican Food', 'Mexican')
# restaurante_japones = Restaurante('Japa', 'Japonesa')
restaurante_praca.receber_avaliacao('Kezia', 10)
restaurante_praca.receber_avaliacao('Becky', 8)
restaurante_praca.receber_avaliacao('Adiel', 5)

# restaurante_mexicano.alternar_estado()
def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()