R = 8.3145
n = 1.0

pressure = float(input('Enter a pressure in kilopascals.  If pressure is the variable you are solving for, enter 0.'))
if pressure == 0:
            volume = float(input('Enter a volume in liters: '))
            temperature = float(input('Enter a temperature in Kelvin: '))
            pressure = (n * R * temperature)/volume
            print('Your pressure is: ', (pressure), 'kPa')
else:
            volume = float(input('If volume is the variable you are solving for, enter 0.  Otherwise, enter a value in liters to calculate temperature.'))
            if volume == 0:
                    temperature = float(input('Enter a temperature in Kelvin: '))
                    volume = (n * R * temperature)/pressure
                    print('Your volume is: ', (volume), 'L')
            else:
                    temperature = (pressure * volume)/(n * R)
                    print('Your temperature is: ', (temperature), 'Kelvin') 
                    
            

        
