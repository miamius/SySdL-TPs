def lexer(cadena):
   
    tokens = []
    reservadas = ["int", "float", "if", "for", "while"]
    opLog = [":=", "<", ">", ">=", "<=", "!=", "=="]
    opMat = ["+", "*", "-", "/"]
    simbolos = ["(", ")", "{", "}", ",", ";"]


    
    acum = ""
    for i in range(len (cadena)):	
        print(i,cadena[i])
        #if caracter.isdigit():
       # acum = acum + caracter
            
lexer('holas');
