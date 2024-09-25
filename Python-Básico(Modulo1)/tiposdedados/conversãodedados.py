#Conversão de  tipos, coerção
#Type convertion, typecasting, coercion --> Mesma a coisa mas com nomeclaturas diferentes
# É o ato de converter umtipo em outro
#Tipos imutáveis e primitivos
# Str, int, float, boolean

print(1 + 1)
#print("1"+2) # Ele avisa os erros! Não pode concatenar um  string com int
print('a' + 'b') # Concatenação, juntou duas strings

# Funções de  conversão >>int("1")<<, string para números 
print("1", type("1"), int("1"), type(int("1")), sep="-")

print(int("2") +  float("2.4"))
print(bool(' '))

print(str(11) + "b")