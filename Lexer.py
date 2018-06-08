def lexer(cadena):
    tokens = []
    reservadas = ["int", "float", "if", "for", "while"]
    opLog = [":=", "<", ">", ">=", "<=", "!=", "=="]
    opMat = ["+", "*", "-", "/"]
    simbolos = ["(", ")", "{", "}", ",", ";"]