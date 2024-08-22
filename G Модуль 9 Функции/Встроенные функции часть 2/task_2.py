if isinstance(txt := eval(input()), list): print(txt[-1])
elif isinstance(txt, tuple): print(txt[0])
else: print(len(txt))
