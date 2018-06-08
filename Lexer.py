def lexer(cadena):
    tokens = []
    reservadas = ["int", "float", "if", "for", "while"]
    opLog = [":=", "<", ">", ">=", "<=", "!=", "=="]
    opMat = ["+", "*", "-", "/"]
    simbolos = ["(", ")", "{", "}", ",", ";"]

<<<<<<< HEAD
    acum = ""
    for caracter in cadena:
        if caracter.isdigit():
            acum = acum + caracter
            
=======
Someday this will compile and be a working lexer... one can only dream.
>>>>>>> fa06ea89352ec09bb57b8622f3ced843ca1c97b2
