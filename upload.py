from flask import request

import os
def upload_File():
    filename = None
    if request.method == 'POST':
        uploadedFile = request.files['file']
        if uploadedFile:
            file_path = os.path.join('uploads', uploadedFile.filename)
            uploadedFile.save(file_path)
            filename = uploadedFile.filename

            file_List = os.listdir('uploads')
    if os.path.exists('uploads'):
        file_List = os.listdir('uploads')
    else:
        file_List = []
    return [file_List]

def delete_File(file_Name):
    file_path = os.path.join('uploads', file_Name)
    if os.path.exists(file_path):
        os.remove(file_path)

"""So this bit of code requires a significant amount of explanation in the sense that it actually does a fair bit of work So the first thing it checks for is the far than when we have your button click with the request log method equal POST this checks if we had clicked into it it will automatically generate the file list of if I was located in the uplift directory However for facilitating a refresh the POST is not always generated but rather in GET As such we have the if else statements blue to cater to that so for instance if once the folder exists and they files within the directory it automatically populates the file list other than that it generates a null or empty file list which allows for a value to be passed to the return for a function which avoids the error of the file list being null but rather an empty or or list."""
