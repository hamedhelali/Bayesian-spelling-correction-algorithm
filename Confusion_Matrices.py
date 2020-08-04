import pandas as pd

err_freq = pd.read_csv('count_1edit.csv', delimiter=',', encoding='ISO-8859-1', header=None)
alphabet = list('abcdefghijklmnopqrstuvwxyz') + ['>']
del_conf_mat = pd.DataFrame(None, columns=alphabet, index=alphabet)
ins_conf_mat = pd.DataFrame(None, columns=alphabet, index=alphabet)
sub_conf_mat = pd.DataFrame(None, columns=alphabet, index=alphabet)
tran_conf_mat = pd.DataFrame(None, columns=alphabet, index=alphabet)

for row in alphabet:
    for col in alphabet:
        temp1 = err_freq[err_freq[0] == col + '|' + col + row]
        try:
            del_conf_mat.loc[row, col] = int(temp1[1])
        except:
            del_conf_mat.loc[row, col] = 0

        temp2 = err_freq[err_freq[0] == col + row + '|' + col]
        try:
            ins_conf_mat.loc[row, col] = int(temp2[1])
        except:
            ins_conf_mat.loc[row, col] = 0

        temp3 = err_freq[err_freq[0] == row + '|' + col]
        try:
            sub_conf_mat.loc[row, col] = int(temp3[1])
        except:
            sub_conf_mat.loc[row, col] = 0

        temp4 = err_freq[err_freq[0] == row + col + '|' + col + row]
        try:
            tran_conf_mat.loc[row, col] = int(temp4[1])
        except:
            tran_conf_mat.loc[row, col] = 0

# print(sub_conf_mat)
del_conf_mat.to_csv('del_mat.csv')
ins_conf_mat.to_csv('ins_mat.csv')
sub_conf_mat.to_csv('sub_mat.csv')
tran_conf_mat.to_csv('tran_mat.csv')
