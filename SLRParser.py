# Define grammar rules
GRAMMAR = [
    ("CODE", ["VDECL", "CODE"]),
    ("CODE", ["FDECL", "CODE"]),
    ("CODE", [""]),
    ("VDECL", ["vtype", "id", "semi"]),
    ("VDECL", ["vtype", "ASSIGN", "semi"]),
    ("ASSIGN", ["id", "assign", "RHS"]),
    ("RHS", ["EXPR"]),
    ("RHS", ["literal"]),
    ("RHS", ["character"]),
    ("RHS", ["boolstr"]),
    ("EXPR", ["EXPR", "addsub", "TERM"]),
    ("EXPR", ["TERM"]),
    ("TERM", ["TERM", "multidev", "FACTOR"]),
    ("TERM", ["FACTOR"]),
    ("FACTOR", ["lparen", "EXPR", "rparen"]),
    ("FACTOR", ["id"]),
    ("FACTOR", ["num"]),
    (
        "FDECL",
        [
            "vtype",
            "id",
            "lparen",
            "ARG",
            "rparen",
            "lbrace",
            "BLOCK",
            "RETURN",
            "rbrace",
        ],
    ),
    ("ARG", ["vtype", "id", "MOREARGS"]),
    ("ARG", [""]),
    ("MOREARGS", ["comma", "vtype", "id", "MOREARGS"]),
    ("MOREARGS", [""]),
    ("BLOCK", ["STMT", "BLOCK"]),
    ("BLOCK", [""]),
    ("STMT", ["VDECL"]),
    ("STMT", ["ASSIGN", "semi"]),
    ("STMT", ["if", "lparen", "COND", "rparen", "lbrace", "BLOCK", "rbrace", "ELSE"]),
    ("STMT", ["while", "lparen", "COND", "rparen", "lbrace", "BLOCK", "rbrace"]),
    ("COND", ["boolstr", "COND'"]),
    ("COND'", ["comp", "COND"]),
    ("COND'", [""]),
    ("ELSE", ["else", "lbrace", "BLOCK", "rbrace"]),
    ("ELSE", [""]),
    ("RETURN", ["return", "RHS", "semi"]),
]

TERMINALS = [
    "vtype",
    "num",
    "character",
    "boolstr",
    "literal",
    "id",
    "if",
    "else",
    "while",
    "return",
    "addsub",
    "multidev",
    "assign",
    "comp",
    "semi",
    "comma",
    "lparen",
    "rparen",
    "lbrace",
    "rbrace",
]

NON_TERMINALS = [
    "CODE",
    "VDECL",
    "ASSIGN",
    "RHS",
    "EXPR",
    "TERM",
    "FACTOR",
    "FDECL",
    "ARG",
    "MOREARGS",
    "BLOCK",
    "STMT",
    "COND",
    "COND'",
    "ELSE",
    "RETURN",
]


ACTION_TABLE = {
    0: {"vtype": "s2"},
    1: {"vtype": "s5", "$": "r2"},
    2: {"id": "s6"},
    3: {"$": "acc"},
    4: {"vtype": "s5", "$": "r2"},
    5: {"id": "s9"},
    6: {"semi": "s10", "assign": "s11"},
    7: {"semi": "s12"},
    8: {"$": "r1"},
    9: {"semi": "s10", "assign": "s11", "lparen": "s13"},
    10: {
        "vtype": "r3",
        "id": "r3",
        "rbrace": "r3",
        "if": "r3",
        "while": "r3",
        "return": "r3",
        "$": "r3",
    },
    11: {
        "id": "s22",
        "literal": "s16",
        "character": "s17",
        "boolstr": "s18",
        "lparen": "s21",
        "num": "s23",
    },
    12: {
        "vtype": "r4",
        "id": "r4",
        "rbrace": "r4",
        "if": "r4",
        "while": "r4",
        "return": "r4",
        "$": "r4",
    },
    13: {"vtype": "s25", "rparen": "r19"},
    14: {"semi": "r5"},
    15: {"semi": "r6", "addsub": "s26"},
    16: {"semi": "r7"},
    17: {"semi": "r8"},
    18: {"semi": "r9"},
    19: {"semi": "r11", "addsub": "r11", "multidev": "s27", "rparen": "r11"},
    20: {"semi": "r13", "addsub": "r13", "multidev": "r13", "rparen": "r13"},
    21: {
        "id": "s22",
        "lparen": "s21",
        "num": "s23",
    },
    22: {"semi": "r15", "addsub": "r15", "multidev": "r15", "rparen": "r15"},
    23: {"semi": "r16", "addsub": "r16", "multidev": "r16", "rparen": "r16"},
    24: {"rparen": "s29"},
    25: {"id": "s30"},
    26: {
        "id": "s22",
        "lparen": "s21",
        "num": "s23",
    },
    27: {
        "id": "s22",
        "lparen": "s21",
        "num": "s23",
    },
    28: {"addsub": "s26", "rparen": "s33"},
    29: {"lbrace": "s34"},
    30: {"rparen": "s21", "comma": "s36"},
    31: {"semi": "r10", "addsub": "r10", "multidev": "s27", "rparen": "r10"},
    32: {"semi": "r12", "addsub": "r12", "multidev": "r12", "rparen": "r12"},
    33: {"semi": "r14", "addsub": "r14", "multidev": "r14", "rparen": "r14"},
    34: {
        "vtype": "s2",
        "id": "s43",
        "rbrace": "r23",
        "if": "s41",
        "while": "s42",
        "return": "r23",
    },
    35: {"rparen": "r18"},
    36: {"vtype": "s44"},
    37: {"return": "s46"},
    38: {
        "vtype": "s2",
        "id": "s43",
        "rbrace": "r23",
        "if": "s41",
        "while": "s42",
        "return": "r23",
    },
    39: {
        "vtype": "r24",
        "id": "r24",
        "rbrace": "r24",
        "if": "r24",
        "while": "r24",
        "return": "r24",
    },
    40: {"semi": "s48"},
    41: {"lparen": "s49"},
    42: {"lparen": "s50"},
    43: {"assign": "s11"},
    44: {"id": "s51"},
    45: {"rbrace": "s52"},
    46: {
        "id": "s22",
        "literal": "s16",
        "character": "s17",
        "boolstr": "s18",
        "lparen": "s21",
        "num": "s23",
    },
    47: {"rbrace": "r22", "return": "r22"},
    48: {
        "vtype": "r25",
        "id": "r25",
        "rbrace": "r25",
        "if": "r25",
        "while": "r25",
        "return": "r25",
    },
    49: {"boolstr": "s55"},
    50: {"boolstr": "s55"},
    51: {"rparen": "r21", "comma": "s36"},
    52: {"rbrace": "r17", "$": "r17"},
    53: {"semi": "s58"},
    54: {"rparen": "s59"},
    55: {"rparen": "r30", "comp": "s61"},
    56: {"rparen": "s62"},
    57: {"rparen": "r20"},
    58: {"rbrace": "r33"},
    59: {"lbrace": "s63"},
    60: {"rparen": "r28"},
    61: {"boolstr": "s55"},
    62: {"lbrace": "s65"},
    63: {
        "vtype": "s2",
        "id": "s43",
        "rbrace": "r23",
        "if": "s41",
        "while": "s42",
        "return": "r23",
    },
    64: {"rparen": "r29"},
    65: {
        "vtype": "s2",
        "id": "s43",
        "rbrace": "r23",
        "if": "s41",
        "while": "s42",
        "return": "r23",
    },
    66: {"rbrace": "s68"},
    67: {"rbrace": "s69"},
    68: {
        "vtype": "r32",
        "id": "r32",
        "rbrace": "r32",
        "if": "r32",
        "while": "r32",
        "else": "s71",
        "return": "r32",
    },
    69: {
        "vtype": "r27",
        "id": "r27",
        "rbrace": "r27",
        "if": "r27",
        "while": "r27",
        "return": "r27",
    },
    70: {
        "vtype": "r26",
        "id": "r26",
        "rbrace": "r26",
        "if": "r26",
        "while": "r26",
        "return": "r26",
    },
    71: {"lbrace": "s72"},
    72: {
        "vtype": "s2",
        "id": "s43",
        "rbrace": "r23",
        "if": "s41",
        "while": "s42",
        "return": "r23",
    },
    73: {"rbrace": "s74"},
    74: {
        "vtype": "r31",
        "id": "r31",
        "rbrace": "r31",
        "if": "r31",
        "while": "r31",
        "return": "r31",
    },
}

GOTO_TABLE = {
    0: {"VDECL": 1, "vtype": 2},
    1: {"CODE": 3, "VDECL": 1, "FDECL": 4, "vtype": 5},
    2: {"id": 6, "ASSIGN": 7},
    4: {"CODE": 8, "VDECL": 1, "FDECL": 4, "vtype": 5},
    5: {"id": 9, "ASSIGN": 7},
    6: {"semi": 10, "assign": 11},
    9: {"semi": 10, "lparen": 13, "assign": 11},
    11: {
        "RHS": 14,
        "EXPR": 15,
        "literal": 16,
        "character": 17,
        "boolstr": 18,
        "TERM": 19,
        "FACTOR": 20,
        "lparen": 21,
        "id": 22,
        "num": 23,
    },
    13: {"ARG": 24, "vtype": 25},
    15: {"addsub": 26},
    19: {"multidev": 27},
    21: {"EXPR": 28, "TERM": 19, "FACTOR": 20, "lparen": 21, "id": 22, "num": 23},
    24: {"rparen": 29},
    25: {"id": 30},
    26: {"TERM": 31, "FACTOR": 20, "lparen": 21, "id": 22, "num": 23},
    27: {"FACTOR": 32, "lparen": 21, "id": 22, "num": 23},
    28: {"rparen": 33, "addsub": 26},
    29: {"lbrace": 34},
    30: {"MOREARGS": 35, "comma": 36},
    31: {"multidev": 27},
    34: {
        "BLOCK": 37,
        "STMT": 38,
        "VDECL": 39,
        "ASSIGN": 40,
        "if": 41,
        "while": 42,
        "vtype": 2,
        "id": 43,
    },
    36: {"vtype": 44},
    37: {"RETURN": 45, "return": 46},
    38: {
        "BLOCK": 47,
        "STMT": 38,
        "VDECL": 39,
        "ASSIGN": 40,
        "if": 41,
        "while": 42,
        "vtype": 2,
        "id": 43,
    },
    39: {"semi": 48},
    41: {"lparen": 49},
    42: {"lparen": 50},
    43: {"assign": 11},
    44: {"id": 51},
    45: {"rbrace": 52},
    46: {
        "RHS": 53,
        "EXPR": 15,
        "literal": 16,
        "character": 17,
        "boolstr": 18,
        "TERM": 19,
        "FACTOR": 20,
        "lparen": 21,
        "id": 22,
        "num": 23,
    },
    49: {"COND": 54, "boolstr": 55},
    50: {"COND": 56, "boolstr": 55},
    51: {"MOREARGS": 57, "comma": 36},
    54: {"rparen": 59},
    55: {"COND'": 60, "comp": 61},
    56: {"rparen": 62},
    59: {"lbrace": 63},
    61: {"COND": 64, "boolstr": 55},
    62: {"lbrace": 65},
    63: {
        "BLOCK": 66,
        "STMT": 38,
        "VDECL": 39,
        "ASSIGN": 40,
        "if": 41,
        "while": 42,
        "vtype": 2,
        "id": 43,
    },
    65: {
        "BLOCK": 67,
        "STMT": 38,
        "VDECL": 39,
        "ASSIGN": 40,
        "if": 41,
        "while": 42,
        "vtype": 2,
        "id": 43,
    },
    66: {"rbrace": 68},
    67: {"rbrace": 69},
    68: {"ELSE": 70, "else": 71},
    71: {"lbrace": 72},
    72: {
        "BLOCK": 73,
        "STMT": 38,
        "VDECL": 39,
        "ASSIGN": 40,
        "if": 41,
        "while": 42,
        "vtype": 2,
        "id": 43,
    },
    73: {"rbrace": 74},
}


class ParseNode:
    def __init__(self, type):
        self.type = type
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"ParseNode({self.type})"

    def print_tree(self, level=0):
        indent = "  " * level
        result = f"{indent}{self.type}\n"
        for child in self.children:
            result += child.print_tree(level + 1)
        return result


class ParseNode:
    def __init__(self, type):
        self.type = type
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"ParseNode({self.type})"

    def print_tree(self, level=0):
        indent = "  " * level
        result = f"{indent}{self.type}\n"
        for child in self.children:
            result += child.print_tree(level + 1)
        return result


class SLRParser:
    def __init__(self, grammar, terminals, non_terminals, action_table, goto_table):
        self.grammar = grammar
        self.terminals = terminals
        self.non_terminals = non_terminals
        self.action_table = action_table
        self.goto_table = goto_table
        self.stack = []

    def parse(self, tokens):
        tokens = tokens.split(" ")
        tokens += ["$"]
        self.stack = [0]
        index = 0
        root = ParseNode("CODE")

        while True:
            state = self.stack[-1]
            token = tokens[index]
            print(self.stack)

            if token not in self.action_table[state]:
                return self.error(index, tokens)

            action = self.action_table[state][token]

            if action.startswith("s"):
                new_state = int(action[1:])
                new_node = ParseNode(token)
                self.stack.append(new_state)
                index += 1
            elif action.startswith("r"):
                prod_index = int(action[1:])
                lhs, rhs = self.grammar[prod_index]

                new_node = ParseNode(lhs)
                if rhs != [""]:
                    for _ in rhs:
                        child = self.stack.pop()
                        new_node.add_child(child)
                    new_node.children.reverse()

                goto_state = self.goto_table[self.stack[-1]][lhs]
                self.stack.append(goto_state)
            elif action == "acc":
                return "Parse successful!"
            else:
                return self.error(index, tokens)

    def error(self, index, tokens):
        return f"Error at token {index}: {tokens[index]}"


tokens = "vtype id semi"

parser = SLRParser(GRAMMAR, TERMINALS, NON_TERMINALS, ACTION_TABLE, GOTO_TABLE)
result = parser.parse(tokens)
print(result)
