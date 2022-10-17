#language: pt
Funcionalidade: Splash Screen
  Eu, como usuário do app TODO
  Gostaria, que fosse exibido a tela de Splash Screen
  Porque, vou ter um tutorial das funcionalidades do app

Contexto: Acessar o aplicativo
  Dado que o app foi aberto
  Quando o carrousel é exibido

#altaprioridade
Cenário: Validar os slides do carrousel
  Então é visualizado 3 slides no carrousel

#altaprioridade
Cenário: Primeiro slide do carrousel
  Então a opção de Create a Note e Import Notes deve ser exibido

