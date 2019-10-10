from django.shortcuts import render
import pandas as pd
import numpy as np
from bokeh.models import  FixedTicker, LinearColorMapper, PrintfTickFormatter, ColorBar
from bokeh.plotting import figure
from bokeh.layouts import row
from bokeh.embed import components


def homepage(request):  
    infileName = 'main/sold-price-data.txt'
    plot_title='Housing price map'
    
    dot_size = 3
    col_type=['yellow','pink','red', 'green', 'cyan']
    bounds = [0, 5, 25, 75, 95,100]
    
    plot_components = plotMap(infileName, plot_title, dot_size, col_type, bounds)

    script, div = plot_components
    return render(request, 'main/base.html', {'script':script, 'div':div})


def plotMap(infileName, plot_title, dot_size, col_type, bounds):
    #1. get list of X, Y, P values from dataframe
    dX, dY, dP = file2Dataframe('main/sold-price-data.txt')
    
    #2 assign colors to each P value using colorRange       
    colors=colorRange(dP)
    
    #3 prepare for the plot, some tools can be removed    
    TOOLS='hover,crosshair,pan,wheel_zoom,zoom_in,zoom_out,box_zoom,undo,redo,reset,tap,save,box_select,poly_select,lasso_select,'
    p = figure(title=plot_title, tools=TOOLS)
    p.title.align="center"
    p.grid.grid_line_color = 'black'
    p.axis.axis_line_color = 'black'
    p.axis.major_tick_line_color = 'black'
    p.axis.major_label_text_font_size = '10pt'

    # 4 draw dots with color coresponding to the P value in X, and Y coordinates.
    p.circle(x=dX, y=dY,  size=dot_size, color=colors, line_color=None)
    
    # 5 mapping color bar color same with the plot and fix the ticker boundaries.
    palette_c = [ "yellow" ]*5 + ["pink"]*20 + ["red"]*50 + ["green"]*20 + ["cyan"] *5
    #Then this palette could be used with a LinearColorMapper with low, high = (0, 100).
    mapper = LinearColorMapper(palette=palette_c, low=dP.min(), high=dP.max())
    
    ticker = FixedTicker(ticks=bounds)
    
    color_bar = ColorBar(color_mapper=mapper, major_label_text_font_size='5pt',
                         ticker=ticker,
                         formatter=PrintfTickFormatter(format='%d%%'),
                         label_standoff=6, border_line_color=None, location=(0, 0))
    
    # 6 give title to color bar
    color_bar_p = figure(title='price %',title_location="right", 
                        width=110, toolbar_location=None, 
                        outline_line_color=None)
    
    color_bar_p.add_layout(color_bar, 'right')
    color_bar_p.title.align="center"
    layout=row(p, color_bar_p)
    
    # 6 output the component of the plot to web
    return components(layout)


def file2Dataframe(inFile):
    X = 'X' 
    Y = 'Y'
    P = 'P'
    df = pd.read_table(inFile, delim_whitespace=True, names=(X, Y, P),
                       dtype={X: np.float64, Y: np.float64, P: np.float64})

    scaleP = df[P].max() - df[P].min()
    df[P] =df[P]*100/scaleP
    return df[X], df[Y], df[P]
    

def colorRange(lst):
    cols=[]
    for l in lst:
        if 0 <= l <= 5:
            cols.append('yellow')
        elif 5 < l <= 25:
            cols.append('pink')
        elif 25 < l <= 75:
            cols.append('red')
        elif 75 < l <= 95:
            cols.append('green')
        else:
            cols.append('cyan')
    return cols

