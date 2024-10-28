import itertools as itt
print(len(set([i[0]**i[1] for i in itt.product(range(2,101),range(2,101))])))