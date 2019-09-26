# SoldPriceMap
#### For the () Backend role

- go to [Backend](Backend) folder:
  download the [readdata_pandas_plt](Backend/readdata_pandas_plt.py) file;
  save it in the same folder with sold-price-data.txt 
  
- example command in terminal: 
  python readdata_pandas_plt.py sold-price-data.txt spm.png 6 8
  
  This command wil generate a png file called spm.png with graph size 6 and scatter dot size 8
  
  <img src='/Backend/spm.png' height="50%" width="50%">

- detail explaination for the inputs

    * arg1 -  input-text-data-file-name.txt
    * arg2 -  output-graph-file-name.pny
    * arg3 -  the size of the output graph,
            suggest choose a number between 5-30.
           
    * arg4 -  the size of each scatter points in the graph,
            suggest choose a number similar with graph size,
            so the larger of the graph the bigger the dots.

#### simple website demo
Please clone this repo for easier run the code.
- go to [FullStack](FullStack) folder.
  * if you have copy/cloned all folder and files from FullStack dir:
  
   run command: python manage.py runserver
   
   open local server http://127.0.0.1:8000/
  
<img src='/FullStack/webDemo.png' height="50%" width="50%">

