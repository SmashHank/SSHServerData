import numpy as np
#import pandas as pd
import json


json.loads(open('/Users/admin/Desktop/brute_force_data.json').read().encode().decode('utf-8-sig'))

'''with open('/Users/admin/Desktop/brute_force_data.json') as f:
    data = json.load(f)'''

NewList = [1, 2, 3]

NewList = np.array(NewList)

print(NewList)

print(NewList.dtype)
