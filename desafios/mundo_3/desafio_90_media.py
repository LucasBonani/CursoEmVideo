alunos = dict()
listaAprovados = list()
listaReprovados = list()
while True:
    alunos['nome'] = str(input('Digite o nome do aluno: '))
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    alunos['media'] = (nota1 + nota2) / 2
    if alunos['media'] >= 7:
        alunos['passou'] = (f'O(a) aluno(a) {alunos["nome"]} passou '
                                     f'com a média {alunos["media"]}')
        listaAprovados.append(alunos['passou'])
    elif alunos['media'] < 7:
        alunos['reprovado'] = (f'O(a) aluno(a) {alunos["nome"]} foi reprovado '
                               f'com a média {alunos["media"]}')
        listaReprovados.append(alunos['reprovado'])
    alunos.clear()
    simNao = str(input('Deseja add outro aluno? [S/N]: '))
    if simNao in 'Nn':
        break
print(f'A lista de alunos aprovados: {listaAprovados}')
print(f'A lista de alunos reprovados: {listaReprovados}')
