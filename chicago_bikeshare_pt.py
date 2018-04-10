# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos
print("Número de linhas:")
print(len(data_list))

# Imprimindo a primeira linha de data_list para verificar se funcionou.
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.

# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados
print("Linha 1: ")
print(data_list[1])

input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
for i, data in enumerate(data_list[1:21]):
    print("Linha {} -> {}".format(i + 1, data))

# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")
# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
for i, data in enumerate(data_list[:20]):
    print("Linha {} -> gênero {}".format(i + 1, data[6]))


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem
def column_to_list(data, index):
    """
    Função que adiciona as colunas(features) de uma lista em outra lista, na mesma ordem.
      Argumentos:
          data: A lista de dados (list).
          index: O indice da coluna (int).
      Retorna:
          Uma lista com os valores da coluna escolhida pelo indice 'index'
    """
    column_list = []
    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    for sample in data:
        column_list.append(sample[index])
    return column_list


# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função parTODO isso.
male = 0
female = 0
vazio = 0
gender_list = column_to_list(data_list, -2)
for gender in gender_list:
    if gender == "Male":
        male += 1
    elif gender == "Female":
        female += 1
    else:
        vazio += 1

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)
print('Quantidade de amostras com gêneros faltando: ' + str(vazio))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Por que nós não criamos uma função parTODO isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)
def count_gender(data_list):
    """
    Função que conta a quantidade de cada gênero em uma lista.
      Argumentos:
          data_list: A lista de gêneros (list).
      Retorna:
          Uma lista com as quantidades de homem e mulher, no formato [qntd_male, qntd_female].
    """
    male = 0
    female = 0
    for data in data_list:
        if data[-2] == "Male":
            male += 1
        elif data[-2] == "Female":
            female += 1
    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """
    Função que retorna o gênero mais popular de uma lista de gêneros.
      Argumentos:
          data_list: lista de gêneros (list).
      Retorna:
          Uma string com o gênero mais popular:
          "Male" caso o masculino, "Female" caso o feminino e "Equal" caso iguais.
    """
    answer = ""
    count_g = count_gender(data_list)
    if count_g[0] > count_g[1]:
        answer = "Male"
    elif count_g[0] < count_g[1]:
        answer = "Female"
    else:
        answer = "Equal"
    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")

user_types_list = column_to_list(data_list, -3)
types = ["Customer", "Dependent", "Subscriber"]
quantity = [user_types_list.count("Customer"), user_types_list.count("Dependent"), user_types_list.count("Subscriber") ]

print("Customer:{}\nDependent:{}\nSubscriber:{}".format(quantity[0], quantity[1], quantity[2]))

y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Tipos de usuários')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de usuário')
plt.show(block=True)

input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Por que existem {} amostras sem a informação de gênero.".format(vazio)
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0.
max_trip = 0.
mean_trip = 0.
median_trip = 0.

# Iniciando as variáveis
min_trip = float(trip_duration_list[0])
max_trip = float(trip_duration_list[0])
sum_trip = 0

# Fazendo os elementos da lista virarem float
trip_duration_list = list(map(float,trip_duration_list))

# Buscando max, min e realizando a soma
for trip in trip_duration_list:
    sum_trip += trip

# Ordenando para achar o mediana, também poderia ser usada para achar o min e max, pegando o primeiro e último elemento.
trip_duration_list_orden = sorted(trip_duration_list)
length_list = len(trip_duration_list)

# Arredondando a saída
max_trip = round(trip_duration_list_orden[len(trip_duration_list_orden) - 1])
min_trip = round(trip_duration_list_orden[0])
mean_trip = round(sum_trip/length_list)
median_trip = int(trip_duration_list_orden[length_list // 2])

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------

input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:/
"""
Função de exemplo com anotações.
  Argumentos:
      param1: O primeiro parâmetro.
      param2: O segundo parâmetro.
  Retorna:
      Uma lista de valores x.
"""

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
print("Você vai encarar o desafio? (yes ou no)")
answer = "yes"

def count_items(column_list):
    """
    Função que conta a ocorrência de cada item diferente em uma lista, sem ser necessário definir os itens.
      Argumentos:
          column_list: A lista de itens (list).
      Retorna:
          Uma tupla (item_types, count_items):
                item_types - os tipos diferentes de itens na lista.
                count_items - quantidade de cada tipo de itens na lista.
    """
    items_set = set(column_list)
    # print(items_set)
    item_types = []
    count_items = []
    for item in items_set:
        item_types.append(item)
        count_items.append(column_list.count(item))
    return item_types, count_items


if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, -2)
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------


input("Aperte Enter para continuar...")
print("\nTAREFA EXTRA: Mostrando as 5 estações mais visitadas")
# TAREFA EXTRA
# TODO: Mostre as 5 start_stations mais populares, ou seja, as start_stations
# que tem maior quantidade de usuarios saindo dela
start_stations_list =  column_to_list(data_list, 3)
stations, quantity = count_items(start_stations_list)
start_stations_count = list(zip(quantity, stations))
start_stations_count = sorted(start_stations_count, reverse=True)
top5 = start_stations_count[:5]
quantity, stations = zip(*top5)

print('As 5 estações de saida com maior frenquência de usuários são')
for i, station in enumerate(stations):
    print('{} - {}'.format(i+1, station))

y_pos = list(range(len(stations)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Estações de partida')
plt.xticks(y_pos, stations)
plt.title('Quantidade por Estação')
plt.show(block=True)
