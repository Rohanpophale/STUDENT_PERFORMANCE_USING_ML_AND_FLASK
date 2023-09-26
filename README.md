# STUDENT_PERFORMANCE_USING_ML_AND_FLASK

<h3>HOW TO RUN</h3>
The repository is consist of two folders named as
1. Without_GUI
2. With_gui (Flask)

First folder consist of:
1. Student_Marks.csv : Dataset required for the training of the Machine Learning model.
2. P1_ML_Algo.py : Main Logic file where all the data loading, preprocessing, data spliting in train and test and model building is done.
3. P2_Load_algo_pickel.py : Creating the weights of the model trained in the 'P2_ML_Algo.py' file
4. sm.model : Weighted model which is to be directly used in the HUI based application

Second folder consist of:
1. Folder --> Sample.html : GUI main landing page created using html and css
2. App.py : Actual logic file where flask interaction with the Sample.html file is established,taking the user input information from html file, processing the information using 'sm.model' file which is created previously in the 'Without_GUI' folder which is imported in this folder
3. sm.model : this is weighted model which is imported here to directly use while making the GUI based web application 
