f = open("file.in")
w = f.readline()
nr_stari = int(f.readline())
nr_tranzitii = int(f.readline())
matrix = [] * nr_stari
for i in range(nr_stari):
    matrix.append([])
for i in range(nr_tranzitii):
    x, y, z = f.readline().split()
    x = int(x)
    y = int(y)
    matrix[x].append((y, z))
nr_stari_finale = int(f.readline())
sf = [int(i) for i in f.readline().split()]
queue = [0]
for i in range(len(w) - 1):
    char = w[i]
    aux = []
    while queue:
        for j in matrix[queue.pop(0)]:
            if j[1] == char:
                aux.append(j[0])
    queue = aux.copy()

k = 0
for i in queue:
    if i in sf:
        print("Cuvant acceptat")
        k = 1
        break
if k == 0:
    print("Cuvant neacceptat")
