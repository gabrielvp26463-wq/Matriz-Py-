import numpy as np

def criar_matriz():
    linhas = int(input("Número de linhas: "))
    colunas = int(input("Número de colunas: "))
    print("Digite os elementos da matriz linha por linha:")
    matriz = []
    for i in range(linhas):
        linha = list(map(float, input(f"Linha {i + 1}: ").split()))
        matriz.append(linha)
    return np.array(matriz)

def mostrar_menu():
    print("\nEscolha uma operação:")
    print("1. Soma de matrizes")
    print("2. Subtração de matrizes")
    print("3. Multiplicação de matrizes")
    print("4. Determinante da matriz")
    print("5. Sair")

def main():
    while True:
        mostrar_menu()
        escolha = input("Digite sua escolha: ")
        
        if escolha == "1":
            print("\nMatriz A:")
            A = criar_matriz()
            print("\nMatriz B:")
            B = criar_matriz()
            if A.shape == B.shape:
                print("\nResultado da soma:")
                print(A + B)
            else:
                print("Erro: As matrizes devem ter o mesmo tamanho!")
        
        elif escolha == "2":
            print("\nMatriz A:")
            A = criar_matriz()
            print("\nMatriz B:")
            B = criar_matriz()
            if A.shape == B.shape:
                print("\nResultado da subtração:")
                print(A - B)
            else:
                print("Erro: As matrizes devem ter o mesmo tamanho!")
        
        elif escolha == "3":
            print("\nMatriz A:")
            A = criar_matriz()
            print("\nMatriz B:")
            B = criar_matriz()
            if A.shape[1] == B.shape[0]:
                print("\nResultado da multiplicação:")
                print(np.dot(A, B))
            else:
                print("Erro: O número de colunas de A deve ser igual ao número de linhas de B!")
        
        elif escolha == "4":
            print("\nMatriz:")
            A = criar_matriz()
            if A.shape[0] == A.shape[1]:
                print("\nDeterminante da matriz:")
                print(np.linalg.det(A))
            else:
                print("Erro: A matriz deve ser quadrada!")
        
        elif escolha == "5":
            print("Saindo...")
            break
        
        else:
            print("Escolha inválida. Tente novamente.")

if __name__ == "__main__":
    main()
