from flask import request
import os

from matplotlib import category

def select_file(uploadedFile, file_type):
    if file_type == "bsh":
        return os.path.join('uploads/BSH/', uploadedFile.filename)
    elif file_type == "pop":        
        return os.path.join('uploads/PO_Pending/', uploadedFile.filename) 
    elif file_type == "aged":        
        return os.path.join('uploads/Aged/', uploadedFile.filename)

def upload_File():
    filename = None
    if request.method == 'POST':
        file_type = request.form.get("file_type")
        uploadedFile = request.files.get("file")
        if uploadedFile:
            file_path = select_file(uploadedFile, file_type)
            uploadedFile.save(file_path)
            bsh_List = os.listdir('uploads/BSH')
            pop_List = os.listdir('uploads/PO_Pending')
            aged_List = os.listdir('uploads/Aged')
    if os.path.exists('uploads'):
        bsh_List = os.listdir('uploads/BSH')
        pop_List = os.listdir('uploads/PO_Pending')
        aged_List = os.listdir('uploads/Aged')
    else:
        bsh_List = []
        pop_List = []
        aged_List = []
    return bsh_List, pop_List, aged_List

def delete_File(folder, file_Name):
    file_path = os.path.join('uploads', folder, file_Name)
    if os.path.exists(file_path):
        os.remove(file_path)

"""So this bit of code requires a significant amount of explanation in the sense that it actually does a fair bit of work So the first thing it checks for is the far than when we have your button click with the request log method equal POST this checks if we had clicked into it it will automatically generate the file list of if I was located in the uplift directory However for facilitating a refresh the POST is not always generated but rather in GET As such we have the if else statements blue to cater to that so for instance if once the folder exists and they files within the directory it automatically populates the file list other than that it generates a null or empty file list which allows for a value to be passed to the return for a function which avoids the error of the file list being null but rather an empty or or list."""

def filepath(file_Name):
    file_path = os.path.join('uploads', file_Name)
    return file_path
