### PROJETO DE WEB SCRAPING

##### Extrai os dados de Fundos Imobiliarios

* Para executar o projeto em seu computador, primeiro faça git clone do repositório.

`git clone https://github.com/claytoncampos/web-crawler-fundos-imobiliarios.git`

* Instale as dependências executando o comando abaixo.

`pip install -r requirements.txt` 

* Navegue até o diretorio \fiinvest

`cd .\web-crawler-fundos-imobiliarios`

* Execute o comando abaixo para rodar o crawler.

`scrapy crawl fiis -o fiis.json`

<b>OBS:</b> <i>Mude a extensão do arquivo de acordo com sua necessidade <b>.json .xml ou .csv</b>

Após a execução o arquivo de extração será gerado no diretorio raiz do projeto


