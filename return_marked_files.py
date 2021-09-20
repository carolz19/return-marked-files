from canvasapi import Canvas
import yaml
from pathlib import Path
import os

"""
Submission file names will have the form: 
firstnamelastname_studentid_submissionid_assignmentname.____
"""

def parse_file_name(f):
    return "lol"


def create_marked_files_dict(path) :
    content = os.listdir(path)
    marked_files = {}

    for f in content:
        print(f)
        file_path = os.path.join(path, f)
        
        if os.path.isfile(file_path):
            stu_id = parse_file_name(f)
            marked_files[stu_id] = file_path


def main(assignment_id):
    '''Initialize dictionaries'''
    marked_files = create_marked_files_dict("./marked_files/")
    # submissions = create_submissions_dict()

    '''Connect to Canvas'''
    path_to_token = Path(".").resolve()
    file = open(path_to_token / "token.yaml")
    token = yaml.load(file, Loader=yaml.FullLoader)

    API_URL = "https://canvas.ubc.ca/"
    API_KEY = token

    canvas = Canvas(API_URL, API_KEY)
    
    '''Get submissions'''
    course = canvas.get_course(51824)
    assignment = course.get_assignment(assignment_id)
    submissions = assignment.get_submissions()
    for submission in submissions: print(submission)

if __name__=="__main__":
    assignment_id = 1047215
    main(assignment_id)