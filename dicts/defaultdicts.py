from collections import defaultdict

name = "IndianPythonista"

d = defaultdict()
for c in name:
    if c not in d:
        d[c] = 1
    else:
        d[c] += 1

print(d)

d_with_lambda = defaultdict(lambda: 0)
for c in name:
    # if c not in d:
    #     d[c] = 1
    # else:
    d_with_lambda[c] += 1

print(d_with_lambda)
print(d_with_lambda['z'])

