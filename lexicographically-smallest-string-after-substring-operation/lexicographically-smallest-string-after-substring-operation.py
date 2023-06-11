class Solution:
    def smallestString(self, s: str) -> str:
        length = len(s)
        if s=="a":
            return "z"
        if set(s)=={'a'}:
            return "a"*(length-1) + "z"
        substrings = []
        #count = 0
        s = s + "a"
        first,last = 0,0
        Max = s[:]
        for i in range(length+1):
            #print("s[i]:",s[i])
            if s[i]!="a":
                
                last += 1
                #print("last increment:",last)
            else:
                if first!=last:
                    substrings.append([first,last])
                #if((last-first)>(Max[1]-Max[0])):
                    #Max = [first,last]
                    #print("max updated",Max)
                first,last = i+1,i+1
                #print("reset:",first,last)
        for i in substrings:
            current = ""
            for j in range(i[0],i[1]):
                current += chr(ord(s[j])-1)
            current = s[:i[0]] + current + s[i[1]:length]
            #print("current",current)
            Max = min(Max,current)
        return Max

                
        