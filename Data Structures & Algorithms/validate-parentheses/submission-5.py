class Solution:
    def isValid(self, s: str) -> bool:
        valid = []
        for b in s:
            if b == "(":
                valid.append(")")
            elif b == "[":
                valid.append("]")
            elif b == "{":
                valid.append("}")
            else:
                if not valid or valid.pop() != b:
                    return False
        
        return not valid