import argparse
import sys
import numpy as np
import cupy as cp

def regular_gpu_cal(xmat_cpu,yvector_cpu):

	x_mat_gpu = cp.asarray(xmat_cpu)
	yvector_gpu = cp.asarray(yvector_cpu)
	# calcualte the transpose
	xmat_transpose_gpu = cp.transpose(x_mat_gpu)
	# calcaulte the inversion
	temp1 = cp.dot(xmat_transpose_gpu, x_mat_gpu)
	inv_array_gpu = cp.linalg.inv(temp1)
	# calcaulte the result
	temp2 = cp.dot(inv_array_gpu,xmat_transpose_gpu)
	result_beta_gpu = cp.dot(temp2, yvector_gpu)
	# calcaulte the result
	result_beta = cp.asnumpy(result_beta_gpu)

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
xmat_cpu=np.loadtxt(args.xmat)
yvector_cpu=np.loadtxt(args.yvector)
# xmat.astype(np.float16)
# yvector.astype(np.float16)

result = regular_gpu_cal(xmat_cpu,yvector_cpu)

np.savetxt(args.output, result)

# for i in np.arange(len(result)):
# 	sys.stdout.write('%s\n' % result[i])

