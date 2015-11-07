"""
Parsing basic arithmetic strings

operators:
["+", "-", "*", "/"]

digit:
[0,1,2,3,4,5,6,7,8,9]

number:
digit {digit}

term:
<term> <operator> <term>
"""

from enum import Enum


"""
Enum class for arithmetic operation
"""

Operator_Priority = {
    "+": 10,
    "-": 20,
    "*": 40,
    "/": 30
}

class Identifier(Enum):
    int = "int"
    float = "float"


class Basic_Operator(Enum):
    operator = "operator"
    add = "+"
    minus = "-"
    multiply = "*"
    divide = "/"

class Eval_Operator(object):
    def __init__(self, left_part, right_part):
        self.left_part = left_part
        self.right_part = right_part


class Add_Operator(Eval_Operator):
    def __init__(self, left_part, right_part):
        self.left_part = left_part
        self.right_part = right_part
        self.priority = 10

    def evaluate(self):
        return self.left_part.evaluate() + self.right_part.evaluate()


class Minus_Operator(Eval_Operator):
    def __init__(self, left_part, right_part):
        self.left_part = left_part
        self.right_part = right_part
        self.priority = 20

    def evaluate(self):
        return self.left_part.evaluate() - self.right_part.evaluate()


class Multiply_Operator(Eval_Operator):
    def __init__(self, left_part, right_part):
        self.left_part = left_part
        self.right_part = right_part
        self.priority = 40

    def evaluate(self):
        return self.left_part.evaluate() * self.right_part.evaluate()


class Divide_Operator(Eval_Operator):
    def __init__(self, left_part, right_part):
        self.left_part = left_part
        self.right_part = right_part
        self.priority = 30

    def evaluate(self):
        return self.left_part.evaluate() / self.right_part.evaluate()


class P_Integer(object):
    def __init__(self, item):
        self.value = item

    def evaluate(self):
        return int(self.value)

"""
Token helper function
"""
# Return number pair
def num_tk(item):
    if is_int(item):
        return (Identifier.int, int(item))
    elif is_float(item):
        return (Identifier.float, float(item))


# Return operator pair
def operator_tk(item):
    if item == Basic_Operator.add.value:
        return (Basic_Operator.operator, Basic_Operator.add)

    elif item == Basic_Operator.minus.value:
        return (Basic_Operator.operator, Basic_Operator.minus)

    elif item == Basic_Operator.multiply.value:
        return (Basic_Operator.operator, Basic_Operator.multiply)

    elif item == Basic_Operator.divide.value:
        return (Basic_Operator.operator, Basic_Operator.divide)


def is_number(item):
    if is_int(item):
        return True
    elif is_float(item):
        return True
    else:
        return False


def is_int(item):
    try:
        int(item)
        return True
    except ValueError:
        return False


def is_float(item):
    try:
        float(item)
        return True
    except ValueError:
        return False


def is_operator(item):
    if item == Basic_Operator.add.value:
        return True
    elif item == Basic_Operator.minus.value:
        return True
    elif item == Basic_Operator.multiply.value:
        return True
    elif item == Basic_Operator.divide.value:
        return True
    else:
        print("No operator match")
        return False

def is_operator_tk(token):
    return token[0] == Basic_Operator.operator


def is_add_tk(token):
    return token[1] == Basic_Operator.add


def is_minus_tk(token):
    return token[1] == Basic_Operator.minus


def is_multiply_tk(token):
    return token[1] == Basic_Operator.multiply


def is_divide_tk(token):
    return token[1] == Basic_Operator.divide


"""
Parser Modules
"""
# Split input string into word list
def word_splitter(input_string):
    return input_string.split()


# Tokenizing each word into identifiable tokens
def tokenizer(input_list):
    token_list = []
    for item in input_list:
        if is_number(item):
            token_list.append(num_tk(item))
        elif is_operator(item):
            token_list.append(operator_tk(item))
    return token_list


# Evaluating token list
def build_AST(token_list):
    return recur_build_ast(token_list[::-1])


def recur_build_ast(token_list):
    if len(token_list) == 1 and (token_list[0][0] == Identifier.int or token_list[0][0] == Identifier.float):
        return P_Integer(token_list[0][1])

    for item in token_list:
        lowest_priority = get_lowest_priority(token_list)
        if is_add_tk(token_list[lowest_priority]):
            return Add_Operator(recur_build_ast(token_list[lowest_priority + 1:]),
                                recur_build_ast(token_list[:lowest_priority]))
        elif is_minus_tk(token_list[lowest_priority]):
            return Minus_Operator(recur_build_ast(token_list[lowest_priority + 1:]),
                                  recur_build_ast(token_list[:lowest_priority]))
        elif is_multiply_tk(token_list[lowest_priority]):
            return Multiply_Operator(recur_build_ast(token_list[lowest_priority + 1:]),
                                     recur_build_ast(token_list[:lowest_priority]))
        elif is_divide_tk(token_list[lowest_priority]):
            return Divide_Operator(recur_build_ast(token_list[lowest_priority + 1:]),
                                   recur_build_ast(token_list[:lowest_priority]))
        else:
            raise Exception("Error, No operator match")


def get_lowest_priority(token_list):
    cur_max = 100
    max_index = -1
    for index in range(len(token_list)):
        if is_operator_tk(token_list[index]):
            cur_priority = Operator_Priority[token_list[index][1].value]
            if cur_priority < cur_max:
                cur_max = cur_priority
                max_index = index
    return max_index

def main(input):
    word_list = word_splitter(input)
    token_list = tokenizer(word_list)
    ast = build_AST(token_list)
    value = ast.evaluate()

    return value