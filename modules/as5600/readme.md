### AS5600

Esse módulo é um sensor que determina o ângulo do eixo através de um ímã
que será fixo ao eixo de rotação de um objeto que desejamos mensurar o
quanto ele girou.

Os dados são passados pelo sensor numa resolução de 12 bits, ou seja,
temos 4096 posições possíveis a serem inspecionadas durante o giro,
essas 4096 posições nos dá uma precisão de aproximadamente 0.08789 graus.

A comunicação é dada através da interface I2C do microcontrolador a ser
utilizado, então deve-se verificar no datasheet ou na web para utilizar os
pinos SDA, SCL e CS corretamente.

### Como utilizar

A biblioteca que utilizamos é a [AS5600](https://github.com/RobTillaart/AS5600)
, no momento que estou escrevendo este "manual" é a única que aparece no
gerenciador de biblioteca.

Faça o passo padrão, que é instalar a biblioteca e em um novo código, importar
a mesma. Crie um objeto AS5600, no topo do código (ou seja: global) e os
métodos que vão no `setup` são: begin e setDirection.

Há 2 métodos que podem pegar informações a respeito da posição do ímã, são
eles: readAngle e rawAngle.

Se quiser o ângulo em graus, basta multiplicar o valor retornado pelo
rawAngle pela macro AS5600_RAW_TO_DEGREES.

Nessa mesma pasta há um [código]() que está sendo utilizado para obtenção
de dados no teste de impacto de charpy, ele serve como exemplo de uso
dessa biblioteca.
