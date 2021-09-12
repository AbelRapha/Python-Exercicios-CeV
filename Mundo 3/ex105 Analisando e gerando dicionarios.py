def notas(*notas,sit):
    """
    -> Funcao que analisa notas e situacoes de varios alunos.
    :param n: uma ou mias notas dos alunos (aceita varias notas)
    :param: sit: valor opcional se deve ou nao adicionar a situacao
    :return: dicionario com varias informacoes sobre a situacao da turma
    """
    notasdict = {}
    notasdict["Total"] = len(notas)
    notasdict["Maior"] = max(notas)
    notasdict["Menor"] = min(notas)
    notasdict['Media'] = sum(notas)/len(notas)
    if sit == True:
        if notasdict["Media"] < 5:
            notasdict['Situacao'] = "REPROVADO"
        elif 5<notasdict["Media"]<6:
            notasdict["Situacao"] = "RECUPERACAO"
        else:
            notasdict["Situacao"] = "APROVADO"
    return notasdict
print(notas(5,9,8,10,sit=True))
help(notas)
help(min)