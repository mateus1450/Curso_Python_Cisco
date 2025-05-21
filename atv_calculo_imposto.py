income = float(input("Entre com os rendimentos anuais "))
# Atividade calculo de imposto
# se a renda do cidadão não era superior a 85.528 talões, o imposto era igual a 18% da renda, menos 556 taller e 2 centavos (isso era o que eles chamavam de isenção de imposto)
# se a receita fosse superior a esse valor, o imposto seria igual a 14.839 talões e 2 centavos, mais 32% do excedente em mais de 85.528 taller.


if income < 85528:
    tax = income * 0.18 - 556.02

if income > 85528:
    tax = (income - 85528) * 0.32 + 14839.2
    
else:

    if tax < 1:
        print("The tax is:", 0.0, "thalers")
        exit()
    

tax = round(tax, 0)
print("A taxa é:", tax, "thalers") 
 