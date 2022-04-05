# convert into dictionary using ast

def dict_from_ast(ast_node):
    """
    Convert an ast node into a dictionary
    """
    if isinstance(ast_node, ast.AST):
        return dict((key, dict_from_ast(value))
                    for key, value
                    in ast.iter_fields(ast_node))
    elif isinstance(ast_node, list):
        return [dict_from_ast(node) for node in ast_node]
    else:
        return ast_node