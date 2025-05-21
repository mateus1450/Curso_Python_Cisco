year = int(input("Digite um ano: "))

if year < 1582:
  print("Não dentro do período do calendário gregoriano")
  
else:
  
    if year > 1582:
        gregorian1= year % 4
        gregorian2= year % 100
        gregorian3= year % 400
      
        if gregorian1 > 0:
            print("Ano comum")
          
        elif gregorian2 > 0:
            print("Ano bissexto")
          
        elif gregorian3 > 0:
            print("Ano comum")
        
        else:
            print("Ano bissexto")
    
      
 