# -*- coding: utf-8 -*-
"""
@author: Saumitra Kulkarni
"""

from kaprekar import kaprekar_routine
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt

# Specify the parameters
base  = 10
ndigits = 4
pad = True

# Kaprekar orbits for each of the integers, with respect to given base
# and with the above number of digits
row_list = list()

for n in range((base ** ndigits)):
    row_list.append(kaprekar_routine(n, ndigits, base, pad))
    
orbits = pd.DataFrame(row_list)

n_rowcol = math.ceil(math.sqrt(base ** ndigits))
transients = np.zeros(shape=(n_rowcol, n_rowcol))

# Compute length of initial transient for each n
for i in range(len(orbits)):
    j = (i % n_rowcol)
    k = (i // n_rowcol)
    transients[j, k] = orbits['transient_length'].loc[i]

# Plot the figure
plt.figure(figsize=(8, 8))

plt.pcolormesh(transients, cmap = 'hsv' )

# Plot cosmetics
plt.title("Kaprekar's 6174", fontsize = 17)
plt.xlabel(r'n div $\left[ \sqrt{{%d}^{%d}} \right]$' %(base, ndigits),
           fontsize = 14)
plt.ylabel(r'n mod $\left[ \sqrt{{%d}^{%d}} \right]$' %(base, ndigits), 
           fontsize = 14)
plt.xticks([0,n_rowcol])
plt.yticks([0,n_rowcol])

# Save the figure
plt.savefig('kaprekar_tapestry.png', dpi=150)
print('Visualization of Kaprekar Tapestry has been saved!'

# Show the figure
plt.show()
