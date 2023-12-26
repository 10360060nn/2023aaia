 n=len(s)
        ans=0
        for left in range(n-1):
            now=0
            for i in range(n):
                if i<=left and s[i]=='0': now += 1
                if i>left and s[i]=='1': now += 1
            if now>ans: ans=now
        return ans