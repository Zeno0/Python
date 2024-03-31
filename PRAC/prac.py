import itertools
import os
from subprocess import DEVNULL, run

implementations = [
                   ('ref', ['shake', 'sha2', 'haraka']),
                   ('haraka-aesni', ['haraka']),
                   ('shake-avx2', ['shake']),
                   ('sha2-avx2', ['sha2']),
                   ]

options = ["f", "s"]
sizes = [128, 192, 256]
thashes = ['robust', 'simple']

# print(itertools.product(options, sizes, thashes))
for impl, fns in implementations:
    # print(impl)
    # print(fns)
    params = os.path.join(impl, "params.h")
    print(params)
    for fn in fns:
        # print("-"*50)
        # print('inside 2nd for loop that prints functions used from provided implementations')
        # print(fn) 
        # print("-"*50)

        for opt, size, thash in itertools.product(options, sizes, thashes):
            pass
            # print(opt)
            # print(size)
            # print(thash)
        
print(os.path)