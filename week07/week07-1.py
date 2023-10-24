        if n<=0:                  #負數一定是錯的，0也是
            return False


        while n>1:
            if n%2 != 0:
                return False

            n = n // 2 

        return True