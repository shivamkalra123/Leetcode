class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators=["+","*","/","-"]
        
        def operate(a,b,op):
            print(f"Operating: {b} {op} {a}")
            if op=="+":
                return b+a
            if op=="-":
                return b-a
            if op=="*":
                return b*a
            if op=="/":
                return int(b/a)   # truncate toward zero
        
        for s in tokens:
            
            
            if s in operators:
                a=stack.pop()
                b=stack.pop()
                
                
                v=operate(a,b,s)
                
                
                stack.append(v)
                
            else:
                stack.append(int(s))   # push int directly
                
                
  
        return stack[-1]