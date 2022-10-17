#language: pt
Funcionalidade: Splash Screen
  Eu, como usuário do app TODO
  Gostaria, que fosse exibido a tela de Splash Screen
  Porque, vou ter um tutorial das funcionalidades do app

RN 1 - Carrousel com 3 slides
RN 2 - O slide atual deve apresentar uma marcação, indicando assim qual slide eu estou
RN 3 - O carrousel é composto de imagem, título e descrição
RN 4 - O primeiro slide é composto por imagem, título, descrição e 2 botões
    - 1 botão de Create a Note
    - 1 botão de Import Notes
RN 5 - A spash screen deve ser exibida somente na primeira vez que o app for aberto

Contexto: Acessar o aplicativo
  Dado que o app foi aberto
  Quando o carrousel é exibido

#altaprioridade
Cenário: Validar RN 1 - Carrousel com 3 slides
  Então é visualizado 3 slides no carrousel

#altaprioridade
Cenário: Validar RN 2 - Indicar a posição no carrousel
  Então o carousel deve ter indicador dos slides existentes
  E deve apresentar uma cor mais forte no slide em que me encontro

