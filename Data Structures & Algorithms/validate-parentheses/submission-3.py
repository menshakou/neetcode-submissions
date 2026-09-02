class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2:
            return False
        
        result = []

        for i in s:
            if i == '(' or i == '{' or i == '[':
                result.append(i)
            
            elif i == ')':
                if len(result) > 0 and result[-1] == '(':
                    result.pop()
                else:
                    return False
            elif i == '}':
                if len(result) > 0 and result[-1] == '{':
                    result.pop()
                else:
                    return False
            elif i == ']':
                if len(result) > 0 and result[-1] == '[':
                    result.pop()
                else:
                    return False
            
        return len(result) == 0
