"""
USE: python <PROGNAME> (options)

OPTIONS:
    -h : Print this help message and exit.
    -i FILE : input-text-data-file-name.txt, process text from input file FILE.
    -o FILE : output-graph-file-name.png, write results to output file FILE.
    -g PARAMETER: The size of the output graph, 
                    I suggest choosing a number between 5 and 30.
    -d PARAMETER: The size of each scatter point in the graph, 
                    I suggest choosing a number similar to the graph size,
                    so that a larger graph has bigger dots.
                    
                    
    For example, copy this command to the terminal: 
        1. Using the default graph size and dot size:
            python plotSoldPriceMap_v2.py -i sold-price-data.txt -o priceMap.png 
       
        2. Using a customesed graph size and dot size:
            python plotSoldPriceMap_v2.py -i sold-price-data.txt -o priceMap.png -g 6 -d 8
        
        3. Hint: enter to run the code, you can then find a file called priceMap.png
            which contains the graph that the program just ploted. 
"""
"""
**************************** Code explaination - move to README *****************************************
* What does this file do?
    1. Reads the text file to the dataframe (X, Y, P).
    2. Plots each point onto a grid. 
        The points given colours representing how expensive 
        a house was in relation to other houses. 
    3. The boundries of the color range are: 
        0% - 5%     yellow
        5% - 25%    pink
        25% - 75%   red
        75% - 95%   green
        95% - 100%  cyan
    
* Code structure for main functionalities:
    1. main function 
        I/O: Inputs: From the command line with flag -i -o -g -d (link to dataFrame_2_plot function inputs);
             Output: A .png file as the sold price map (link from dataFrame_2_plot function output)
        Steps:
        (1) Setup help and simple validations for command line flag inputs.
        (2) Link the sys input to function's input.
        (3) Run the dataFrame_2_plot function to generate the sold price map graph.
        
    2. dataFrame_2_plot function
        I/O: Inputs: inFile: Name of the input .txt file (linked from the command line).
                     outFile: Name of the output .png graph (linked from the command line).                       
                     graphSize: A str data type integer for customised graph size (optional input linked from the command line or the commandLine_flagOptions function).  
                     dotSize: A str data type integer for customised dot size (optional input linked from the command line or the commandLine_flagOptions function).
             Output: A .png file as the sold price map.
        Steps:
            (1) Saves X, Y & P values from .txt file to a dataframe (using inFile_2_dataFrame function).
            (2) Plots the sold price map graph with a colour bar (see more details within the function).
            (3) Save the plot to a .png file.
            

* Updates 08/10/19:
    1. Updated the file name to plotSoldPriceMap_v2.py
    2. Using getopt command line flag I/O rather than args.
        Reason: more informative, graph size and dot size become optional inputs. 
    3. Updated varible/function names (I really appreciate for the feedback!)
        -- Updated variable names to readable camel style. 
        -- Updated function names to readable snake style (sometimes combined with camel style within the name).   
        -- Some unchanged names based on conventions, I will adapt to the company tech team style when I can read scripts from you. :)
    4. Added code structure for main functionalities explaination.

* Futher improvements:
    a. Unit tests - coming later.
    b. System tests - coming later.
    c. Using both short and long input options e.g. 'h:i:o:g:d:',
        ['help','inFile','outFile','graphSize','dotSize'].
    d. I can add code structure for the command line flag settings if required.

* The libraries used are: matplotlib, pandas, numpy, sys & getopt.
********************************************************************************
"""

import matplotlib.pyplot as plt
import matplotlib.colors as colors
import matplotlib.colorbar as colorbar
import pandas as pd
import numpy as np
import sys, getopt

#######
# SECTION FOR COVERT DATA TO GRAPH
#######


def inFile_2_dataFrame(inFile):
    X = 'X' 
    Y = 'Y'
    P = 'P'
    df = pd.read_csv(inFile, delim_whitespace=True, names=(X, Y, P),
                       dtype={X: np.float64, Y: np.float64, P: np.float64})
    priceScale = df[P].max() - df[P].min()
    df[P] =df[P]*100/priceScale
    return df[X], df[Y], df[P]

def dataFrame_2_plot(inFile,outFile,graphSize, dotSize):
    
    # 1 Saves X, Y & P values to a dataframe. 
    dX, dY, dP = inFile_2_dataFrame(inFile)
    
    # 2 Plots the sold price map graph with a colour bar. 
    #    2.a Prepares for plot with figure size, selected colour and colour boundaries.
    graphSize = int(graphSize)
    fig,ax = plt.subplots(figsize=(graphSize,graphSize))
    cmap = colors.ListedColormap(['yellow','pink','red', 'green', 'cyan'])
    bounds = [0, 5, 25, 75, 95,100]
    norm = colors.BoundaryNorm(bounds, cmap.N)
    
    #    2.b Plots the sold price map graph.
    dotSize = int(dotSize)
    ax.scatter(dX, dY,c=dP,cmap=cmap, norm=norm,s=dotSize)
    plt.grid()
    ax.set_title('housing prices map')
    
    #    2.c Sets up the colour bar location and plots the colour bar.
    ax2 = fig.add_axes([0.95, 0.1, 0.03, 0.8])
    colorbar.ColorbarBase(ax2, cmap=cmap, norm=norm,
        spacing='proportional', ticks=bounds, boundaries=bounds, format='%1i')
    ax2.set_ylabel('price %')
    
    # 3 Save the plot to a .png file.
    plt.savefig(outFile, bbox_inches='tight')

#######
# SECTION FOR ORGNISING COMMANDLINE INPUTS 
#######

def commandLine_printHelp():
    progName = sys.argv[0]
    progName = progName.split('/')[-1] # Strip out extended path if any.
    help = __doc__.replace('<PROGNAME>', progName, 1)
    print('-' * 60, help, '-' * 60, file=sys.stderr)
    sys.exit() #Normal exit.
    
def commandLine_flagOptions():
    # 1. Validating the command line inputs.
    #    1.a. Checking command line syntax.
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'h:i:o:g:d:') #beware the last ':'
    except getopt.GetoptError:
        sys.exit(2) #Use exit(2) for command line syntax errors and exit(1) for all other kind of errors.
    opts = dict(opts)
    
    #    1.b. If the are no flags.
    if len(args) > 0: # Do a sys input check.  
        print("\n** ERROR: no arg files - only options! **", file=sys.stderr)
        commandLine_printHelp()
    
    #2 Generic & specified error messages based on flag info (for mandatory inputs).
        #2.a print out general help message if calling -h
    if '-h' in opts:
        commandLine_printHelp()
        #2.b if mandatory inputs missing
    if '-i' not in opts:
        print("\n** ERROR: must specify input text file (opt: -i)! **", file=sys.stderr) 
        commandLine_printHelp()
    
    if '-o' not in opts:
        print("\n** ERROR: must specify output text file (opt: -o)! **", file=sys.stderr)
        commandLine_printHelp()
    
    # 3 Give default values for optional inputs/flags.
    if '-g' not in opts:
        opts['-g'] = 6 # Default graph size.
    
    if '-d' not in opts:
        opts['-d'] = 5 # Default dot size.
        
    return opts
    
#######
# RUN WHOLE PROGRAMME USING MAIN FUNCTION
#######
    
def main():
    # 1 Sets up help and simple validations for command line flag inputs.
    opts = commandLine_flagOptions()
    
    # 2 Links the sys input to the function's input.
    inFile = opts['-i']
    outFile = opts['-o']
    graphSize = opts['-g']
    dotSize = opts['-d']
    
    # 3 Runs the dataFrame_2_plot function to generate the sold price map graph.
    dataFrame_2_plot(inFile,outFile,graphSize, dotSize)

if __name__ == '__main__':
    main()
