A = []
for i in range(10):
  A.append(int(input("Informe o " + str(i + 1) + "º número inteiro: ")))

soma_quadrados = 0
for i in range(len(A)):
  soma_quadrados += A[i] ** 2

print("\nSoma dos quadrados dos elementos do vetor A:", soma_quadrados)
