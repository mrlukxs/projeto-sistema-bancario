nome = "Pedro"
idade = 23
profissao = "Data Analist/ Data Scientist"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Pedro", "idade": 23}

print("Nome: %s Idade: %d" % (nome, idade))

print("Nome: {} Idade: {}".format(nome, idade))
print("Nome: {1} Idade: {0}".format(nome, idade))
print("Nome: {1} Idade: {0} Nome: {1} {1}".format(nome, idade))

print("Nome: {nome} Idade: {idade}".format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}".format(age=idade, name=nome))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.1f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")