def backspaceCompare(s, t):
        s_stack = []
        t_stack = []
        for i in range(len(s)):
            if(s[i] == '#'): 
                if(len(s_stack) > 0): 
                    s_stack.pop()
            else: s_stack.append(s[i])
        for i in range(len(t)):
            if(t[i] == '#'): 
                if(len(t_stack) > 0): 
                    t_stack.pop()
            else: t_stack.append(t[i])
        if len(s_stack) != len(t_stack): return False;
        else:
            return "".join(s_stack) == "".join(t_stack);                

print(backspaceCompare("sa#t","ss#t"))
