# bot_sequencias_genBank
Um bot em python que faz o download de sequências em XML de alguns arbovírus retiradas do banco de dados [Genbank](https://www.ncbi.nlm.nih.gov/nucleotide/), usando o Chrome como navegador padrão. Uma pequena lista dos vírus disponíveis
|      Para download       |     Para adicionar     |
| ------------------------ | ---------------------- |
| Dengue (todos os tipos)  |       Oropouche        |    
|       Chikungunya        |                        |
|           Zika           |                        |


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

 - Para desativar o ambiente virtual:

       deactivate

## Instalando as bibliotecas
Dentro da pasta do projeto, rodar no terminal:

     pip install -r requirements.txt

## Problemas com o chromedriver
No caso de problemas com o diretório de destino do arquivo com as sequências virais baixadas, ou com erro do driver do tipo: 

`OSError: [Errno 8] Exec format error: /.../.wdm/drivers/chromedriver/.../THIRD_PARTY_NOTICES.chromedriver'`


 algumas alternativas são:
 ### Reinstalar o webdriver-manager
- Desinstalar o webdriver-manager:

       pip unistall webdriver-manager

- Limpar o cache criado pela biblioteca:
   - Linux:

              rm -rf ~/.wdm

   - Windows:
    
            rd /s /q C:\Users\"SeuUsuario"\.wdm

- Reinstalar o webdriver-manager:

       pip install webdriver-manager

### Somente atualizar o webdriver-manager
       pip install --upgrade webdriver_manager

### Além de atualizar, editar arquivo de logs do webdriver-manager

- (na root do seu sistema <b>Linux</b>) navegar até o diretório do webdriver-manager:

       cd /home/seuUsuario/.wdm/

- se quiser visualizar:
  - o conteúdo da pasta: `ls`
  - o arquivo antes de editar: `cat drivers.json`


- para editar o arquivo usando o ambiente do nano:

       nano drivers.json

- no ambiente do nano, apague a entrada referente ao último uso do chromedriver, que provavelmente terá no fim do seu conteúdo algo como:

    `/THIRD_PARTY_NOTICES.chromedriver`

- para salvar no nano:
   
   `Ctrl + O`, `Enter`, `Ctrl + X`

- visualize novamente o arquivo para verificar alterações feitas com o comando do `cat` e se preciso reinicie seu terminal

## No caso de problemas com o download ~ [wip]

<b>Muito comum:</b> fatores como velocidade e estabilidade de internet - o download provavelmente vai ser interrompido

<b>Caso não seja a internet</b>, a possível melhor solução para esse problema é aumentar o `sleep_time`  em milissegundos. O que pode ser feito de 2 formas:
- Na linha 22 do arquivo `main.py` => melhor para testes rápidos

- Na função `arbov_time()` do arquivo `data_handling.py`, onde o `sleep_time` foi definido de acordo com os arbovírus que possuiam o maior número de sequências
       
  > <br>**Atenção:**<br><br>
   Caso você identifique uma melhor lógica para a função de definição desses tempos por vírus, crie uma **PULL REQUEST** para que o merge com a main possa ser feito.


