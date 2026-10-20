class Solution:
    def isValid(self, s: str) -> bool:
        valid = []
        if len(s) == 1:
            return False
        for b in s:
            if b == "(":
                valid.append(")")
            elif b == "{":
                valid.append("}")
            elif b == "[":
                valid.append("]")
            else:
                if not valid:
                    return False
                elif b != valid.pop():
                    return False 
        return not valid