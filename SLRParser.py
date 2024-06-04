# Define grammar rules
GRAMMAR = [
    ("S", ["CODE"]),
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
    0: {"vtype": "s4", "$": "r3"},
    1: {"$": "acc"},
    2: {"vtype": "s4", "$": "r3"},
    3: {"vtype": "s4", "$": "r3"},
    4: {"id": "s7"},
    5: {"$": "r1"},
    6: {"$": "r2"},
    7: {"semi": "s9", "assign": "s11", "lparen": "s10"},
    8: {"semi": "s12"},
    9: {"vtype": "r4", "id": "r4", "rbrace": "r4", "if": "r4", "while": "r4", "return": "r4", "$": "r4"},
    10: {"vtype": "s14", "rparen": "r20"},
    11: {"id": "s23", "literal": "s17", "character": "s18", "boolstr": "s19", "lparen": "s22", "num": "s24"},
    12: {"vtype": "r5", "id": "r5", "rbrace": "r5", "if": "r5", "while": "r5", "return": "r5", "$": "r5"},
    13: {"rparen": "s25"},
    14: {"id": "s26"},
    15: {"semi": "r6"},
    16: {"semi": "r7", "addsub": "s27"},
    17: {"semi": "r8"},
    18: {"semi": "r9"},
    19: {"semi": "r10"},
    20: {"semi": "r12", "addsub": "r12", "multidev": "s28", "rparen": "r12"},
    21: {"semi": "r14", "addsub": "r14", "multidev": "r14", "rparen": "r14"},
    22: {"id": "s23", "lparen": "s22", "num": "s24"},
    23: {"semi": "r16", "addsub": "r16", "multidev": "r16", "rparen": "r16"},
    24: {"semi": "r17", "addsub": "r17", "multidev": "r17", "rparen": "r17"},
    25: {"lbrace": "s30"},
    26: {"rparen": "r22", "comma": "s32"},
    27: {"id": "s23", "lparen": "s22", "num": "s24"},
    28: {"id": "s23", "lparen": "s22", "num": "s24"},
    29: {"addsub": "s27", "rparen": "s35"},
    30: {"vtype": "s42", "id": "s43", "rbrace": "r24", "if": "s40", "while": "s41", "return": "r24"},
    31: {"rparen": "r19"},
    32: {"vtype": "s44"},
    33: {"semi": "r11", "addsub": "r11", "multidev": "s28", "rparen": "r11"},
    34: {"semi": "r13", "addsub": "r13", "multidev": "r13", "rparen": "r13"},
    35: {"semi": "r15", "addsub": "r15", "multidev": "r15", "rparen": "r15"},
    36: {"return": "s46"},
    37: {"vtype": "s42", "id": "s43", "rbrace": "r24", "if": "s40", "while": "s41", "return": "r24"},
    38: {"vtype": "r25", "id": "r25", "rbrace": "r25", "if": "r25", "while": "r25", "return": "r25"},
    39: {"semi": "s48"},
    40: {"lparen": "s49"},
    41: {"lparen": "s50"},
    42: {"id": "s51"},
    43: {"assign": "s11"},
    44: {"id": "s52"},
    45: {"rbrace": "s53"},
    46: {"id": "s23", "literal": "s17", "character": "s18", "boolstr": "s19", "lparen": "s22", "num": "s24"},
    47: {"rbrace": "r23", "return": "r23"},
    48: {"vtype": "r26", "id": "r26", "rbrace": "r26", "if": "r26", "while": "r26", "return": "r26"},
    49: {"boolstr": "s56"},
    50: {"boolstr": "s56"},
    51: {"semi": "s9", "assign": "s11"},
    52: {"rparen": "r22", "comma": "s32"},
    53: {"vtype": "r18", "$": "r18"},
    54: {"semi": "s59"},
    55: {"rparen": "s60"},
    56: {"rparen": "r31", "comp": "s62"},
    57: {"rparen": "s63"},
    58: {"rparen": "r21"},
    59: {"rbrace": "r34"},
    60: {"lbrace": "s64"},
    61: {"rparen": "r29"},
    62: {"boolstr": "s56"},
    63: {"lbrace": "s66"},
    64: {"vtype": "s42", "id": "s43", "rbrace": "r24", "if": "s40", "while": "s41", "return": "r24"},
    65: {"rparen": "r30"},
    66: {"vtype": "s42", "id": "s43", "rbrace": "r24", "if": "s40", "while": "s41", "return": "r24"},
    67: {"rbrace": "s69"},
    68: {"rbrace": "s70"},
    69: {"vtype": "r33", "id": "r33", "rbrace": "r33", "if": "r33", "while": "r33", "else": "s72", "return": "r33"},
    70: {"vtype": "r28", "id": "r28", "rbrace": "r28", "if": "r28", "while": "r28", "return": "r28"},
    71: {"vtype": "r27", "id": "r27", "rbrace": "r27", "if": "r27", "while": "r27", "return": "r27"},
    72: {"lbrace": "s73"},
    73: {"vtype": "s42", "id": "s43", "rbrace": "r24", "if": "s40", "while": "s41", "return": "r24"},
    74: {"rbrace": "s75"},
    75: {"vtype": "r32", "id": "r32", "rbrace": "r32", "if": "r32", "while": "r32", "return": "r32"},
}

GOTO_TABLE = {
    0: {"CODE": 1, "VDECL": 2, "FDECL": 3, "vtype": 4},
    2: {"CODE": 5, "VDECL": 2, "FDECL": 3, "vtype": 4},
    3: {"CODE": 6, "VDECL": 2, "FDECL": 3, "vtype": 4},
    4: {"id": 7, "ASSIGN": 8},
    7: {"semi": 9, "lparen": 10, "assign": 11},
    8: {"semi": 12},
    10: {"ARG": 13, "vtype": 14},
    11: {
        "RHS": 15, 
        "EXPR": 16, 
        "literal": 17, 
        "character": 18, 
        "boolstr": 19, 
        "TERM": 20, 
        "FACTOR": 21, 
        "lparen": 22, 
        "id": 23, 
        "num": 24
    },
    13: {"rparen": 25},
    14: {"id": 26},
    16: {"addsub": 27},
    20: {"multidev": 28},
    22: {
        "EXPR": 29, 
        "TERM": 20, 
        "FACTOR": 21, 
        "lparen": 22, 
        "id": 23, 
        "num": 24
    },
    25: {"lbrace": 30},
    26: {"MOREARGS": 31, "comma": 32},
    27: {
        "TERM": 33, 
        "FACTOR": 21, 
        "lparen": 22, 
        "id": 23, 
        "num": 24
    },
    28: {"FACTOR": 34, "lparen": 22, "id": 23, "num": 24},
    29: {"rparen": 35, "addsub": 27},
    30: {"BLOCK": 36, "STMT": 37, "VDECL": 38, "ASSIGN": 39, "if": 40, "while": 41, "vtype": 42, "id": 43},
    32: {"vtype": 44},
    33: {"multidev": 28},
    36: {"RETURN": 45, "return": 46},
    37: {
        "BLOCK": 47, 
        "STMT": 37, 
        "VDECL": 38,
        "ASSIGN": 39, 
        "if": 40, 
        "while": 41, 
        "vtype": 42, 
        "id": 43
    },
    39: {"semi": 48},
    40: {"lparen": 49},
    41: {"lparen": 50},
    42: {
        "id": 51,
        "ASSIGN": 8,
        "assign": 11
    },
    44: {"id": 52},
    45: {"rbrace": 53},
    46: {
        "RHS": 54, 
        "EXPR": 16, 
        "literal": 17, 
        "character": 18, 
        "boolstr": 19, 
        "TERM": 20, 
        "FACTOR": 21, 
        "lparen": 22, 
        "id": 23, 
        "num": 24
    },
    49: {"COND": 55, "boolstr": 56},
    50: {"COND": 57, "boolstr": 56},
    51: {"semi": 9, "assign": 11},
    52: {"MOREARGS": 58, "comma": 32},
    54: {"semi": 59},
    55: {"rparen": 60},
    56: {"COND'": 61, "comp": 62},
    57: {"rparen": 63},
    60: {"lbrace": 64},
    62: {"COND": 65, "boolstr": 56},
    63: {"lbrace": 66},
    64: {
        "BLOCK": 67, 
        "STMT": 37, 
        "VDECL": 38, 
        "ASSIGN": 39, 
        "if": 40, 
        "while": 41, 
        "vtype": 42, 
        "id": 43
    },
    66: {
        "BLOCK": 68, 
        "STMT": 37, 
        "VDECL": 38, 
        "ASSIGN": 39, 
        "if": 40, 
        "while": 41, 
        "vtype": 42, 
        "id": 43
    },
    67: {"rbrace": 69},
    68: {"rbrace": 70},
    69: {"ELSE": 71, "else": 72},
    72: {"lbrace": 73},
    73: {
        "BLOCK": 74, 
        "STMT": 37, 
        "VDECL": 38, 
        "ASSIGN": 39, 
        "if": 40,
        "while": 41, 
        "vtype": 42, 
        "id": 43
    },
    74: {"rbrace": 75}
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


f = open("./input.txt", 'r')
tokens = f.readline().replace("\n", "")
#tokens = "vtype id lparen vtype id comma vtype id rparen lbrace if lparen boolstr comp boolstr rparen lbrace rbrace return boolstr semi rbrace"

parser = SLRParser(GRAMMAR, TERMINALS, NON_TERMINALS, ACTION_TABLE, GOTO_TABLE)
result = parser.parse(tokens)
print(result)