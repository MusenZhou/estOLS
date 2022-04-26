# estOLS
This repository archives the source code to calculate the least squares estimate from matrix vector operations.<br>
More specifically, assume xβ=y, this code calculated β via the following mathematical operation: β=(x<sup>T</sup>x)<sup>-1</sup>x<sup>T</sup>y


# Prerequisite
Two versions of implementation are offered and different prerequisites need to be installed based on the need. For GPU implementation, Nvidia GPU and CUDA library would be needed.
### CPU version
Run the following script in the command line<br>
conda install --yes --file cpu_requirements.txt
### GPU version
Run the following script in the command line<br>
conda install --yes --file gpu_requirements.txt

# Excutation
To run the script and obtain the beta, copy the corresponding .py file (e.g., cpu.py for cpu version) in the source code folder to the folder where you have your matrix file (e.g., xmat.dat) and y vector file (e.g., yvector.dat).<br>
Then run the following command in the command line:<br>
python3 cpu.py -x xmat.dat -y yvector.dat -o beta_result.dat<br>
or<br>
python3 cpu.py -x xmat.dat -y yvector.dat -o beta_result.dat<br>
The filename after '-o' can be renamed as user wish. If the option '-o' is not specified, the default file to store the result of beta would be 'beta.dat'.

# Example
Example files of x matrix and y vector are also offered in the example folder. To run it, simple put the following line<br>
python3 cpu.py -x xmat.dat -y yvector.dat -o beta_result.dat<br>
in the command line. One can compare the output file 'beta_result.dat' with the ground true result file 'correct_bta.dat' to see the numerical accuracy of this implementation.