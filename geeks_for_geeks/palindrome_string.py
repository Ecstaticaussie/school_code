def longestPalin(S):
        if S == S[::-1]: return S
        palindromes = []
                    
        for i in range(0, len(S)):
            print(S[0:i+1])
            if S[0:i+1] == S[0:i+1:-1]: palindromes.append(S[0:i+1])

        print(list(reversed(range(0, len(S)))))
        print(list(range(0, len(S))))

        for j in reversed(range(0, len(S))):
            print(S[j:-1:])
            if S[j:-1] == S[j:-1:-1]: palindromes.append(S[j:-1])
    
        return sorted(palindromes)[0]

print(longestPalin("aaaabbaa"))