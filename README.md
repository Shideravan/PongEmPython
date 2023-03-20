# Jogo Pong em Python
Este é um projeto simples que usa o módulo turtle do Python para criar um jogo Pong. O jogo consiste em duas raquetes que se movem verticalmente nas bordas da janela e uma bola que se move horizontalmente e verticalmente. O objetivo do jogo é impedir que a bola saia da janela usando as raquetes. Cada vez que a bola sai da janela pelo lado oposto à raquete do jogador, o outro jogador ganha um ponto. O placar é mostrado na parte superior da janela.

## Requisitos
Para rodar este projeto, você precisa ter o Python 3 ou superior instalado no seu computador. Você pode baixar o Python no site oficial: <https://www.python.org/downloads/>

Você também precisa ter o módulo turtle instalado no seu computador. O módulo turtle é uma biblioteca gráfica padrão do Python que permite criar desenhos e animações usando objetos chamados turtles (tartarugas). Você pode instalar o módulo turtle usando o pip, que é um gerenciador de pacotes do Python. Para isso, abra o terminal ou o prompt de comando e digite:

```
pip install turtle
```

## Como executar
Para executar este projeto, você pode usar um editor de texto ou uma IDE (Integrated Development Environment) que suporte a linguagem Python, como o VS Code, o PyCharm ou o Jupyter Notebook. Você pode escrever ou copiar o código em um arquivo com a extensão .py e depois executá-lo usando a opção Run ou pressionando uma tecla de atalho.

Você também pode usar o terminal ou o prompt de comando do seu sistema operacional. Você pode navegar até a pasta onde está o seu arquivo .py e depois digitar:

```
python pong.py
```

Isso vai rodar o código e abrir a janela do jogo.

## Como jogar
Para jogar este jogo, você precisa usar as teclas do teclado para mover as raquetes. O jogador A usa as teclas “w” e “s” para mover a raquete A para cima e para baixo, respectivamente. O jogador B usa as teclas “Up” e “Down” para mover a raquete B para cima e para baixo, respectivamente. O jogador B usa as teclas “Up” e “Down” para mover a raquete B para cima e para baixo, respectivamente.

O jogo termina quando um dos jogadores alcança 10 pontos ou quando você fecha a janela do jogo.

## Partes do código
O código deste projeto está dividido em várias partes:

- Importação do módulo turtle
- Criação da janela do jogo
- Criação da bola
- Criação das raquetes A e B
- Criação do placar
- Definição das variáveis para guardar os pontos dos jogadores
- Definição das funções para mover as raquetes
- Associação das teclas do teclado às funções de movimento das raquetes
- Limite de movimento vertical das raquetes
- Loop principal do jogo

Cada parte está comentada no código com uma breve descrição.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.
