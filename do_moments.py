from scipy.ndimage.filters import gaussian_filter
import numpy as np
from astropy.io import fits
import matplotlib as mpl
mpl.use('Agg')
import argparse
import matplotlib.pyplot as plt


def load_fits(filename):
        return fits.open(filename)[0].data


def dist(x1, y1, x2, y2):
        return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)


def set_zeros(x1, y1, x2, y2, radius):
        if dist(x1, y1, x2, y2) <= radius:
                return 0


def remove_centre_image(image, radius):
        x_cen, y_cen = np.ceil(image.shape[0]/2), np.ceil(image.shape[1]/2)
        print(image.shape)
        print(x_cen, y_cen)
        for x in range(int(x_cen - radius), int(x_cen + radius)):
                for y in range(int(y_cen - radius), int(y_cen + radius)):
                        if dist(x_cen, y_cen, x, y) <= radius:
                                image[x][y] = 0.


def convolve_image(image, beam_width):
    return gaussian_filter(image, sigma=beam_width)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Import FITS files for convolution.')
    parser.add_argument('--filename', '-f', default='')
    parser.add_argument('--distance', '-d', default=140, type=float)
    parser.add_argument('--seeing', '-s', default=0.04, type=float)
    parser.add_argument('--save', '-z', type=str)
    args = parser.parse_args()

    image = load_fits(args.filename)
    print(type(image))
    print(image.shape)
    image = image[0, 0, 0, :, :, :]
    print(image[0, :, :].shape)
    moment_1 = np.zeros(image[0, :, :].shape)
    v_max = 8.
    vs = np.linspace(-v_max, v_max, image.shape[0])

    for i in range(0, image.shape[0]):
        moment_1 += image[i, :, :]*vs[i]
        print(vs[i])
    image = moment_1
    remove_centre_image(image, 1)
    # image = np.ndarray.flatten(image)
    print(image.shape)
    # Block out central pixel..
    conv_image = convolve_image(image, 2.)
    print(type(conv_image))
    print(conv_image.shape)
    plt.imshow(conv_image, cmap='gist_ncar')
    plt.tight_layout()
    plt.savefig(args.save)
    # print(image.info())