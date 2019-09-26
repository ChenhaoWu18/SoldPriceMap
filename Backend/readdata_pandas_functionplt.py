import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.colorbar as colorbar
import pandas as pd
import numpy as np

def text2plot(inFile,outFile, bounds,fsize=None):
    X = 'X' 
    Y = 'Y'
    P = 'P'
    # 1 save text to data frame and convert str to number
    df = pd.read_table(inFile, delim_whitespace=True, names=(X, Y, P),
                       dtype={X: np.int64, Y: np.float64, P: np.float64})

    # 2 change to percentage
    scaleP = df[P].max() - df[P].min()
    df[P] =df[P]*100/scaleP
    
    
    # 3 prepare for plot with figure size, color boundaries etc
    if fsize == None:
        fsize=6
    fig,ax = plt.subplots(figsize=(fsize,fsize))
    cmap = colors.ListedColormap(['yellow','pink','red', 'green', 'cyan'])
    cmap.set_over('0.10')
    cmap.set_under('0.90')
    norm3 = colors.BoundaryNorm(bounds, cmap.N)
    
    
    # 4 plot scatter with color bar
    scat = ax.scatter(df[X], df[Y],c=df[P],cmap=cmap, norm=norm3,s=3)
    plt.grid()
    ax2 = fig.add_axes([0.95, 0.1, 0.03, 0.8])
    cbar = colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm3,
        spacing='proportional', ticks=bounds, boundaries=bounds, format='%1i')
    
    ax.set_title('housing prices map')
    ax2.set_ylabel('price %')
    
    plt.savefig(outFile, bbox_inches='tight')




#-------test----------

bounds = [0, 5, 25, 75, 95,100]
text2plot('sold-price-data.txt','test.png',bounds, 5)
