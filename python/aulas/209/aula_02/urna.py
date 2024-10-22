candidatos = {
    "A": {"votos": 0},
    "B": {"votos": 0},
    "C": {"votos": 0}
}

for candidato in candidatos:
    print(candidato)

print(candidatos)
voto = input('Digite um candidato pra votar: ')
candidatos[voto]['votos'] += 1
print(candidatos)