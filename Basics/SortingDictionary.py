d = {'Ayush': 42, 'Ankit': 2, 'Aakash': 3, 'Devesh': 49, 'Devansh': 58}

dkeys = list(d.keys())
dkeys.sort()

sd = {i: d[i] for i in dkeys}

print(sd)
