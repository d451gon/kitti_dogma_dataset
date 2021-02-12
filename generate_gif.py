import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt 

from skimage.transform import resize, rescale
from skimage.draw import line_aa

import imageio # for the gif generation

VISUALIZE = False
SAVE = True
SELECTED_GRIDS = [3, 9, 11, 25, 38, 40, 43, 64, 67, 3103]
GRIDS_FOLDER_PATH = Path('./data/')
KITTI_IMGS_PATH = Path('./kitti/training/image_2/')

if VISUALIZE:
    plt.ion()
    plt.show()

gif_imgs = []

for grid_idx in SELECTED_GRIDS:
    grid_path = GRIDS_FOLDER_PATH / '{:010d}_state_grid.npy'.format(grid_idx)
    if not grid_path.is_file():
        continue
    state_grid = np.load(grid_path)      

    # get corresponding front_image
    front_img_filename = grid_path.stem.split('_')[0][-6:] + '.png'
    print(front_img_filename)
    front_img = plt.imread(KITTI_IMGS_PATH / front_img_filename)
    width = front_img.shape[1]
    
    # for the gif we want all images with the same width
    # most front images have width = 1242 px
    if width != 1242:
        continue
    
    # reduce size of front image
    front_img = rescale(front_img, 0.8, multichannel = True,
                        anti_aliasing = True)
    front_img = np.uint8(front_img * 255)
    width = front_img.shape[1]
    
    grid_img = np.uint8(state_grid * 255)[..., [3,1,0]]
    # flip and transpose to show with matplotlib
    grid_img = np.flip(np.transpose(grid_img, (1, 0, 2)), axis = (0, 1))
    # draw approximate field of view
    rr, cc, val = line_aa(grid_img.shape[0] - 1, grid_img.shape[1] // 2,
                          grid_img.shape[0] - grid_img.shape[1] // 2, 0)
    grid_img[rr, cc, 0] = 255
    grid_img[rr, cc, 1] = 211
    grid_img[rr, cc, 2] = 67
    rr, cc, val = line_aa(grid_img.shape[0] - 1, grid_img.shape[1] // 2,
                      grid_img.shape[0] - grid_img.shape[1] // 2,
                      grid_img.shape[1] - 1)
    grid_img[rr, cc, 0] = 255
    grid_img[rr, cc, 1] = 211
    grid_img[rr, cc, 2] = 67

    # pad the grid image on the sides and above
    pad_px = (width - grid_img.shape[1]) // 2
    grid_img = np.pad(grid_img, ((10, 0), (pad_px, pad_px), (0, 0)) )
    
    # stack both grid and front images
    full_img = np.vstack((front_img, grid_img))
    
    if VISUALIZE:
        plt.clf() # otherwise images do not get garbage collected
        plt.imshow(full_img)
        plt.draw()
        plt.pause(.01)
        input("Press any key to continue.")
    
    gif_imgs.append(full_img)
    
if SAVE:
    # save the gif
    imageio.mimsave('state_grids.gif', gif_imgs, format = 'GIF', duration = 2)
