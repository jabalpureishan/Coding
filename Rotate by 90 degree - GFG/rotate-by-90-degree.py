#User function Template for python3

def rotate(matrix): 
    copy = matrix[:]
    matrix.clear()
    length = len(copy)
    Index = -1
    for i in range(length-1,-1,-1):
        Index += 1
        matrix.append([])
        for j in range(length):
            matrix[Index].append(copy[j][i])
    return matrix


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		N=int(input())
		arr=[int(x) for x in input().split()]
		matrix=[]

		for i in range(0,N*N,N):
			matrix.append(arr[i:i+N])

		rotate(matrix)
		for i in range(N): 
			for j in range(N): 
				print(matrix[i][j], end =' ') 
			print() 
        

# } Driver Code Ends