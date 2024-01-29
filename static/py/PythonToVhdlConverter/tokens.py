from .lexer import Token

## Logic tokens

and_tok = Token("and", "and", "logic")
not_tok = Token("not", "not", "logic")
or_tok = Token("or", "or", "logic")
xor_tok = Token("^", "xor", "logic")
nand_tok = Token("|nand|", "nand", "logic")
nor_tok = Token("|nor|", "nor", "logic")
xnor_tok = Token("|xnor|", "xnor", "logic")


## bitwise tokens

srl_tok = Token(">>", "srl", "bitwise")
sll_tok = Token("<<", "sll", "bitwise")
sra_tok = Token("|sra|", "sra", "bitwise")
sla_tok = Token("|sla|", "sla", "bitwise")

## arithmetic tokens

plus_tok = Token("+", "+", "arith")
minus_tok = Token("-", "-", "arith")
mult_tok = Token("*", "*", "arith")
div_tok = Token("/", "/", "arith")
mod_tok = Token("%", "mod", "arith")
exp_tok = Token("**", "**", "arith")

## relational operators

equalto_tok = Token("==", "=", "rel")
notequalto_tok = Token("!=", "/=", "rel")
lessthan_tok = Token("<", "<", "rel")
greaterthan_tok = Token(">", ">", "rel")
lessthanorequalto_tok = Token("<=", "<=", "rel")
greaterthanorequal_tok = Token(">=", ">=", "rel")

## assignment tok

ass_tok = Token("=", "<=", "assignment")


## additional tokens

left_square_bracket_tok = Token("[", "(")
right_square_bracket_tok = Token("]", ")")

left_parentheses_tok = Token("(", "(")
right_parentheses_tok = Token(")", ")")

single_quotation_tok = Token("'", "'")
double_quotation_tok = Token('''"''', '''"''')

coma_tok = Token(",", ",")