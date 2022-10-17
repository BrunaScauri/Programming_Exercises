#language: pt
Funcionalidade: Splash Screen
  Eu, como usuário do app TODO
  Gostaria, que fosse exibido a tela de Splash Screen
  Porque, vou ter um tutorial das funcionalidades do app

Contexto: Acessar o aplicativo
  Dado que o app foi aberto
  Quando o carrousel é exibido

#altaprioridade
Cenário: Validar RN 1 - Carrousel com 3 slides
  Então é visualizado 3 slides no carrousel

#mediaprioridade
Cenário: Validar RN 2 - Indicar a posição no carrousel
  Então o carousel deve ter indicador dos slides existentes
  E deve apresentar uma cor mais forte no slide em que me encontro

#mediaprioridade
Cenário: Validar RN 3 - Composição do carrousel
  Então deve ser exibido uma imagem
  E um título
  E uma descrição

#baixaprioridade
Cenário: Validar RN 4 - Validar o primeiro slide do carrousel
  Então deve ser exibido um botão de Create a Note
  E um botão de Import Notes

#baixaprioridade
Cenário: Validar RN 5 - Exibis splash screen
  Então a spash screen deve ser exibida somente na primeira vez que o app for aberto

#

Cenário: Validar RN 3 - Listar as tarefas de acordo com o filtro
  Quando clico  em uma opção do filtro
  Então as tarefas relacionadas a ele são exibidas

Esquema do Cenário: Validar RN 3 - Listar as tarefas de acordo com o filtro
  Então as tarefas são exibidas
  Quando clico no filtro <nome do filtro>
  Então as tarefas relacionadas a ele são exibidas

Exemplos:
|nome do filtro|
| Today's Task |
| Monthy Tasks |
| Yearly Tasks |