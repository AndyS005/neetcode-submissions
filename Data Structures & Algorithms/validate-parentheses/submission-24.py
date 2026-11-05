class Solution:
    def isValid(self, s: str) -> bool:
        valid = []
        if len(s) == 1:
            return False
        for bracket in s:
            if bracket == '(':
                valid.append(')')
            elif bracket == '{':
                valid.append('}')
            elif bracket == '[':
                valid.append(']')
            else:
                if not valid or valid.pop() != bracket:
                    return False
        
        return len(valid) == 0