# SoldPriceMap
#### For the () Backend role

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

