'''Problem -II
Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

Radio Waves Less than 3 × 10^9
Microwaves 3 × 10^9 to less than 3 × 10^12
Infrared Light 3 × 10^12 to less than 4.3 × 10^14
Visible Light 4.3 × 10^14 to less than 7.5 × 10^14
Ultraviolet Light 7.5 × 10^14 to less than 3 × 10^17
X-Rays 3 × 10^17 to less than 3 × 10^19
Gamma Rays 3 × 10^19 or more

Write a program that reads the frequency of some radiation from the user and
displays name of the radiation as part of an appropriate message.'''

radiation_range=float(input("Enter the radiation between 3e9 to 3e19(3*10*9 to 3*10*19): "))
if radiation_range<3e9:
    print("TypeError:Enter radiation in given limit")
if 3e9<=radiation_range<3e12:
    print("it is microwave range ")
if 3e12<=radiation_range<4.3e14:
    print("it is infrared range ")
if 4.3e14<=radiation_range<7.5e14:
    print("it is visible light range ")
if 7.5e14<=radiation_range<3e17:
    print("it is ultraviolet range ") 
if 3e17<=radiation_range<3e19:
    print("it is X rays range ")
if radiation_range>=3e19:
    print("it is gamma rays range")