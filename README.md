# return-marked-files

## Setup:
1. The `marked-files/` folder will contain files that will be uploaded to corresponding student submissions as comments.
Files in the `marked-files/` folder must have the following naming format: `"<firstnamelastname>_<StudentID>_<SubmissionID>_<assignment_name>.<ext>"`, 
such as `"johnsmith_1234567_98765432_earth_assignment.html"`.
2. Navigate into home project folder:  
`$ cd return_marked_files/`
4. Create conda environment:  
`$ conda env create`
6. Activate conda environment:  
`$ conda activate marked_files`
8. Obtain Canvas API token and place it in 'token.yml' file in project home folder. See [here](https://carolz19.github.io/quiz_mill/canvas-api.html) for how to get the token.

## Usage on command-line: 
`python return_marked_files.py COURSEID ASSIGNMENTID`  
  
ARGUMENTS:  
**COURSEID** := Required argument. The course ID that can be found in Canvas URL.  
**ASSIGNMENTID** := Required argument. The assignment ID that can be found in Canvas URL.  
  
Example:  
`$ python return_marked_files.py 51824 1047215`
