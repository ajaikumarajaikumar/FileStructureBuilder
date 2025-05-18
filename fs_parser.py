
import os

class ParseError(Exception):
    pass

def tokenize(script):
    tokens = []
    current = ''
    i = 0
    while i < len(script):
        c = script[i]
        if c == '\\':
            if i + 1 < len(script):
                current += script[i+1]
                i += 2
                continue
            else:
                raise ParseError("Trailing backslash found.")
        elif c in '(),':
            if current.strip() != '':
                tokens.append(current.strip())
            current = ''
            tokens.append(c)
        else:
            current += c
        i += 1
    if current.strip():
        tokens.append(current.strip())
    return tokens

def parse(input_str):
    tokens = tokenize(input_str)
    if not tokens:
        raise ParseError("Empty input.")
    structure, remaining = parse_tokens(tokens)
    if remaining:
        raise ParseError("Unexpected tokens remaining after parsing.")
    return structure

def parse_tokens(tokens, depth=0):
    structure = {}
    name = None
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if token == ')':
            if depth == 0:
                raise ParseError("Unmatched closing parenthesis ')' at top level.")
            return structure, tokens[i+1:]
        elif token == '(':
            if name is None:
                raise ParseError("Unexpected '(' with no preceding name.")
            sub_structure, rest = parse_tokens(tokens[i+1:], depth + 1)
            structure[name] = sub_structure
            name = None
            return structure, rest
        elif token == ',':
            i += 1
            continue
        else:
            if '.' in token:
                if token.startswith('.'):
                    structure[f"UNNAMED{token}"] = None
                else:
                    if token in structure:
                        raise ParseError(f"Redundant file '{token}' detected.")
                    structure[token] = None
            else:
                if i + 1 < len(tokens) and tokens[i+1] == '(':
                    name = token
                else:
                    structure[token] = {}
        i += 1
    if depth > 0:
        raise ParseError("Unclosed parenthesis '(' in script.")
    return structure, []
