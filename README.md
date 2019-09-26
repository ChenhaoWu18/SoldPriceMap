# SoldPriceMap
#### A. Problem description and proposed solution
The problem I tried to solve here is to load the text file data and plot the data into a heatmap style scatter-graph on a website. Please see this flow diagram for the steps I took to solve the problem and the detailed descriptions that follow below:


<img src='flowdia.png' height="50%" width="50%">

```
The steps I took are:
    1. Reading the text file to a dataframe (using pandas.read_csv).
    2. Coverting the price value (P) to relative/percentage price, meaning (P1, P2,...Pn)/(Max_P-Min_P).  
    3. Setting the colour proportions and % boundaries for the plot, for which I used two methods:
      3.1 Using matplotlib.colors.BoundaryNorm to normalise the ListedColormap with suggested boundaries.
      3.2 Using bokeh.plotting for the realtime web plot display. 
         3.2.1 It was not as simple as BoundaryNorm, and I have written a function (colorRange) to locate each colour with different price boundaries.
      3.3 For both approaches, the boundaries of the colour range are: 
        0% - 5%     yellow
        5% - 25%    pink
        25% - 75%   red
        75% - 95%   green
        95% - 100%  cyan
    4. Plotted each point onto a grid. 
        The points are filled with colours representing how expensive a house was in relation to other houses. 
        You are able to choose: 
          - The size of the plot graph.
          - The size of the points.
          - The different input.txt file names. 
          - The output.png file names.
    5. Compromises and assumptions:
      5.1 I ran out of time while working on the plot in the bokeh/web version. Also it would be great to know how to display the colour bar in the proportional style shown in the matplotlib plot.
      5.2 I personally did not have much experience in unit testing, so I would like to add some more to it later.
      5.3 Although diffierent input files can be processed, the data structure has to be X, Y, Z (X and Y for coordinates, Z for price). Otherwise the remaining column would be ignored. Also if there are only two columns of data in the text file, there will be an error. I would like to solve this later.
      5.5 More exceptions and validation needs to be added to validate the inputs.
 ```
#### B. For the Backend/junior role

- Go to the [Backend](Backend) folder:
  Download the [readdata_pandas_plt](Backend/readdata_pandas_plt.py) file;
  Save it in the same folder as sold-price-data.txt 
  
- Example command in terminal: 
  ```
  python readdata_pandas_plt.py sold-price-data.txt spm.png 6 8
  ```
  
  This command wil generate a png file called spm.png with a graph size of 6 and a scatter dot size of 8.
  
  <img src='/Backend/spm.png' height="50%" width="50%">

- Detailed explaination for the inputs:

    * arg1 -  input-text-data-file-name.txt
    * arg2 -  output-graph-file-name.pny
    * arg3 -  The size of the output graph,
            I suggest choosing a number between 5 and 30.
           
    * arg4 -  The size of each scatter point in the graph,
            I suggest choosing a number similar to the graph size,
            so that a larger graph has bigger dots.

#### C. Simple website demo
Please clone this repo for easier running of the code.
- Go to [FullStack](FullStack) folder.
  * If you have copied/cloned all folders and files from FullStack dir:
  
   Run the command: 
   ```
   python manage.py runserver
   ```
   
   Open the local server http://127.0.0.1:8000/
  
<img src='/FullStack/webDemo.png' height="50%" width="50%">



#### D. Other works in my [repositories](https://github.com/ChenhaoWu18)
 - The [books](https://github.com/ChenhaoWu18/BTFurther_modules) I wrote for [BT Further apprentice software engineer training](https://www.codefirstgirls.org.uk/bt--cfg-digital-intensive.html).
 - I have experimented with Kivy to write [phone apps](https://github.com/ChenhaoWu18/KivyProject_sandbox).
 - Django website for [to do list](https://github.com/ChenhaoWu18/DjangoProject_sandbox).
 - Django website for [internal website](https://github.com/ChenhaoWu18/CourseWeb_sandbox) of a programme I [taught](https://oxmedica.com/about/).  
 
#### E. Contact information
Please feel free to give suggestions through my email: chenhao.wu18@gmail.com or through my [LinkedIn] (https://www.linkedin.com/in/chenhao-wu-31985720/)
