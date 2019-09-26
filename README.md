# SoldPriceMap
#### For the Backend/junior role

- Go to the [Backend](Backend) folder:
  Download the [readdata_pandas_plt](Backend/readdata_pandas_plt.py) file;
  Save it in the same folder as sold-price-data.txt 
  
- Example command in terminal: 
  python readdata_pandas_plt.py sold-price-data.txt spm.png 6 8
  
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

#### Simple website demo
Please clone this repo for easier running of the code.
- Go to [FullStack](FullStack) folder.
  * If you have copied/cloned all folders and files from FullStack dir:
  
   Run the command: python manage.py runserver
   
   Open the local server http://127.0.0.1:8000/
  
<img src='/FullStack/webDemo.png' height="50%" width="50%">

The plot in this version was used by bokeh library. I have run out of time on this, but it would be great to know how to display the colorbar in the proportional style as shown in the first graph.

#### Other work
 - The book I wrote for BT Further junior software engineer training.
 - I have experiment Kivy to write [phone apps](KivyProject_sandbox).
 - Django website for [to do list](DjangoProject_sandbox).
 - Django website for [internal website](CourseWeb_sandbox) of a programme I tought.  
 

