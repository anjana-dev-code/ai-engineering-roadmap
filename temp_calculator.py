import numpy as np 

temperatures = np.array([22,28,31,19,25,33,27])

print("Temperatures:", temperatures)
print("Mean:", temperatures.mean())
print("Max:", temperatures.max())
print("Min:", temperatures.min())
print("Std Dev:", temperatures.std())

passed = temperatures[temperatures > 27]
print("temperature > 27: ", passed)

fahrenheit = temperatures * 9/5 + 32
print("Temperature in Fahrenheit:", fahrenheit)