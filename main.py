import pandas as pd
from CandidateFinder import dic_1w, candidates
from math import log

pd.set_option('display.max_rows', None)
lamda = 1

sum_1w = dic_1w[1].sum()
ins_mat = pd.read_csv('ins_mat.csv', delimiter=',', index_col=0)
del_mat = pd.read_csv('del_mat.csv', delimiter=',', index_col=0)
sub_mat = pd.read_csv('sub_mat.csv', delimiter=',', index_col=0)
tran_mat = pd.read_csv('tran_mat.csv', delimiter=',', index_col=0)
c2 = pd.read_csv('count_2l.csv', delimiter='\t', encoding='ISO-8859-1', header=None)


def counter_2c(x):
    return int(c2[c2[0] == x][1])


def likelihood_calc(type, error, c):
    if type == 'del':
        return del_mat.loc[error, c[0]] / counter_2c(c[-2:])
    elif type == 'ins':
        # if len(c) > 2:
            return ins_mat.loc[error, c[-1]] / counter_2c(c[-2:])
        # else:
        #     return ins_mat.loc[error, c[-1]] / counter_2c(c[-2:])
    elif type == 'sub':
        if len(c) == 2 and c[0] == error:
            return sub_mat.loc[error, c[-1]] / counter_2c(c[:2])
        else:
            return sub_mat.loc[error, c[-2]] / counter_2c(c[:2])
    elif type == 'tran':
        return tran_mat.loc[error[0], c[0]] / counter_2c(c)


def prior_calc(w):
    temp = dic_1w[dic_1w[0] == w]
    try:
        prior = float(temp[1]) / sum_1w
    except:
        prior = 0
    return prior


def corrector(x):
    if len(candidates(x)) > 0:
        can_df = candidates(x)
        can_df['priors'] = can_df['candidates'].apply(prior_calc)
        print(can_df)
        can_df['likelihoods'] = can_df.apply(lambda s: likelihood_calc(s.error_type, s.error, s.c), axis=1)
        can_df.loc[can_df.candidates == x, 'likelihoods'] = 0.8
        print(can_df)
        can_df.drop(can_df[can_df.likelihoods <= 0].index, inplace=True)
        can_df['scores'] = can_df['likelihoods'].apply(log) + lamda * can_df['priors'].apply(log)
        new_df = can_df.sort_values(by='scores', ascending=False, ignore_index=True)
        print(new_df)
        if len(new_df) > 0:
            return new_df.loc[0, 'candidates']
        else:
            return 'ss'
    else:
        return 'ss'


print(corrector('luster'))
