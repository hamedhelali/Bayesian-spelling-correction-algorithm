import pandas as pd

dic_1w = pd.read_csv('dic_1w.csv', delimiter=',', encoding='ISO-8859-1', header=None, na_filter=False, nrows=50000)
dic_1w.drop(dic_1w[dic_1w[0].str.len() < 2].index, inplace=True)


def Is_in_dic(word):
    if len(dic_1w[dic_1w[0] == word]) > 0:
        return True
    else:
        return False


def candidates(x):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    edits = pd.DataFrame(None, columns=['candidates', 'error_type', 'error', 'c'])
    splits = [(x[:i], x[i:]) for i in range(len(x) + 1)]

    dels = []
    inss = []

    trans = [[L + R[1] + R[0] + R[2:], 'tran',  R[0] + R[1], R[1] + R[0]] for L, R in splits if len(R) > 1]
    subs = [[L + c + R[1:], 'sub', R[0], L[-1:] + c + R[1:2]] for L, R in splits if R for c in alphabet]

    for L, R in splits:
        if R:
            if L:
                inss.append([L + R[1:], 'ins', R[0], L[-2:] + R[1:2]])
            else:
                inss.append([L + R[1:], 'ins', R[0], '>' + R[1:3]])
        for c in alphabet:
            try:
                dels.append([L + c + R, 'del', c, L[-1]+c])
            except:
                dels.append([L + c + R, 'del', c, '>' + c + R[0:1]])

    for item in dels:
        if Is_in_dic(item[0]):
            edits.loc[len(edits)] = item

    for item in inss:
        if Is_in_dic(item[0]):
            edits.loc[len(edits)] = item

    for item in trans:
        if Is_in_dic(item[0]):
            edits.loc[len(edits)] = item

    for item in subs:
        if Is_in_dic(item[0]):
            edits.loc[len(edits)] = item

    return edits.drop_duplicates(subset='candidates')

