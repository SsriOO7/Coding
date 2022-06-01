
def temp(cel):
    fore=(1.8*cel)+32
    return fore

cel=int(input("Enter temperature in celsius\t"))
c=temp(cel)
print ("Temperature in fahrenheit\t",c)

