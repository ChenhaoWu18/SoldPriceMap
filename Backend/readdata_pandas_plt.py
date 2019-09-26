info_doc = '''
* Inputs:
    arg1 -  input-text-data-file-name.txt
    arg2 -  output-graph-file-name.pny
    arg3 -  the size of the output graph,
            suggest choose a number between 5-30.
           
    arg4 -  the size of each scatter points in the graph,
            suggest choose a number similar with graph size,
            so the larger of the graph the bigger the dots.
            
* For example, copy the command to terminal: 
    python readdata_pandas_plt.py sold-price-data.txt priceMap.png 6 8
    
    Hint enter to run the code, you can then find a file called priceMap.png
    which contain the graph the program just ploted. 

* What this file do?
    1. read text file to dataframe (X, Y, P)
    2. plot each point on a grid. 
        The points filled with a colour to representing how expensive 
        a house was in relation to other houses. 
    3. boundries of the color range are: 
        0% - 5%     yellow
        5% - 25%    pink
        25% - 75%   red
        75% - 95%   green
        95% - 100%  cyan
'''
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.colorbar as colorbar
import pandas as pd
import numpy as np
import sys

def file2Dataframe(inFile):
    X = 'X' 
    Y = 'Y'
    P = 'P'
    df = pd.read_csv(inFile, delim_whitespace=True, names=(X, Y, P),
                       dtype={X: np.float64, Y: np.float64, P: np.float64})
    scaleP = df[P].max() - df[P].min()
    df[P] =df[P]*100/scaleP
    return df[X], df[Y], df[P]

def data2plot(inFile,outFile,fsize=None, dotsize=None):
    
    #1. save X, Y, P values to a dataframe 
    dX, dY, dP = file2Dataframe(inFile)
    
    
    # 2 prepare for plot with figure size, color boundaries etc
    if fsize == None:
        fsize=6
    fsize = int(fsize)
    fig,ax = plt.subplots(figsize=(fsize,fsize))
    cmap = colors.ListedColormap(['yellow','pink','red', 'green', 'cyan'])
    bounds = [0, 5, 25, 75, 95,100]
    norm3 = colors.BoundaryNorm(bounds, cmap.N)
    
    
    # 3 plot scatter with color bar
    if dotsize == None:
        dotsize=5
    dotsize = int(dotsize)
    ax.scatter(dX, dY,c=dP,cmap=cmap, norm=norm3,s=dotsize)
    plt.grid()
    ax2 = fig.add_axes([0.95, 0.1, 0.03, 0.8])
    colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm3,
        spacing='proportional', ticks=bounds, boundaries=bounds, format='%1i')
    
    ax.set_title('housing prices map')
    ax2.set_ylabel('price %')
    
    plt.savefig(outFile, bbox_inches='tight')
    

def main():
    # 1 sys input check 
    if (len(sys.argv)) != 5:
        print (info_doc)
        sys.exit(1)
        
    # 2 link sys input to function inputs
    inFile = sys.argv[1]
    outFile = sys.argv[2]
    fsize = sys.argv[3]
    dotsize = sys.argv[4]
    
    data2plot(inFile,outFile,fsize, dotsize)


if __name__ == '__main__':
    main()
    





