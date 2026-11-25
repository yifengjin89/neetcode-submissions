class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        temp = []
        
        for token in tokens:
            if token in ["*", "/", "+", "-"]:
                # pop stack
                # only pop two number
                for _ in range(2):
                    temp.append(stack.pop())
                
                curr = self.operator(temp[0], temp[1], token)
                stack.append(curr)
                temp = []
            else:
                stack.append(int(token))
            
        
        return int(stack[-1])
        

    def operator(self, a, b, oper):
        if oper == "+":
            return b + a
        elif oper == "-":
            return b - a
        elif oper == "*":
            return b * a
        else:
            return int(b / a)