#!/usr/bin/env python

from math import cos, pi

path='misc/log_charpy_03.txt'
with open(path, encoding='utf-8') as file:
    data = file.read()
    data_list = []

    # pega cada linha do arquivo e atribui os dados
    # a um dicionário que separa as informações para
    # que possam ser usadas com facilidade
    line_count = 1
    for line in data.splitlines():

        tmp = line.split()
        tmp = {
                'us': tmp[0],
                'degrees': tmp[1],
                'line': line_count
        }

        line_count += 1
        data_list.append(tmp)

    # vai armazenar os momentos em que o martelo estava preso
    # no gancho, os testes atuais indicam que quando o sensor
    # acusa 321 graus, é quando o martelo está preso.
    locked_moment_list = []

    line_count = 1
    for i in data_list:
        if i['degrees'] == '321':
            locked_moment_list.append(i)
        line_count += 1
    
    # pegando o último momento antes do martelo ser liberado
    last_target_line = locked_moment_list[-1]
    last_target_line = int(last_target_line['line'])

    # FIXME: repare que o algorítmo não tem ideia de que o operador,
    # após o impacto, prendeu novamente o martelo no gatilho.

    print(f"O último momento do 321 graus:\nLinha {last_target_line}")

    # atribui o valor da última vez que apareceu o 321
    last_degree = int(data_list[last_target_line]['degrees'])

    # aqui vamos guardar o valor do último ângulo antes do pêndulo
    # inverter a direção de giro.
    max_degree= 0

    for i in data_list[last_target_line + 1:]:
        target = int(i['degrees'])

        # se o valor interior for maior que o atual,
        # significa que o pêndulo atingiu o ponto máximo e
        # está voltado (em sentido anti-horário)
        if last_degree < target:
            max_degree = target
            break

        last_degree = target

    # FIXME: 178 graus é quando o pêndulo está em repouso, próximo
    # da região de impacto, faça com que esse valor seja dinâmico.
    # algo como pedir para que o usuário que coloque o pêndulo próximo
    # ao corpo de prova para realizar o impacto vai servir.
    opening_angle = 178 - last_degree

    print(f"O pêndulo fez uma abertura de {opening_angle} graus")

    # massa do pêndulo
    m = 8.65

    # tamanho do pêndulo
    l = 0.8

    beta = opening_angle

    # qual é a altura que o martelo subiu?
    post_impact_h = lambda l, beta: (l * (1 - cos(beta * (pi / 180))))
    h = post_impact_h(l, beta)
    print(f"Após o impacto, o pêndulo subiu {h:.4}m")

    # FIXME: refaça os cálculos para obter uma nova energia potencial,
    # pois esse valor está baseado no artigo.
    dissipated_energy = 120 - (m * 9.81 * h)

    print(f"A energia dissipada foi de {dissipated_energy:.4}J")

