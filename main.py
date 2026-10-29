# notas = [100, 89, 90, 35, 67, 75]

# media = sum(notas) / len(notas) 

# print(media)

# if media >= 60:
#     print("aprovado")
# else:
#     print("reprovado")

alunos = [
    {'nome' : 'yasmin', 'notas': [3, 7] , 'idade': 16, 'frequencia' : 150},
    {'nome' : 'Bruno', 'notas': [8, 7] , 'idade': 16, 'frequencia' : 300},
    {'nome' : 'geira', 'notas': [6, 7] , 'idade': 18, 'frequencia' : 240},
    {'nome' : 'anarquias', 'notas': [3, 8] , 'idade': 14, 'frequencia' : 780},
]

def presenca(frequencia):
     if frequencia >= 225:
          return 'presença ok'
     return 'reprovado por falta'

def calcular_media(soma, qtde):
    return soma / qtde


def status_aprovação(nota):
     if nota >= 6:
            return 'Aprovado'
     return 'reprovado'
for aluno in alunos:
    qtde_notas = len(aluno['notas'])
    soma = sum(aluno['notas'])
    nota = calcular_media(soma, qtde_notas)

status_nota = status_aprovação(nota)
status_falta = presenca(aluno['frequencia'])

print(f"aluno: {aluno['nome']}, nota: {nota}, Status: {status_nota}, frequencia: {status_falta}")

if status_nota == 'Aprovado' and status_falta == 'presença ok':
        'aprovado'.append(aluno['nome'])
else:
       'reprovado'.append(aluno['nome'])

print(f"\nLista de Aprovados: {'aprovado'}")
print(f"Lista de Reprovados: {'reprovado'}")
