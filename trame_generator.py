#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LEnsE projects / Institut d'Optique

FFT on images / Sine Trame Generator

Created on 25/Sep/2024

@author: LEnsE / IOGS / Palaiseau
@author: Julien Villemejane
"""

import numpy as np
import cv2
import matplotlib.pyplot as plt

def sine_trame(height, width, step, angle):
    x = np.arange(0,height)
    y = np.arange(0,width)
    XX, YY = np.meshgrid(x, y)
    alpha_rad = np.radians(angle)
    return 0.5*(1 + np.cos(2*np.pi*XX/step*np.cos(alpha_rad) + 2*np.pi*YY/step*np.sin(alpha_rad) )) 


image = sine_trame(400, 300, 30, 63)

fft_image = np.fft.fft2(image)
fft_shifted = np.fft.fftshift(fft_image)

# Display images
plt.figure(1,figsize=(10, 5))
plt.imshow(image, cmap='gray')
plt.title('Image in Gray')
plt.figure(2,figsize=(10, 5))
plt.imshow(np.abs(fft_shifted), cmap='gray')
plt.title('FFT Image in Gray')
plt.show()