import ast
code = """
def load(path):
    try:
        return open(path).read()
    except:
        return None
"""
for node in ast.walk(ast.parse(code)):
    if isinstance(node, ast.ExceptHandler) and node.type is None:
        print("line", node.lineno, "bare except")
