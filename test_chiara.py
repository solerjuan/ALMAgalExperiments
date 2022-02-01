########################
# Created by Chiara
# 31 January 2022
#######################
import numpy
from astropy.stats import sigma_clipped_stats


def  chiara_test(n):
	if n==0:
		print('######### n = 0 - no calculation performed')
	if n!=0:
		somma_1_n = n*(n+1)/2
		quadrato = n**2
		cubo = n***3

		print('\n ### n : ', n, '\n')
		print('\n ### somma da 1 a n : ', somma_1_n, '\n')
		print('\n ### quadrato di n : ', quadrato, '\n')
		print('\n ### cubo di n : ',cubo, '\n')

		#gaussian distribution mean n**2 and std n
		data = np.random.normal(quadrato, n, 1000)
		mean , median, std = sigma_clipped_stats(data, sigma=3.0, maxiters = 5)

		print('\n mean value of the gaussian distribution : ', mean, '\n')
		print('\n std of the gaussian distribution : ', std, '\n')

	return None