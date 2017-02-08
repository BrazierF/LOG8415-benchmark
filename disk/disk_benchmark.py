import os, sys, timeit
import subprocess

"""
More elegant way to run executions of shell commands 
and retrieve directly the output in a string object : 

cmd = ['sudo hdparm', '-tT']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
out, err = p.communicate('/dev/sda/')
print out
"""

def run_disk_benchmark(n_exec=4):
	for k in range(n_exec):
		os.system("sudo hdparm -t /dev/sda >> output")

	output = open('output', 'r')
	lines = output.readlines()
	av_throughput = 0.0	
	for k in range(n_exec):
		#words = lines[3*k+2].split(' ')
		#print words[12]
		av_throughput += float(lines[3*k+2].split(' ')[12])

	av_throughput /= n_exec

	os.system("rm output")

	return av_throughput

print run_disk_benchmark()


