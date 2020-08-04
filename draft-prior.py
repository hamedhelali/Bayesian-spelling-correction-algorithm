def prior_calc(wp, w, wn):
    temp = dic_2w[dic_2w[0] == wp]
    temp = temp[temp[1] == w]
    try:
        n_p = int(temp[2])
    except:
        n_p = 0
    p_p = n_p / sum_2w
    print(n_p)
    print(p_p)
    temp2 = dic_2w[dic_2w[0] == w]
    temp2 = temp2[temp2[1] == wn]
    try:
        n_n = int(temp2[2])
    except:
        n_n = 0
    print(n_n)
    p_n = n_n / sum_2w
    print(p_n)

    prior = p_p * p_n
    return prior