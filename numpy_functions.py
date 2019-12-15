1.numpy.meshgrid:
link- https://www.geeksforgeeks.org/numpy-meshgrid-function/
Return coordinate matrices representing co-ordinate point of perticular dimension from 1d coordinate vectors.
ex. x = np.arange(-5, 5, 0.1)
    y = np.arange(-5, 5, 0.1)
    xx, yy = np.meshgrid(x, y, sparse=True) # sparse=true,make sparse output arrays
    xx: returns x coordinates of created grid, yy : returns y coordinates of created grid
