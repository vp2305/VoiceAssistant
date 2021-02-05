'''
Created on 2020 M12 18

@author: vaibh
'''
import operator
def get_operator_fn(op):
    return {
        '+' : operator.add,
        '-' : operator.sub,
        '*' : operator.mul,
        '/' :operator.__truediv__,
        'mod' : operator.mod,
        }[op]

def eval_binary_expr(op1, oper, op2):
    op1,op2 = int(op1), int(op2)
    if (oper == "^"):
        return operator.pow(op1, op2)
    else:
        return get_operator_fn(oper)(op1, op2)
    
    

def mathOperations(math_command):
    """
    we get information like 3 plus 3
    """
    v = math_command.split()
    return eval_binary_expr(*(v))