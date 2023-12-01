""" Pika e o modulo reponsavel pela interacao com o rabbitmq """
import pika
from backend.models import VeiculoModel, CartaoModel, ClienteModel, EntregadorModel, UsuarioModel
from backend.views import ClienteView, CartaoView, EntregadorView, UsuarioView
from backend.controllers import VeiculoController, CartaoController, \
    ClienteController,EntregadorController, UsuarioController

# Configurações do banco de dados
database_config = {
    'database': 'itadelivery',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': '5432'
}

# Configurações do RabbitMQ
rabbitmq_config = {
    'host': 'localhost',
    'port': 5672,
    'credentials': pika.PlainCredentials('admin', '1234')
}

# Criar instâncias dos modelos
veiculo_model = VeiculoModel(database_config)
cartao_model = CartaoModel(database_config, rabbitmq_config)
cliente_model = ClienteModel(database_config)
entregador_model = EntregadorModel(database_config)
usuario_model = UsuarioModel(database_config)

# Criar instâncias das visões
cliente_view = ClienteView()
cartao_view = CartaoView()
entregador_view = EntregadorView()
usuario_view = UsuarioView()

# Criar instâncias dos controladores
veiculo_controller = VeiculoController(veiculo_model)
cartao_controller = CartaoController(cartao_model, cartao_view)
cliente_controller = ClienteController(cliente_model, cliente_view)
entregador_controller = EntregadorController(entregador_model, entregador_view)
usuario_controller = UsuarioController(usuario_model, usuario_view)

# Testar algumas funcionalidades
veiculo_controller.cadastrar_veiculo('carro', 'wolks', 'nivus', 2022, 'ABC2134')

cliente_controller.cadastrar_cliente('Claudio', '78377232741', '99999999', 'masculino', 'senha123')

cliente_controller.atualizar_cliente(1, 'Jeferson', '8599999999')

print("Parte referente ao mostrar dados do cliente!\n")
cliente_controller.obter_e_mostrar_dados(1)
print('\n')

cliente_controller.remover_cliente(4)

entregador_controller.atualizar_entregador(1, 'Allan', '999999999')

usuario_controller.realizar_login('123456789', 'senha123')

cartao_controller.cadastrar_cartao(1, 'Débito', '987654321')

usuario_controller.realizar_logout()
