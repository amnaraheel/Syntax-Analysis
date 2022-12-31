import ast

def syntax_tree(expression):
    syntax_tree = ast.parse(expression)
    return ast.dump(syntax_tree)
    
if __name__=="__main__":
    expression=input("Enter a regular Expression (e.g. (3 + 4) * 10): \n")
    print(syntax_tree(expression))
