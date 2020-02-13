class Staircase_solution(object):
    def UsingBottomUp(self, n):
        """
        :type n: int
        :rtype: int
        It behaves as a Fibonaci series
        """
        if n==0:
            return 0
        elif n==1:
            return 1
        elif n==2:
            return 1
        d={0:0,1:1,2:1}
        for i in range(3,n+1):
            value=d[i-2]+d[i-1]
            d[i]=value
        return d[n]

    def fibo_staircase_memoization(self,n,memo):
        if memo[n] is not None:
            return memo[n]
        if n==1 or n==2:
            return 1
        else:
            result= self.fibo_staircase_memoization(n - 2, memo) + self.fibo_staircase_memoization(n - 1, memo)
            memo[n]=result
            return result

    def fib_memo(self,n):
        memo=[None]*(n+1)
        return self.fibo_staircase_memoization(n, memo)


sol=Staircase_solution()
print(sol.UsingBottomUp(1000))
print(sol.fib_memo(1000))