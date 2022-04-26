import numpy as np
import time
import subprocess


range_n = np.array([20000, 50000])
range_m = np.array([500, 1000, 2000, 10000])

cpu_time = np.zeros([len(range_n), len(range_m)])
gpu_time = np.zeros([len(range_n), len(range_m)])

for i in np.arange(len(range_n)):
	for ii in np.arange(len(range_m)):
	
		n = range_n[i]
		m = range_m[ii]

		np.random.seed(0)
		xmat = np.random.rand(n,m)
		np.random.seed(1)
		beta = np.random.rand(m,1)
		yvector = np.dot(xmat, beta)

		np.savetxt('xmat.dat', xmat)
		np.savetxt('yvector.dat', yvector)
		np.savetxt('default_beta.dat', beta)

		start = time.time()
		subprocess.call(['python3','cpu.py','-x', 'xmat.dat', '-y', 'yvector.dat'])
		stop = time.time()
		cpu_time[i,ii] = stop-start
		print(cpu_time[i,ii])


		start = time.time()
		subprocess.call(['python3','gpu.py','-x', 'xmat.dat', '-y', 'yvector.dat'])
		stop = time.time()
		gpu_time[i,ii] = stop-start
		print(gpu_time[i,ii])


print(cpu_time)
print(gpu_time)