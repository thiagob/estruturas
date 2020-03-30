# Lista de exercícios - Lição 4

## 01 - Fibonacci iterativo e recursivo

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


## 02 - Substituição de caracter (recursivo)

Desenvolva uma função/procedimento *recursivo* que receberá uma string como parâmetro, e que imprime a frase cada vez substituindo uma letra diferente por *.

Exemplo: `"Você recebe esta frase"`

E seu método deverá imprimir:

`"*ocê recebe esta frase"`
`"V*cê recebe esta frase"`
`"Vo*ê recebe esta frase"`
`"Voc* recebe esta frase"`

E assim sucessivamente até que todas as letras tenham sido substituídas.