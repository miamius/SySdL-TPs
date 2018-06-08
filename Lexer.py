def lexer(cadena):
    tokens = []
    reservadas = ["int", "float", "if", "for", "while"]
    opLog = [":=", "<", ">", ">=", "<=", "!=", "=="]
    opMat = ["+", "*", "-", "/"]
    simbolos = ["(", ")", "{", "}", ",", ";"]

    acum = ""
    for caracter in cadena:
        if caracter.isdigit():
            acum = acum + caracter
            