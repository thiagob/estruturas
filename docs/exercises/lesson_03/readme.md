# Lista de exercícios - Lição 3

## 01 - Multiplicação usando apenas somas

Implemente uma função que recebe 2 números (a, b) e retorna a multiplicação de a * b, porém sem fazer uso da operação básica de *.

## 02 - Números primos 

Desenvolva um algoritmo para imprimir todos os números primos menores que 100.

> A definição mais comum é que "um número é primo se for divisível por 1 e por ele mesmo" ou então "é todo o número com dois e somente dois divisores, ele próprio e a unidade". Sendo assim, por exemplo, o número 7 é primo por ser divisível apenas por 1 e por 7. Já o número 6 não é primo porque é divisível por 1, 2, 3 e 6.
> **E o número 1, é primo?**
Tendo em conta a explicação anterior, a resposta é não. Uma vez que o número 1 apenas tem um divisor.
> **E o número 0, é primo?**
Utilizando a mesma definição, a resposta continua a ser não. Já que um número primo é divisível por ele próprio e zero não pode ser dividido por zero, já que 0/0 é uma indeterminação.

## 03 - Fibonacci iterativo e recursivo

Implemente 2 soluções para a sequência de fibonacci no arquivo `math.py` dentro de sua biblioteca:

* Dentro do método `fibonacci_r(n)` faça a implementação recursiva
* Dentro do método `fibonacci_i(n)` faça a implementação iterativa

> Na matemática, a Sucessão de Fibonacci (também Sequência de Fibonacci), é uma sequência de números inteiros, começando normalmente por 0 e 1, na qual, cada termo subsequente corresponde à soma dos dois anteriores. 

> Em termos matemáticos, a sequência é definida recursivamente pela fórmula abaixo:
> `Fib(n) = Fib(n-1) + Fib(n-2)`
> Sendo que Fib(0) = 0 e Fib(1) = 1

Depois de implmentar os 2 métodos:

1. Avalie qual implementação apresenta melhor performance em termo de tempo de execução? (Tente utilizar números maiores como 50)
1. Efetue a execução dos testes unitários e garanta que sua biblioteca está corretamente configurada


## 04 - Substituição de caracter (recursivo)

Desenvolva uma função/procedimento *recursivo* que receberá uma string como parâmetro, e que imprime a frase cada vez substituindo uma letra diferente por *.

Exemplo: `"Você recebe esta frase"`

E seu método deverá imprimir:

`"*ocê recebe esta frase"`
`"V*cê recebe esta frase"`
`"Vo*ê recebe esta frase"`
`"Voc* recebe esta frase"`

E assim sucessivamente até que todas as letras tenham sido substituídas.

## 05 - Gerar uma lista de inteiros

No arquivo `generators.py` implemente o método `generate_list_of_ints` de forma que ele returno uma lista de números inteiros randômicos.

A lista deverá ter o tamanho de `length` e os números gerados não podem ser maiores que `max_number`.

Por exemplo, para `generate_list_of_ints(5, 10)` um resultado possível poderia ser `[3, 9, 10, 1, 2]`.

Execute novamente os testes unitários, agora todos devem estar "verdes".