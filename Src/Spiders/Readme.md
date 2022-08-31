# como rodar e instalar local server ScrapyD e ScrapyD-Client

```
pip install scrapyd
pip install scrapyd-client   

```
## para rodar local server no terminal
```
scrapyd
```

## para adcionar projetos do spider em local host
### no arquivo .cfg descomentar localhost server e no deploy adcionar nome apleido desejado
### EX:

```
[Deploy:local]
```
## para adcionar dentro do scrapyD  (tem que ser dentro do pasta de crawler)
```
scrapyd-deploy local

```
## como Agendar Crawler usando curl
### baixar curl pelo no https://curl.haxx.se/ (baixa versao dependendo do versao sistema operacional)

### dentro do pasta no terminal 
```
cd curl/bin
curl http://localhost/schedule.json -d project=nomedoProjeto -d spider=NomeDoSpider
```

## para melhor entendimento ver o docs do ScrapyD
[docs ScrapyD](https://scrapyd.readthedocs.io/en/stable/)  tem muito informacao como agendar e cancelar etc.....
