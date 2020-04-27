# Lista de exercícios - Lição 9

## :star2: 01 - Implementação de Pilha

**Importante:** 
1. Renomear o arquivo `stack.py` para `lists.py`
1. Conferir se o arquivo `__init__.py` na raiz da blioteca possui a seguinte linha de código
```
from .lists import *
```
Implementar uma **fila** utilizando as funções mais básicas do array. Evite simplesmente criar um "wrapper" para os métodos existentes do array.

Implemente a fila controlando as posições iniciais e finais de acordo com o examplo: https://www.cs.usfca.edu/~galles/visualization/QueueArray.html

1. Dentro do arquivo `lists.py` em sua pasta da biblioteca crie uma classe Queue que implemente os principais métodos da fila (aula 5 slide 18).
1. Execute os testes unitários disponibilizados pelo professor para garantir que está tudo em ordem.

## 02 - Encontrar o número desejado

Para adentrar em um recinto secreto é necessário conhecer o número desejado. Para identificá-lo você recebeu as segunintes instruções:

1. Adicione os números de 1 a 10 em uma pilha
1. Depois remove os 3 primeiros números
1. Adicione os números de 1 a 5
1. Remova 8 números

O último número retirado da pilha é o número desejado. Qual foi?

Utilize sua implementação de pilha para resolver este mistério.

## 03 - Decodifcar a mensagem

Você interceptou duas informações para decodificar uma mensagem. A primeira é uma string e a segunda é uma sequência de inteiros conforme abaixo:

* String => ojrggcfetscrapeooukeszwtteaof-dbcobteqrrjttsmfslua
* Sequência de números => 3, 5, 2, 4, 3, 4, 4, 2, 3, 3, 4, 3, 3, 7

Para decodificar a mensagem você deve enfileirar todos os números, e desinfilar-los de acordo com a sequência de números.

Por exemplo: Após desisnfileirar 3 posições, a primeira letra optida será "r".

Para decodificar esta mensagem utiliza sua implementação de fila.
