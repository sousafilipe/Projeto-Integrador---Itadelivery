""" Esse arquivo é responsável pelas views """


class ClienteView:
    """ Classe View do cliente """
    def mostrar_mensagem(self, mensagem):
        """ Método View do cliente para mostrar mensagem """
        print(mensagem)
    def mostrar_dados_conta(self, dados_cliente):
        if dados_cliente:
            print(f'Dados do Cliente:')
            # print(f'ID: {dados_cliente[0]}')
            print(f'Nome: {dados_cliente[1]}')
            print(f'CPF: {dados_cliente[2]}')
            print(f'Telefone: {dados_cliente[3]}')
            print(f'Gênero: {dados_cliente[4]}')
        else:
            print(f'Cliente não encontrado.')

class CartaoView:
    """ Classe View do cartão """
    def mostrar_mensagem(self, mensagem):
        """ Método View do cartao para mostrar mensagem """
        print(mensagem)

class EntregadorView:
    """ Classe View do Entregador """
    def mostrar_mensagem(self, mensagem):
        """ Método View do entregador para mostrar mensagem """
        print(mensagem)
    def mostrar_dados_conta(self, dados_entregador):
        if dados_entregador:
            print(f'Dados do Entregador:')
            # print(f'ID: {dados_entregador[0]}')
            print(f'Nome: {dados_entregador[1]}')
            print(f'CPF: {dados_entregador[2]}')
            print(f'Telefone: {dados_entregador[3]}')
            print(f'Gênero: {dados_entregador[4]}')
        else:
            print(f'Entregador não encontrado.')

class UsuarioView:
    """ Classe View do usuario """
    def mostrar_mensagem(self, mensagem):
        """ Método View do usuario para mostrar mensagem """
        print(mensagem)
