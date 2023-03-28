'''Complete the Exercises - Representing Abstraction Through Code 
In programming, we deal with two kinds of elements: functions and data. 

Informally, data is stuff that we want to manipulate, and functions describe the rules for manipulating the data. 

By the concept of abstraction create functions representing abstracting principles through function 

Think and design a user-defined function that should provide the result by mare passing few arguments by the calling function.
Arithmetic: Input some numbers, do some simple arithmetic, output results (Python3)
Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
Factor:  Calculate temperature that a person feels because of the wind (Python3)'''

#abstraction arthimetic
def operator(m,n):
    oper=input("enter operation: ")
    if oper=="-" :
        return print((m-n))
    elif oper=="+" :
        return print(m+n)
    elif oper=="*" :
        return print(m*n)
    elif oper=="/" :
        return print(m/n)
    elif oper=="//" :
        return print(m//n)
m=float(input("enter first number: "))
n=float(input("enter second number: "))
operator(m,n)

#Conversion
def conversion(meter):
    centimeter =meter*0.01
    kilometer =meter*1000
    milimeter =meter*0.001
    return print(centimeter,kilometer,milimeter)
meter=float(input("enter value in meter: "))
conversion(meter)

#Earthquake impact
def earthquake_impact(shear_modulus,seismic_moment,Density ):
    speed_of_seismic_waves=(((shear_modulus*seismic_moment) / Density)**(2))
    return print(speed_of_seismic_waves) 
shear_modulus=float(input("shear_modulus: "))
Density=float(input("density: "))  
seismic_moment=float(input("seismic_moment: "))
earthquake_impact(shear_modulus,seismic_moment,Density )

#Factor
def factor(temperature, wind_speed):
    wind_chill = 13.12 + 0.6215 * temperature - 11.37 * (wind_speed ** 0.16) + 0.3965 * temperature * (wind_speed ** 0.16)
    return print(wind_chill)
factor(35,45)
