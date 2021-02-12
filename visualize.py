import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt 

plt.ion()
plt.show()

GRIDS_FOLDER_PATH = Path('./data/')
grid_paths = sorted(GRIDS_FOLDER_PATH.glob('*state_grid.npy'))

for state_grid_path in grid_paths:
    state_grid = np.load(state_grid_path)
    
    # remove potential nans or large values
    # state_grid[np.where(np.isnan(state_grid))] = 0.0
    # state_grid[np.where(state_grid>1000.0)] = 0.0
    # state_grid[np.where(state_grid<-1000.0)] = 0.0
    
    grid_img = np.uint8(state_grid * 255)[..., [3,1,0]]
    # flip and transpose to show with matplotlib
    grid_img = np.flip(np.transpose(grid_img, (1, 0, 2)), axis = (0, 1))

    plt.clf() # otherwise images do not get garbage collected
    plt.imshow(grid_img)
    plt.draw()
    plt.pause(.01)
    input("Press any key to continue.")