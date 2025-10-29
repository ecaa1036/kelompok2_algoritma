# casting @ merubah dari satu tipe ke tipe lain
#integer
data_int = 9;
print("data :", data_int, ", type :", type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int)

print("data :", data_float, ", type :", type(data_float))
print("data :", data_str, ", type :", type(data_str))
print("data :", data_bool, ", type :", type(data_bool))

# float
print("-------------------FLOAT-------------------")
data_float = 9.5;
print("data :", data_float, ", type :", type(data_float))

data_int = float(data_float) #akan dibulatkan ke bawah
data_str = str(data_float)
data_bool = bool(data_float)# akan false juka nilai intinya 0

print("data :", data_int, ", type :", type(data_int))
print("data :", data_str, ", type :", type(data_str))
print("data :", data_bool, ", type :", type(data_bool))

#BOOLEAN
print("-------------------BOOLEAN-------------------")
data_bool = True;
print("data :", data_bool, ", type :", type(data_bool))

data_int = float(data_bool) 
data_str = str(data_bool)
data_float = float(data_bool)

print("data :", data_int, ", type :", type(data_int))
print("data :", data_str, ", type :", type(data_str))
print("data :", data_float, ", type :", type(data_float))

#STRING
print("-------------------STRING-------------------")
data_str = "10";
print("data :", data_str, ", type :", type(data_str))

data_int = float(data_str) 
data_bool = str(data_str)
data_float = float(data_str)

print("data :", data_int, ", type :", type(data_int))
print("data :", data_bool, ", type :", type(data_bool))
print("data :", data_float, ", type :", type(data_float))

