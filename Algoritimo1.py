def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            print("Item encontrado no índice:", meio)
            return meio
        elif chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1

    print("Item não encontrado")
    return None

minha_lista = [1, 3, 5, 7, 9]
print(pesquisa_binaria(minha_lista, 3))  # Saída: 1
print(pesquisa_binaria(minha_lista, -1)) # Saída: None

""" 
Pesquisa Binária

Oque estamos fazendo nesse código?

Primeiro definimos uma função chamada de "pesquisa_binaria"
depois que fizermos isso vamos criar duas variáveis "baixo" e "alto" para armazenar os índices do início e do fim da lista, respectivamente.

Em seguida, usamos um loop "while" para continuar a pesquisa enquanto o índice "baixo" for menor ou igual ao índice "alto". Dentro do loop, calculamos o índice do meio da lista usando a fórmula (baixo + alto) // 2 e armazenamos o valor correspondente em uma variável chamada "chute".

Em seguida, comparamos o valor do "chute" com o item que estamos procurando. Se o "chute" for igual ao item, retornamos o índice do meio. Se o "chute" for maior que o item, ajustamos o índice "alto" para ser um índice antes do meio, ou seja, meio - 1. Caso contrário, ajustamos o índice "baixo" para ser um índice depois do meio, ou seja, meio + 1.

Se o loop terminar sem encontrar o item, retornamos None para indicar que o item não está presente na lista.

Depois de fizermos isso vamos criar uma lista para que ela seja usada como exemplo para testar a função de pesquisa binária. A lista é [1, 3, 5, 7, 9]

Como assim ? 
A minha_lista ela vai receber os valores 1, 3, 5, 7 e 9. Depois disso, vamos chamar a função "pesquisa_binaria" passando a lista e o item que queremos encontrar como argumentos. No primeiro teste, estamos procurando o número 3, que está presente na lista, então a função retornará o índice 1. No segundo teste, estamos procurando o número -1, que não está presente na lista, então a função retornará None, indicando que o item não foi encontrado.

"""