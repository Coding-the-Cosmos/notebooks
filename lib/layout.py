import matplotlib.pyplot as plt
from astropy.visualization import astropy_mpl_style

def set_custom_layout(figsize=(16, 8)) -> None:
    plt.style.use(astropy_mpl_style)

    # Global settings for plots

    # Set global figure size
    plt.rcParams['figure.figsize'] = figsize

    # Set the global default figure facecolor to white
    plt.rcParams['figure.facecolor'] = 'white'

    # Set the color cycle to include 10 easily distinguishable colors
    plt.style.use('tableau-colorblind10')