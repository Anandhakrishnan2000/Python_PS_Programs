def returnscore(mat,N):
    i=0
    j=0
    score=0
    scorelst=[]
    while(i<N):
        while (j<N):
            S=score
            if i==N-1:
                j+=1
            elif j==N-1:
                i+=1
            elif mat[i+1][j] < mat[i][j+1]:
                i+=1
            else:
                j+=1
            if i<N and j<N:
                score = int((S / 2) + mat[i][j])
                scorelst.append(score)
            if j==N:
                i=N
    return scorelst[len(scorelst)-1]

N = int(input())
matrix=[]
for i in range(N):
    x=list(input().split())
    row = [int(item) for item in x]
    matrix.append(row)
returnscore(matrix,N)
