# Diário de Bordo de IA - Kev

## 20/03/2026

### Dificuldade encontrada
Meu programa executava uma vez e finalizava. Eu queria que ele ficasse rodando até eu digitar QUIT.

### Solução que encontrei
Adicionar loop no meu código do gestor de portfolio. Colocar while comando.upper() != "QUIT" faz o programa rodar até eu digitar QUIT.

### O que eu aprendi
Aprendi que o while repete tudo que está dentro dele. Usei comando.upper() para funcionar tanto com QUIT maiúsculo quanto quit minúsculo.


## 25/03/2026

### Dificuldade encontrada
Queria que o usuário pudesse cadastrar vários projetos de uma vez, não um por um.

### Prompt enviado para a IA
"como fazer para o usuario digitar quantos projetos quer cadastrar e depois digitar o nome de cada um?"

### Resposta da IA (Resumo)
Foi-me ensinado a usar um for dentro do ADD. Primeiro pergunta a quantidade, depois repete a pergunta do nome usando for i in range(1, quantidade + 1).

### O que eu aprendi
Aprendi que o for serve para repetir algo um número específico de vezes. Usei range para contar do 1 até a quantidade que o usuário pediu.


## 28/03/2026

### Dificuldade encontrada
O programa quebrava se o usuário digitasse letras no lugar do número de projetos.

### Prompt enviado para a IA
"como verificar se o usuario digitou um numero sem usar vários != "numero"?"

### Resposta da IA (Resumo)
A IA ensinou a usar o isdigit(), que verifica se a string só tem números.

### O que eu aprendi
Aprendi que isdigit() retorna True se o usuário digitou um número e False se digitou letras.


## 01/04/2026

### Dificuldade encontrada
O programa aceitava número negativo ou zero. Não faz sentido cadastrar -5 projetos.

### Prompt enviado para a IA
"como impedir o usuario de digitar numero negativo ou zero?"

### Resposta da IA (Resumo)
Ensinou que if quantidade <= 0: serve para verificar e mostrar mensagem de erro.

### O que eu aprendi
Aprendi que programar é também pensar nos erros que o usuário pode cometer. Sempre devo verificar se o número faz sentido antes de usar.


## 05/04/2026

### Dificuldade encontrada
Queria que o programa aceitasse "quit", "QUIT" ou "Quit" do mesmo jeito.

### Solução que encontrei
Usar .upper() converte tudo para maiúsculo antes de comparar.


## 13/04/2026

### Alterações realizadas
Alterei algumas características do código para ficar melhor estruturado, como:

Troquei `while comando.upper() != "QUIT":` para `While True` porque `elif comando.upper() == "QUIT"` já funciona como um verificador de variações na escrita de um comando.

Com pesquisa e ajuda da IA, descobri que posso utilizar `if not projetos` ao invés da contagem de projetos armazenados, apresentando boas práticas e tornando o código mais elegante.

Substitui todas as funções elif com upper, e dexei a formatação dele no campo de `comando` para deixá-lo mais limpo e simples.



## 15/04/2026
### OBS: Na última atividade FORMATIVA que enviei, não foi o diario atualizado, essa parte ficou de fora, peço que me perdoe.
### Dificuldade encontrada
A lista de strings era limitada. Eu não conseguia guardar se o projeto estava pronto ou ver o que mudei nele ao longo do tempo. Precisava de uma estrutura que aceitasse múltiplos dados para um mesmo item.

### Alterações realizadas
Refatorei o modelo de dados para parar de usar uma lista simples de textos e passar a usar uma lista de dicionários. Agora, cada projeto é um objeto com nome, status, um histórico e um campo de observação.

Comando UPDATE: Implementei a lógica de busca para encontrar um projeto pelo nome e permitir a alteração de seus dados.

Comando DELETE: Adicionei a funcionalidade de remover um projeto específico da lista usando o método .remove().

Histórico com Tuplas: Para cada mudança, o sistema salva uma tupla imutável dentro de uma lista de histórico, registrando o que foi alterado.

### O que eu aprendi
Dicionários: Aprendi que chaves e valores são perfeitos para representar "objetos" do mundo real.

Tuplas: Entendi que elas são ideais para logs e históricos, pois os dados não devem ser alterados depois de registrados.

Refatoração: Aprendi que mudar a estrutura principal do código (o modelo de dados) exige atenção para atualizar todos os comandos que dependiam da estrutura antiga (LIST e ADD), mas deixa o sistema muito mais profissional.

Consultas à IA: Usei a IA para ajustar a sintaxe da busca dentro da lista de dicionários e para validar a melhor forma de organizar o histórico de mudanças de maneira limpa.



## 29/04/2026

### Dificuldades encontradas
A principal dificuldade consistiu em determinar qual seria a arquitetura ideal para integrar as novas funcionalidades sem comprometer a simplicidade original do projeto. Para mim, o maior desafio foi implementar a "memória" de dados de uma forma eficiente para o usuário final.


### Alterações realizadas
A maior mudança foi fazer o programa "lembrar" dos projetos mesmo após ser fechado. Agora também há um carregamneto otimizado. Antes de iniciar o menu principal, o programa tenta ler o arquivo portfolio.json, já que a lista é convertida para o formato JSON e gravada no disco.

Salvamento ao sair: Quando o usuário escolhe a opção QUIT, a lista atual de projetos é convertida para o formato JSON e gravada no disco.

Para tratamento de erros:  Implementei mecanismos para que o programa não pare de funcionar caso ocorra algo inesperado, usei blocos try... except para lidar com casos onde o arquivo de dados ainda não existe.


### Adições bônus:
com ajuda da ia, foi-me explicado a melhor maneira de adicionar recursos que ajudam a analisar os dados armazenados, utilizando:

Estatísticas(STATS): Uma função que percorre a lista e calcula quantos projetos estão prontos, quantos estão pendentes e qual foi o último nome finalizado.

Busca(SEARCH): Um filtro que permite encontrar projetos pelo nome, ignorando um pequeno registro das altrações feitas em seu status ou nome.

### O que eu aprendi
Entendi sobre o ciclo de vida de um software. Aprendi que um programa profissional vai além da lógica básica, ele precisa ser eficiente para não quebrar, e útil para fornecer os insights corretos. A prática da depuração e a leitura detalhada das instruções foram essenciais para conquistar a qualidade e autoria do meu trabalho.
