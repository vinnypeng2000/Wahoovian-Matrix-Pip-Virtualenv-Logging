import numpy as np
import logging

def wahoovian(m):
    nm = np.zeros((3, 3))
    num_rows, num_cols = nm.shape
    for i in range(num_rows):
        for j in range(num_cols):
            nm[i][j] = -m[j][i]
            logging.debug("Indices: %d %d", i, j)
    print(nm)