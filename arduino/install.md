### O Arduino

O nosso projeto utiliza a o dispositivo (ou "plaquinha") para
realizar uma rápida prototipagem do sistema que será desenvolvido,
esse protótipo vai capturar informações do veículo através de sensores,
os dados obtidos são tratados, armazenados e transformados em
informações úteis para a equipe, por exemplo o sensor de temperatura
é crucial para sabermos em quantos graus alguns componentes do carro
estão operando.

### IDE (_Integrated Development Environment_)

Para inserir as instruções na plaquinha e torná-la em uma ferramente útil,
primeiro é preciso compreender como o arduino vai interpretar essas intruções
e como elas devem ser feitas.

Nós utilizamos a própria IDE da ferramenta, que por capricho tem a sua própria
API (_Application Programming Interface_), ou seja, conseguimos programar o
arduino com facilidade, basta apenas compreendermos como iremos estruturar as
instruções.

`TODO: fazer um manual de introdução a linguagem.`

### Como instalar?

A instalação do IDE é feito localmente e o binário de instalação pode ser
obtido pelo [site oficial](https://www.arduino.cc/en/software) da plataforma.

Procure pela versão mais recente do software e baixe o instalador referente
ao sistema que estiver utilizando

### Como utilizar

`TODO: explicar a etapa de utilização da protoboard`

Após realizar a instalação do _software_ é interessante que se faça o "olá, mundo!",
um exemplo simples que aprendemos em toda linguagem de programação durante o nosso
primeiro passo.

Basta conectar o cabo do arduino em nosso computador e no arduino, depois disso observe
a aba "_Tools_" da ferramenta, ao clicar nela vamos observar duas opções, a "_Board_" e
"_Port_", se a placa estiver correta e haver uma porta válida, basta apenas fazer o
código e enviar para a placa, o código que vamos utilizar é o seguinte:


```c
const int led = 10;

void setup() {
  pinMode(led, OUTPUT);
}

void loop() {
  digitalWrite(led, HIGH);
}
```

Copie e cole o mesmo no software, pressiona o botão "_Upload_", se tudo ocorreu bem
teremos um led sendo acendido.
