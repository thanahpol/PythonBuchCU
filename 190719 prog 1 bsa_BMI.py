
w = float (input('Enter weight (kg): '))
h = float (input('Enter height (cm): '))
bsa = 0.007184 * w**0.425 * h**0.725
BMI = w/((h/100)**2)

print('w = ', w, 'kg')
print('h = ', h, 'cm')
print('bsa = ', bsa, 'm2')
print('BMI = ', BMI, '-')
