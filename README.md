# bot_sequencias_genBank
Um bot em python que faz o download de sequências em XML de alguns arbovírus (dengue todos os tipos, chikungunya e zika) retiradas do banco de dados [Genbank](https://www.ncbi.nlm.nih.gov/nucleotide/), usando o Chrome como navegador padrão

teste

## Sobre o navegador
Para usuários de Linux sem o Chrome instalado, acessem [aqui](https://www.edivaldobrito.com.br/instalar-google-chrome-no-ubuntu/) um simples tutorial

## Criação de um ambiente virtual
 - Dentro da pasta do projeto, rodar no terminal:
    
        python3 -m venv "nome do ambiente virtual"

 - Para ativar o ambiente virtual:
   - Linux:

            source "nome do ambiente virtual"/bin/activate

   - Windows:
    
            "nome do ambiente virtual"\Scripts\activate.bat


## Instalando as bibliotecas
Dentro da pasta do projeto, rodar no terminal:

     pip install -r requirements.txt

## No caso de problemas com diretório
No caso de problemas com o diretório de destino do arquivo com as sequências virais baixadas, algumas alternativas são:
- Desinstalar o webdriver-manager:

       `pip unistall webdriver-manager`

- Limpar o cache criado pela biblioteca:
   - Linux:

            rm -rf ~/.wdm

   - Windows:
    
            rd /s /q C:\Users\"SeuUsuario"\.wdm

- Reinstalar o webdriver-manager:

       `pip istall webdriver-manager`
