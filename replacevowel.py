#Para manter o loop
while True:
 #Início da requisição
 nome = input("Digite a palavra que deseja alterar")
 print(nome.replace("a" , "@").replace("e" , "&").replace("i" , "!").replace("o" , "#").replace("u" , "*"))
 #Início do código de saída
 saida = input("Digite 0 para sair do programa") 
 if saida == "0":
    break
