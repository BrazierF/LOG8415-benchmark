import os, sys, timeit

def run_network_benchmark(n_exec=4):
	for k in range(n_exec):
		os.system("speedtest-cli --simple")

	output = open('output', 'r')
	lines = output.readlines()
	av_down_speed = 0.0
	av_up_speed = 0.0
	for k in range(n_exec):
		words = lines[4*k+1].split(' ')
		print words[2]
		av_down_speed += float(lines[4*k+1].split(' ')[2])
		av_up_speed += float(lines[4*k+3].split(' ')[2])
	
	av_down_speed /= n_exec
	av_up_speed /= n_exec

	os.system("rm output")

	return av_down_speed, av_up_speed

print run_network_benchmark()