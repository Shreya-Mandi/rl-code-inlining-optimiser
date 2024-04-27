import ast


def extract_function_calls_from_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()
    return extract_function_calls(code)


def extract_function_calls(code):
    function_calls = {}

    # Parse the code into an Abstract Syntax Tree (AST)
    tree = ast.parse(code)

    # Traverse the AST
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            caller = node.name
            function_calls[caller] = set()
            # Traverse the function body to find function calls
            for sub_node in ast.walk(node):
                if isinstance(sub_node, ast.FunctionDef):
                    callee = sub_node.name
                    if caller != callee:  # Avoid self-calls
                        function_calls[caller].add(callee)

    return function_calls


def genCallGraph(filePath):
    file_path = filePath
    call_graph = extract_function_calls_from_file(file_path)
    return call_graph
