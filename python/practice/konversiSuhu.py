print('\nKONVERSI SUHU\n')

print('Konversi Celcius Ke Temperatur lain')

# konversi celcius ke celcius
cc = float(input('Masukkan suhu : '))
print('Suhu adalah',cc,'derajat celcius')

# konversi celcius ke rearmur
cr = (4/5) * cc
print('Suhu adalah',cr,'derajat rearmur')

# konversi celcius ke fahrenheit
cf = ((9/5) * cc) + 32
print('Suhu adalah',cf,'derajat fahrenheit')

# konversi celcius ke kelvin
ck = cc + 273
print('Suhu adalah',ck,'kelvin')

print('\nKonversi Rearmur Ke Temperatur lain\n')

# konversi rearmur ke rearmur
rr = float(input('Masukkan suhu : '))
print('Suhu adalah',rr,'derajat rearmur')

# konversi rearmur ke celcius
rc = (5/4) * rr
print('Suhu adalah',rc,'derajat celcius')

# konversi rearmur ke fahrenheit 
rf = ((9/4) * rr) + 32
print('Suhu adalah',rf,'derajat fahrenheit')

# konversi rearmur ke kelvin
rk = ((5/4) * rr) + 273
print('Suhu adalah',rk,'kelvin')

print('\nKonversi Fahrenheit Ke Temperatur lain\n')

# konversi fahrenheit ke fahrenheit
ff = float(input('Masukkan suhu : '))
print('Suhu adalah',ff,'derajar fahrenheit')

# konversi fahrenheit ke celcius
fc = 5/9 * (ff - 32)
print('Suhu adalah',fc,'derajar celcius')

# konversi fahrenheit ke rearmur
fr = 4/9 * (ff - 32)
print('Suhu adalah',fr,'derajar rearmur')

# konversi fahrenheit ke kelvin
fk = 5/9 * (ff - 32) + 273
print('Suhu adalah',fk,'kelvin')

print('\nKonversi Kelvin Ke Temperatur lain\n')

# konversi kelvin ke kelvin
kk = float(input('Masukkan suhu : '))
print('Suhu adalah',kk,'kelvin')

# konversi kelvin ke celcius
kc = kk - 273
print('Suhu adalah',kc,'derajat celcius')

# konversi kelvin ke rearmur
kr = 4/5 * (kk - 273)
print('Suhu adalah',kr,'derajat rearmur')

# konversi kelvin ke fahrenheit
kf = 9/5 * (kk - 273) + 32
print('Suhu adalah',kf,'derajat fahrenheit')



















