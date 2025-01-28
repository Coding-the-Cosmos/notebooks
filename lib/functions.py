import numpy as np

from .const import h, c, k

def blackbody_radiation(wavelength, temp):
    """
    Calculates the spectral radiance of a black body at a given wavelength and temperature using Planck's law.
    
    Parameters:
    - wavelength: Wavelength of the radiation (in meters).
    - temp: Temperature of the black body (in Kelvin).
    
    Returns:
    - Spectral radiance (in W/m^2/sr/m) of the black body.
    """
    exponent_factor = np.exp(h * c / (wavelength * k * temp))
    spectral_radiance = (2 * h * c**2) / (wavelength**5 * (exponent_factor - 1))
    return spectral_radiance

def peak_wavelength(temp):
    """
    Calculates the peak wavelength of black body radiation for a given temperature using Wien's Law.
    
    Parameters:
    - temp: The absolute temperature of the black body (in Kelvin).
    
    Returns:
    - The peak wavelength (in meters).
    """
    b = 2.897e-3  # Wien's displacement constant in meter-Kelvin
    lambda_max = b / temp
    return lambda_max