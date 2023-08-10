#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        left,prod,count = 0,1,0
        for right in range(n):
            prod *= a[right]
            while(prod>=k and left<right):
                prod  = prod//a[left]
                left += 1
            if prod<k:
                    count += right - left + 1
        return count
    
    
    
    





#{ 
 # Driver Code Starts

#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends