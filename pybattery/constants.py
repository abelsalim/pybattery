from collections import namedtuple

# [Imagens]
ZEROMAIS = '/pybattery/static/0_10.png'
ONZEMAIS = '/pybattery/static/11_20.png'
VINTEUMMAIS = '/pybattery/static/21_50.png'
CINQUENTAUMMAIS = '/pybattery/static/51_85.png'
OITENTASEISMAIS = '/pybattery/static/86_100.png'
CARREGANDO = '/pybattery/static/carregando.png'

# Namedtuple
Level = namedtuple('Level', ['inicio', 'fim', 'foto'])
LEVEL_1 = Level(0, 11, ZEROMAIS)
LEVEL_2 = Level(11, 21, ONZEMAIS)
LEVEL_3 = Level(21, 51, VINTEUMMAIS)
LEVEL_4 = Level(51, 86, CINQUENTAUMMAIS)
LEVEL_5 = Level(86, 101, OITENTASEISMAIS)

# Descrição Argparse app.py
DESCRIPTION = '''
Pybattery tem a função de auxiliar desktops como I3WM e OPENBOX
a notificarem o usuário sobre o status da bateria, assim como o
status do carregador (se está ou não carregando).
'''

# Níveis
NIVEIS = (20, 30, 40, 50, 60, 70, 80, 90)
