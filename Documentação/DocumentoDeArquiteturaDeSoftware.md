<!-- <p align="center">
  <img 
    src="https://github.com/fga-eps-mds/GFour-Invext/blob/main/docs/assets/msg1187136684-18592.jpg"
    alt: 'Logo Invext'
    width="1000"
    height="150"
  />
</p> -->

<h1 align="center"><b>DOCUMENTO DE ARQUITETURA DE SOFTWARE</b></h1>

## Histórico de revisão

| Data       | Versão | Descrição                      | Autor(es)                                                  |
| ---------- | ------ | ------------------------------ | ---------------------------------------------------------- |
| /07/2022 | 0.1    | Abertura do documento de Visão | [Abdul hannan](https://github.com/hannanhunny01)             |
| 24/07/2022 | 0.2    | Atualizacao do documento de Visão | [Abdul hannan](https://github.com/hannanhunny01)           |
 




## **INTRODUÇÃO**



1. ### _**VISÃO GERAL**_

   O documento de arquitetura está organizado em informações da seguinte maneira:

   1. Finalidade
   2. Escopo
   3. Metas e Restrições de Arquitetura
   4. Visão dos Casos de Uso
   5. Visão Lógica
   6. Visão de Processos
   7. Visão de Implantação
   8. Visão de implementação
   9. Tamanho e Desempenho
   10.Qualidade



2. ### _**FINALIDADE**_

   Cebraspe Tracker é uma funcionalidade a qual vai funcionar em uma pagina web e é baseada em web crawler. O site vai ser criado com intuito de ajudar estudantes que estão em processo seletivo, mais especificamente o PAS pois o mesmo acaba tendo varias chamadas e muitos alunos acabam perdendo sua vaga, por isso o Cebraspe Tracker vai ajudar essas pessoas, as pessoas ao se cadastrarem no site elas seriam informados via email e whatsapp caso fossem aprovadas..

3. ### _**ESCOPO**_

   Cebaspre tracker é a solução perfeita para estudantes que estao em processo seletivo tanto pra ajudar as pessoas que perdem sua vaga por falta de entendiento sobre o processo seletivo tanto quanto as pessoas que sofrem de uma ansiedade pesada, para poder tranquiliza-las e tirar das costas dessas pessoas o peso de ficar atualizando todos os dias a pagina do concurso público PAS.


4. ### _**CONFIGURAÇÕES, ACRÔNIMOS E ABREVIAÇÕES**_

   - API: É um acrônimo para Application Programming Interface(Interface de programação de aplicações). A API é um conjunto de definições e protocolos usados no desenvolvimento e na integração de um software, permitindo a interação com outros produtos sem a necessidade de interação com outro software.
   - UML: É um acrônimo para Unified Modeling Language(linguagem de modelagem unificada). O UML é uma linguagem utilizada para visualizar, especificar, construir e documentar a arquitetura completa de um software, fornecendo informações detalhadas para o desenvolvedor implementar o software.
   - UI: É uma sigla para User Interface(interface do usuário). É a área que está associada a criação das interfaces que interagem diretamente com o usuário do software, promovendo formas fáceis e amigáveis de interação no programa.

5.  ### _**REPRESENTAÇÃO ARQUITETURAL**_

- Front-end:
   - React: É um conjunto de bibliotecas de código aberto seguro para a criação de UIs interativas de forma mais fácil. Toda lógica é escrita em JavaScript da Repassagem de dados ao longo da passagem de dados. Essa tecnologia foi escolhida por quantidade de conteúdo disponível na internet, para o treinamento e aprendizado da equipe, outro ponto positivo é o fórum de dúvidas acerca do assunto estar sempre a disposição.
- Back-end:
   - Django REST framework (DRF) é um kit de ferramentas poderoso e flexível para construir APIs da Web. Seu principal benefício é que torna a serialização muito mais fácil.
O framework Django REST é baseado nas visualizações baseadas em classes do Django, então é uma excelente opção se você estiver familiarizado com o Django. Ele adota implementações como visualizações baseadas em classes, formulários, validador de modelo, QuerySet e muito mais.
  - Scrapy-selenium é um middleware que é usado em web scraping. scrapy não suporta a scraping dos sites modernos que usam estruturas javascript e esta é a razão pela qual esse middleware é usado com scrapy para crawl esses sites modernos. O Scrapy-selenium fornece as funcionalidades do selenium que ajudam no trabalho com sites javascript. Outra vantagem proporcionada por isso é o driver pelo qual também podemos ver o que está acontecendo nos bastidores. Como o selênium é uma ferramenta automatizada, ele também nos fornece como lidar com tags de entrada e scrap de acordo com o que você passa no campo de entrada.


6. ### _**METAS E RESTRIÇÕES DA ARQUITETURA**_
- Restrições:
  - Software deve ser desenvolvido nas tecnologias;
  - O ambiente de desenvolvimento do software deve funcionar tanto em windows, linux e MacOS;
  - Para usar o Software é necessário Internet;
  - O escopo final deve ser concluído até o final da disciplina;
- Metas:
   - **Usabilidade** - O Software deve possuir alta aprendizagem e performance para atender os requisitos elicitados pelo grupo;
   - **Manutenção** - O código e as documentações realizadas devem estar num nível de qualidade, seguindo os padrões do projeto e bibliografia, onde sua manutenção seja fácil de ser realizada.

8. ### _**VISÃO DE CASOS DE USO**_

   Para representar os Casos de Uso do sistema especificado, foi criado um diagrama de casos de uso que exibe os pontos principais do sistema.

9. ### _**VISÃO LÓGICA**_

   A visão lógica descreve como o sistema é compatível, em termos de unidade e implementação. Mostra como é uma organização conceitual do sistema em termos de camadas, pacotes, classes e interfaces. O relacionamento entre os elementos mostra como dependências e interface, os relacionamentos parte assim por diante.

- Diagrama de Aulas

   O diagrama representa como as classes serão programadas, os principais objetos ou realmente como diagrama completo pode ser encontrado na parte de Diagrama de Classes na wiki do projeto.

- Diagrama de Pacotes

   O diagrama de pacotes é um diagrama estático que possibilita uma organização mais adequada ao sistema que representa uma versão de pacotes. O diagrama completo pode ser encontrado na parte de Diagrama de Pacotes da wiki do projeto.

- Diagrama de Comunicação

   O diagrama de comunicação mostra partes de comunicação entre objetos e/ou (representadas pela lifelines usando mensagens sequenciadas um arranjo) de forma livre. O diagrama completo pode ser encontrado na parte de Diagrama de Comunicação na wiki do projeto.

10. ### _**VISÃO DE PROCESSOS**_
- Visão geral:

   De tempo-de-execução como o sistema de execução de tempo-de-execução é construído na forma de um conjunto de tempo-de-execução que tem como modelo de comportamento de execução. Uma estrutura de tempo-de-execução normalmente tem semelhança com uma estrutura de código. Consistência de redes de comunicação rápida de objetos de comunicação.

- Diagrama de Sequência:

   O diagrama de sequência é uma das soluções fornecidas pela UML, que descrevem quimicamente o ciclo de vida do sistema em desenvolvimento. Descrição detalhada. O foco principal deste diagrama é descrito como troca entre os componentes do sistema e módulos que existem de uma maneira determinada e mensagens entre si. Os ciclos de vida podem ser aulas, atores ou mesmo abstrações que ocorrem entre aulas.

11. ### _**VISÃO DE IMPLANTAÇÃO**_
      Descreve como a aplicação é disponibilizada para uso, seja em um ambiente de desenvolvimento, para testes ou em produção.

12. ### _**VISÃO DE IMPLEMENTAÇÃO**_
   - Visão Geral:

Descreve como os defensores do desenvolvimento estão organizados no sistema de arquivos. Os elementos são arquivos e pastas(Quaisquer itens de configuração). Isto inclui as propriedades de desenvolvimento e os riscos de implantação.

   - Diagramas de Aulas:

É uma representação da estrutura e relações das classes que servem de modelo para os objetos. Consiste em um conjunto de objetos com as mesmas características. Dessa forma, consegue-se identificar os objetos agrupá-los, de forma a encontrar suas classes conhecidas

13. ### _**Diagrama de Classes**_
    Essa é a primeira versão das classes no diagrama de classe do projeto Cebraspe-Tracker.
    <p align="center">
  ![Diagrama de classes](https://github.com/fga-eps-mds/Cebraspe-Tracker/blob/main/Documenta%C3%A7%C3%A3o/Assets/DiagramaDeClasses.png)
  
</p>

13. ### _**Diagrama de Pacotes**_
    Essa é a primeira versão das classes no diagrama de Pacotes do projeto Cebraspe-Tracker.
      <p align="center">
  ![Diagrama do Pacotes](https://github.com/fga-eps-mds/Cebraspe-Tracker/blob/main/Documenta%C3%A7%C3%A3o/Assets/DiagramaDePacotes%20.png)
  ![Diagrama do Pacotes2](https://github.com/fga-eps-mds/Cebraspe-Tracker/blob/main/Documenta%C3%A7%C3%A3o/Assets/DiagramaDePacotes2.png)
  
</p>
    




   


