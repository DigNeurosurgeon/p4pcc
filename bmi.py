# Decision making - another good way

def calculate_bmi(mass, length):
    '''Calculate Body Mass Index using body mass (kg) and body length (cm)'''
    return mass / ( (length / 100) ** 2 )

def dietary_advice(body_mass, body_length): 
    '''Give dietary advice based on Body Mass Index'''
    bmi = calculate_bmi(body_mass, body_length)

    if bmi > 30:
        return 'No more burgers for you!!'
    else:
        return 'All right, one burger will do.'

print dietary_advice(100, 180)