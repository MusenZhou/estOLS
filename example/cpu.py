import argparse
import sys
import numpy as np


def regular_cpu_cal(xmat,yvector):
	# calcualte the transpose
	xmat_transpose = np.transpose(xmat)
	# calcaulte the inversion
	inv_array = np.linalg.inv(np.dot(xmat_transpose, xmat))
	# calcaulte the result
	result_beta = np.dot(np.dot(inv_array,xmat_transpose), yvector)
	return result_beta


# initialize parse
parser = argparse.ArgumentParser()

parser.add_argument('-x', '--xmat', help='x matrix')
parser.add_argument('-y', '--yvector', help='y vector')
parser.add_argument('-o', '--output', help='output')

args = parser.parse_args()

if not args.output:
	args.output = 'beta.dat'



# main script
xmat=np.loadtxt(args.xmat)
yvector=np.loadtxt(args.yvector)

result = regular_cpu_cal(xmat,yvector)

np.savetxt(args.output, result)

# for i in np.arange(len(result)):
# 	sys.stdout.write('%s\n' % result[i])

