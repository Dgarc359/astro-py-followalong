import numpy as np
from astropy.io import fits
import matplotlib.pyplot as plt


def main():
    file = fits.open('r.fits')
    file.info()

    primary_hdu = file[0].data
    plt.imshow(primary_hdu, cmap='virids', norm='log', origin='lower')
    plt.colorbar(location='top')
    plt.show()

if __name__ == "__main__":
    main()
