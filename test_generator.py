import pandas as pd
from main import corrector, dic_1w

test_df = pd.read_table('spell-testset2.txt', delimiter=':', encoding='ISO-8859-1', header=None)
tests = []
for k in test_df.iterrows():
    temp = k[1][1].split()
    for i in temp:
        tests.append((k[1][0], i))

n = len(tests)
print(n)
right = 0
unknown = 0
dis = 0
for word, error in tests:
    print(word, corrector(error))
    if corrector(error) == 'ss':
        dis += 1
    if corrector(error) == word:
        right += 1
    elif word not in dic_1w[0]:
        unknown +=1

print(right / n)
print(unknown / n)