# Documento de Visão

## Histórico de revisão

| Data       | Versão | Descrição                      | Autor(es)                                                  |
| ---------- | ------ | ------------------------------ | ---------------------------------------------------------- |
| 15/07/2022 | 0.1    | Abertura do documento de Visão | [Matheus Henrick](https://github.com/MatheusHenrickSantos) |
| 16/07/2022 | 0.2    | Adição dos tópicos 1, 2 e 3    | [Matheus Henrick](https://github.com/MatheusHenrickSantos) |
| 17/07/2022 | 0.3    | Adição dos tópicos 4, 5 e 6    | [Matheus Henrick](https://github.com/MatheusHenrickSantos) |
| 24/07/2022 | 1.0    | Adição do tópico 7             | [Matheus Henrick](https://github.com/MatheusHenrickSantos) |

## 1. Introdução

### 1.1 Objetivo

O objetivo deste documento é detalhar as etapes do desenvolvimento do projeto Cebraspe Tracker, definir o escopo do produto, os requisitos funcionais e não funcionais e os problemas enfrentados na execução.

### 1.2 Escopo

Cebaspre tracker é a solução perfeita para estudantes que estao em processo seletivo tanto pra ajudar as pessoas que perdem sua vaga por falta de entendiento sobre o processo seletivo tanto quanto as pessoas que sofrem de uma ansiedade pesada, para poder tranquiliza-las e tirar das costas dessas pessoas o peso de ficar atualizando todos os dias a pagina do concurso público PAS.

### 1.3 Definições, acrônimos e abreviações

| Abreviação | Significado                                          |
| ---------- | ---------------------------------------------------- |
| _UnB_      | Universidade de Brasília                             |
| _FGA_      | Faculdade UnB Gama                                   |
| _MDS_      | Métodos de Desenvolvimento de Software               |

## 2. Posicionamento

### 2.1 Oportunidade de Negócios

O projeto Cebraspe Tracker surge como uma forma de atacar um problema muito comum em pessoas que buscam entrar na faculdade, que é a perda de chamadas no processo seletivo, o que acaba por gerar um longo processo de preenchimento de vagas e interrompe o sonho de muita gente.

### 2.2 Descrição do Problema

| O problema é | Que afeta | Cujo impacto é | Uma boa solução seria |
| ------------ | --------- | -------------- | --------------------- |
| A perda de chamadas nos processos seletivos | Estudantes em busca de uma vaga na universidade | Estudantes terem o seu sonho de entrar em uma universidade adiado ou encerrado | Notificar os estudantes que foram chamados para o processo seletivo |

### 2.3 Posição do Produto

Destinado a pessoas que estão à espera do resultado do processo seletivo, a fim de evitar que estes percam uma chamada e poupá-los do trabalho de ter que atualizar a página do Cebraspe a todo instante.

## 3. Descrição dos Envolvidos e dos Usuários

### 3.1 Resumo dos envolvidos

| Nome                                  | Descrição                                  | Responsabilidades                 |
| ------------------------------------- | ------------------------------------------ | --------------------------------- |
| Orientadores                          | Professora da disciplina de MDS            | Orientar e guiar a equipe         | 
| Equipe de desenvolvimento de Software | Estudantes da disciplina de MDS da UnB FGA | Desenvolver e gerenciar o projeto |

### 3.2 Descrição dos Usuários

| Nome                                     | Responsabilidades                                        |
| ---------------------------------------- | -------------------------------------------------------- |
| Estudantes em processo seletivo          | Cadastrar-se na plataforma                               | 
| Equipe de desenvolvimento de Software    | Documentar, desenvolver, testar e implementar o software |
| Professora da disciplina de MDS          | Orientar e avaliar o trabalho realizado pela equipe      |

### 3.3 Principais Necessidades dos Usuários e dos Envolvidos

| Usuário | Necessidade | Solução Atual | Solução Proposta |
| ------- | ----------- | ------------- | ---------------- |
| Estudantes | Meio de notificar sobre chamadas em andamento | Verificar constantemente a página do Cebraspe | Enviar notifiação por e-mail |

### 3.4 Ambiente dos Usuários

Os usuários poderão utilizar a aplicação por meio de navegadores web.

### 3.5 Perfis dos Envolvidos

#### 3.5.1 Equipe de Desenvolvimento de Software

| Representantes | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | ---- | ---------------- | ------------------- | ------------ |
| Abdul Hannan, Asafe Salumiel Souza, Gabriel De Souza Fonseca Ribeiro, João Lucas Pinto Vas, Matheus Henrick Dutra | Estudantes de MDS na UnB FGA | Criar e manter documentos; Desenvolver e testar o software | Completar o projeto proposto dentro do período estipulado e atendendo à todos os requisitos | Alto |

#### 3.5.2 Avaliadores

| Representantes | Tipo                         | Responsabilidade                    | Critério de sucesso                                         | Envolvimento |
| -------------- | ---------------------------- | ----------------------------------- | ----------------------------------------------------------- | ------------ |
| Carla Rocha    | Professora de MDS na UnB FGA | Avaliar qualidade do projeto criado | Transmitir conhecimento sobre projetos de software em grupo | Baixo        |

### 3.6 Perfis dos Usuários

| Representantes | Tipo | Responsabilidade | Critério de sucesso | Envolvimento |
| -------------- | ---- | ---------------- | ------------------- | ------------ |
| Interessados em ingressar na universidade | Estudantes em processo seletivo | Cadastrar-se na plataforma | Ser notificado de que seu nome consta na lista de chamada | Baixo |

## 4. Visão Geral do Produto

### 4.1 Perspectiva do Produto

O Projeto visa ser um facilitador do uso da plataforma do Cebraspe, dando segurança e praticidade aos alunos que estão à espera de uma chamada em processos seletivos. Para isso será utilizado a lista que será disponibilizada pelo próprio site, para que se possa realizar uma busca pelo nome de forma automatizada e notificar o usuário via e-mail.

### 4.2 Resumo das capacidades

| Benefício para o Usuário | Recursos de suporte |
| ------------------------ | ------------------- |
| Facilidade em se cadastrar | A aplicação disponibiliza uma interface com um campo para preenchimento do nome, e-mail e telefone, o usuário não terá a necessidade de criar uma conta |
| Segurança na busca pelo nome | A aplicação notificará o estudante em caso deste ser chamado em um processo seletivo |

### 4.3 Funções do Produto

O projeto está encarregado de notificar o usuário caso o nome conste na lista de chamada, dando segurança e acabando com a necessidade de uma busca manual.

### 4.4 Suposições e dependências

- O usuário deverá ter um meio de se conectar à internet para acessar a aplicação.
- O usuário deverá ter um e-mail cadastrado na plataforma.

## 5. Recursos do Produto

Os usuários interessados no projeto terão acesso ao seguinte recurso:
- Ser notificado via e-mail, caso seja chamado.

## 6. Restrições

Listagem de restrições externas e outras dependências:

- Ter um computador.
- Ter conexão à internet.
- Ter um e-mail cadastrado.

### 6.1 Restrições de Implementação

O sistema será implementado utilizando 2 principais tecnologias, sendo elas Django para o backend, webcrawler para leitura do html e React.js para o frontend.

### 6.2 Restrições externas

Dentre as restrições externas as que mais irão influenciar são a falta de experiência com as tecnologias, além de possíveis transtornos entre a equipe de desenvolvimento.

### 6.3 Restrições de Design

Toda a interação com o software deve ocorrer de forma a não causar dúvida no usuário. Para isso será necessário apenas que o usuário informe o nome, e-mail e telefone.

### 6.4 Restrições de Confiabilidade

Visando uma maior manutenibilidade do projeto pela comunidade, os desenvolvedores têm o comprometimento de manter uma cobertura de testes mínima de 90%.

## 7. Requisitos do Produto

### 7.1 Requisitos funcionais

| Identificador | Requisito | Prioridade |
| ------------- | --------- | ---------- |
| RF1           | Permitir que o estudante possa realizar o cadastro, utilizando nome, número de telefone e e-mail | Alta |
| RF2           | O primeiro web crawler deverá ler o html, identificar e salvar o link das consultas online no banco de dados | Alta |
| RF3           | O segundo web crawler deverá ser capaz de pegar um nome cadastrado e utilizá-lo como parâmetro para busca no html do subprograma do PAS | Alta |
| RF4           | O segundo web deverá ser capaz de salvar no banco de dados o html gerado na busca do nome do estudante | Alta |
| RF5           | O segundo web deverá buscar no html gerado o nome do estudante cadastrado | Alta |
| RF6           | A aplicação deverá notificar o estudante cujo nome tenha sido chamado | Alta |
| RF7           | O cadastro do estudante deverá ser removido caso este já tenha sido chamado | Média |

### 7.2 Requisitos não-funcionais

| Identificador | Requisito | Prioridade |
| ------------- | --------- | ---------- |
| RNF1          | A interação com o usuário deve ser feita por meio de interface gráfica | Alta |
| RNF2          | O software será desenvolvido para ambiente web | Alta |
| RNF3          | O software deverá ser desenvolvido utilizando React.js e TypeScript para o Frontend | Alta |
| RNF4          | O software deverá ser desenvolvido utilizando Django e Python para o Backend | Alta |
| RNF5          | O software deverá ser desenvolvido utilizando o PostgreeSQL como banco de dados | Alta |
| RNF6          | O software deverá ser desenvolvido utilizando Selenium e Scrapy para o web crawler | Alta |
| RNF7          | O software deverá ser desenvolvido utilizando a arquitetura MVC | Alta |
| RNF8          | O desenvolvimento da aplicação será containerizado com o Docker | Alta |
