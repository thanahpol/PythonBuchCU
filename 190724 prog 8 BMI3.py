
w = float (input('Enter weight (kg): '))

if w <= 10:
    print ('น้ำหนักเบาไป')
    exit (1)

h = float (input('Enter height (cm): '))

if h == 0:
    print ('เป็นไปไม่ได้')
    exit (2)
 
import math

bsa1 = 3.207*(10**(-4))*(h**(0.3))*((1000*w)**(0.7285-(0.0188*(3+math.log(w,10)))))

bsa2 = 0.007184 * w**0.425 * h**0.725
# BMI = w/((h/100)**2)

print('w = ', w, 'kg')
print('h = ', h, 'cm')
print('bsa1 = ', bsa1, 'm2')
print('bsa2 = ', bsa2, 'm2')
# print('BMI = ', BMI, '-')
