FindNaValues

Para executar o código é necessário:

    - incluir o arquivo que será processado na pasta input.

    - informar os argumentos de acordo com a lista abaixo:

        -filename - o nome do arquivo que será processado. É importante que ele não tenha espaços no nome, pois o código entenderá como um novo argumento e dará erro.
        -sep - identificador de nova coluna
        -dec - identificador de casa decimal
        -navalues - lista com o que será considerado como valor nulo no arquivo.

    - exemplo de chamada do código no prompt:
        python main.py -filename CC GENERAL.csv -sep ; -dec , -navalues ? NaN None

    - o arquivo processado será escrito na pasta output.

    - é necessário que tenha as bibliotecas pandas e argparse instaladas no ambiente, caso não tenha, instalar utilizando os seguintes comandos no prompt:
        pip install argparse
        pip install pandas