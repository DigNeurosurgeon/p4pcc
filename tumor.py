# This now is a module that helps for tumor volumetry

import math

def calculate_tumor_volume(diameter):
	'''Calculate tumor volume based on diameter'''
	return (4/3) * math.pi * (diameter / 2) ** 3

def print_tumor_stats(diameter):
	'''Print tumor parameters to the screen (based on diameter)'''
	print 'Tumor diameter: ' + str(diameter) + ' cm'
	print 'Tumor volume: %.2f cc' % calculate_tumor_volume(diameter)
