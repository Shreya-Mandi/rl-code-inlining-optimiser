def extract_function_calls(call_graph):
    function_calls = {}
    for node in call_graph.nodes:
        function_name = call_graph.nodes[node]['name']
        function_calls[function_name] = set()
        successors = call_graph.successors(node)
        for successor in successors:
            callee_name = call_graph.nodes[successor]['name']
            function_calls[function_name].add(callee_name)
    return function_calls