# STUDENT_PERFORMANCE_USING_ML_AND_FLASK
<h3>TITLE</h3>

STUDENT PERFORMANCE USING ML AND FLASK
<h3>INTRODUCTION</h3>

The project is a Flask-based web application that leverages machine learning to predict student scores based on two key input parameters: the number of courses a student is taking and the amount of time they dedicate to studying. This application provides a user-friendly interface for users to input their academic information, after which it employs a pre-trained machine learning model to estimate their academic performance.

<h3>METHODOLOGY</h3>
<h3>RESULT</h3>

<img width="960" alt="output" src="https://github.com/Rohanpophale/STUDENT_PERFORMANCE_USING_ML_AND_FLASK/assets/97818946/59122688-fe14-4d70-a556-53f55bc0cb3c">

<h3>OUTPUT</h3>

<img width="960" alt="landing page" src="https://github.com/Rohanpophale/STUDENT_PERFORMANCE_USING_ML_AND_FLASK/assets/97818946/70be86c1-c53c-4a6f-b6ae-7b19bc8de89a">

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
