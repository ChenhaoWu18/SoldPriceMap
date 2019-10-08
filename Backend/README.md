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

* The libraries used are: matplotlib, pandas, numpy, sys, & getopt.
