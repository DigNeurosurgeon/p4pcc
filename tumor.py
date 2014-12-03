# This little utility helps to calculate tumor volume

import math

def calculate_tumor_volume(diameter):
	'''Calculate tumor volume based on diameter'''
	return (4/3) * math.pi * (tumor_diameter / 2) ** 3

def print_tumor_stats(diameter):
	'''Print tumor parameters to the screen (based on diameter)'''
	print 'Tumor diameter: ' + str(diameter) + ' cm'
	print 'Tumor volume: %.2f cc' % calculate_tumor_volume(diameter)


tumor_diameter = float(raw_input('Enter tumor diameter in cm: '))
print_tumor_stats(tumor_diameter)