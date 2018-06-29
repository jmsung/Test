# collections.Counter lets you find the most common
# elements in an iterable:

import collections
import numpy as np

data = [int(x) for x in 10*np.random.randn(1000000)]

c = collections.Counter(data)

#print('data = %r' % (data))
#print(c)
print(c.most_common(10))


