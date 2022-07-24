## 🚀 Como executar o Crawlers


### Pré-requisitos

Antes de começar, você vai precisar ter instalado em sua máquina as seguintes ferramentas:
[scrapinghub/splash ](https://hub.docker.com/r/scrapinghub/splash), [Python3](https://www.djangoproject.com),
[Documentacao Scrapy](https://docs.scrapy.org/en/latest/).
Além disto é bom ter um editor para trabalhar com o código como [VSCode](https://code.visualstudio.com/)

#### 🎲 Rodando o Crawler1 (com middleware Splash)

```bash

# dentro do Pasta cebrase-crawler 
$ pip install Scrapy
$ pip install scrapy-splash

# rodar Splash no docker
$ docker run -p 8050:8050 scrapinghub/splash

# para rodar crawler1
$ scrapy crawl cebraspe1

# para rodar crawler1 e gerar um arquivo json dos links
$ scrapy crawl cebraspe1 -o links.json

#### 🎲 Rodando o Crawler2 (com middleware selenium)

# dentro do Pasta cebrase-crawler 
$ pip install Scrapy
$ pip install scrapy-selenium

# dependendo do navegador que vc tem instalado pesquisar o webdriver do versao atual de navegador vc tem instalado e configurar o path no setting.py  

# para rodar crawler1
$ scrapy crawl cebraspe2selenium

