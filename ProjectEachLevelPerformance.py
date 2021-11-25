import csv
import pandas as pd 
import plotly.express as px 

df = pd.read_csv("data.csv")
mean = df.groupby(["student_id", "level"], as_index = False)["attempt"].mean()

fig = px.scatter(
    mean, 
    x = "student_id", 
    y = "level", 
    title = "Student's Performance in each level",
    size = "attempt", 
    color = "attempt", 
    labels = {
        'student_id': 'Student ID',
        'level': 'Level',
        'attempt': 'Attempt'
    }
    )

fig.show()