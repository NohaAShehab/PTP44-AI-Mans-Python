import json


def get_all_students():
    try:
        with open('students.json', 'r') as myfile:
            data = myfile.read() #  string
            if data:
                # print("found")
                # print(data, type(data))
                # convert to list of dicts
                json_data = json.loads(data)
                return  json_data  # list of dicts
            else:
                # file is empty ---> return with empty list
                return  []

    except Exception as e:
        print(e)


def save_all_students(students_data: list):
    # convert list --> to list of json objects --> prepare as string for saving
    students_data= json.dumps(students_data, indent=2)
    try:
        with open('students.json', 'w') as myfile:
            myfile.write(students_data )
            return  True

    except Exception as e:
        print(e)

    return  False

def save_student(studentdata):  # data is dict
    old_data= get_all_students() # list of dicts
    old_data.append(studentdata)
    # print(f"old_data= {old_data}")
    # convert data to array of json --> then to string
    saved = save_all_students(old_data)
    

