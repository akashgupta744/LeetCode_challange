def numberOfBeams(bank):
        ans=0
        prev=0
        for i in bank:
            res=i.count('1')
            if res:
                ans+=prev*res
                prev=res
        return ans 
bank = ["011001","000000","010100","001000"]
print(numberOfBeams(bank))