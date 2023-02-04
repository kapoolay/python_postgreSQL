class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{" }

        for p in s:
            if p in closeToOpen:
                #make sure stack is empty AND check if parantheses match with last item in stack
                if stack and stack[-1] == closeToOpen[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        # return true if stack is empty, else return false
        return True if not stack else False

s = ('(', ')', '{', '}', '[', ']')

print(Solution())