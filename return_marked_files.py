from canvasapi import Canvas
import yaml
from pathlib import Path
import os
import sys

"""
Submission file names will have the form: 
firstnamelastname_studentid_submissionid_assignmentname.____
"""

'''Return dictionary with key as student id and corresponding submission 
file path as value '''
def create_marked_files_dict(path) :
    content = os.listdir(path)
    marked_files = {}

    for f in content:
        file_path = os.path.join(path, f)
        
        if os.path.isfile(file_path):
            stu_id = f.split('_')[1]
            marked_files[stu_id] = file_path

    return marked_files

'''Return dictionary with key as student id and corresponding canvas submission as value '''
def create_submissions_dict(canvas, course_id, assignment_id):
    submissions_dict = {}
    submissions = get_submissions(canvas, course_id, assignment_id)
    for submission in submissions:
        stu_id = str(submission).split('-')[1]
        submission_id = submission
        submissions_dict[stu_id] = submission_id

    return submissions_dict


'''Connect to Canvas'''
def connect_to_canvas():
    path_to_token = Path(".").resolve()
    file = open(path_to_token / "token.yml")
    token = yaml.load(file, Loader=yaml.FullLoader)

    API_URL = "https://canvas.ubc.ca/"
    API_KEY = token

    canvas = Canvas(API_URL, API_KEY)
    return canvas


'''Get submissions for assignment'''
def get_submissions(canvas, course_id, assignment_id):
    course = canvas.get_course(course_id)
    assignment = course.get_assignment(assignment_id)
    submissions = assignment.get_submissions()
    return submissions

'''Driver program to upload files as comments to Canvas'''
if __name__=="__main__":
    '''Specify course and assignment id'''
    course_id = ''
    assignment_id = ''
    try:
        course_id = str(sys.argv[1])
        assignment_id = str(sys.argv[2])
    except:
        print('ERROR: Must input course ID and assignment ID.')
    path_to_files = "./marked_files/"

    canvas = connect_to_canvas() 

    '''Initialize dictionaries'''
    marked_files_dict = create_marked_files_dict(path_to_files)
    submission_dict = create_submissions_dict(canvas, course_id, assignment_id)

    '''Upload files as comments on submissions'''
    for stu_id in marked_files_dict:
        if stu_id in submission_dict:
            (is_success, json) = submission_dict[stu_id].upload_comment(marked_files_dict[stu_id])
            if is_success:
                print(f'File successfully uploaded to submission {submission_dict[stu_id]} for student {stu_id}.')
            else:
                print(f'ERROR: Failed for submission {submission_dict[stu_id]} for student {stu_id}\n. {json}')
