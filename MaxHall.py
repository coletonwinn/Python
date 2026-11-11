import pandas as pd

student_info = {
    "name": ["Zendaya", "Max", "Timothy"],
    "gpa": [4.0,2.4,6.9]
    

}


result = pd.DataFrame([student_info])

print(result)