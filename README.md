# Warehouse Apparel Detection

- End to end object detection project using YOLOV5.
- The training is done using YOLO V5 framework.
- The application is served as an REST API using Flask.


# Steps to run the application 

### Setting up  virtual environment.

- What is [**Virtual Environment in python ?**](https://www.geeksforgeeks.org/python-virtual-environment/)
- [Create virtual environment in python](https://www.geeksforgeeks.org/creating-python-virtual-environment-windows-linux/)
- [Create virtual environment Anaconda](https://www.geeksforgeeks.org/set-up-virtual-environment-for-python-using-anaconda/)
- create a virtual environment and install [requirements.txt](https://github.com/R-aryan/Chess_Piece_Detection_Using_SSD/blob/main/requirements.txt)

> pip install -r requirements.txt

### For Inference
- After performing the above steps go to [**app.py**](https://github.com/R-aryan/Warehouse_Apparel_Detection/blob/main/app.py) and run **app.py**
> python app.py
- After running the **app.py** the web app can be accessed at **http://127.0.0.1:9500/** copy this url and paste it in your browser.
- The UI will look like the following.

![Sample UI](https://github.com/R-aryan/Warehouse_Apparel_Detection/blob/main/msc/sample_input_1.PNG)
  <br>
  <br>

- The picture can be uploaded using the **upload** button and after uploading the image click on **predict** to perform inference.
- Sample Input

![Sample Input](https://github.com/R-aryan/Warehouse_Apparel_Detection/blob/main/msc/sample_input_2.PNG)
  <br>
  <br>

- Sample Output

![Sample output](https://github.com/R-aryan/Warehouse_Apparel_Detection/blob/main/msc/sample_output.PNG)
  <br>
  <br>

- The application logs can also be found [here](https://github.com/R-aryan/Warehouse_Apparel_Detection/tree/main/logs).

### For Training

- The training notebook can be found [here](https://colab.research.google.com/drive/1i1GmImbOt0zp6MDPHE-cUvYf9tFDOqi6?usp=sharing)
- Due to system/hardware limitations it was not possible to perform training locally.
- So google colab and google drive was used for training purpose.
 


 
