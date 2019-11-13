#instead of literal_eval()
#from https://stackoverflow.com/questions/51711688/valueerror-malformed-node-or-string-with-ast-literal-eval-when-adding-a-keras

import ast

def eval_code(code):
    parsed = ast.parse(code, mode='eval')
    fixed = ast.fix_missing_locations(parsed)
    compiled = compile(fixed, '< class \'str\'>', 'eval')
    eval(compiled)