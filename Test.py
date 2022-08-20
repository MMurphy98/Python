import numpy as np
from scipy import signal


def strideConv(arr, arr2, s):
    return signal.convolve2d(arr, arr2[::-1, ::-1], mode='valid')[::s, ::s]


if __name__ == '__main__':
    k_size = 3
    im_size = 4

    kernel = np.arange(0, k_size * k_size, 1).reshape((k_size, k_size))
    act_map = np.arange(0, im_size * im_size, 1).reshape((im_size, im_size))
    conv = strideConv(act_map, kernel, 1)

    print("Kernel:")
    print(kernel)

    print("act_map:")
    print(act_map)

    print("conv:")
    print(conv)
