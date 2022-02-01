import os
import shutil
from flask import Flask,request,render_template
from werkzeug.utils import secure_filename

import test_cases
import helper

WD = os.getcwd()
actual_output_path = os.path.join(WD,'actual_outputs')
UPLOAD_FOLDER = WD + '/uploads'




app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET'])
def upload():
    
    
    context = {}
    return render_template('upload.html', context=context)

@app.route('/', methods=['POST'])
def check():
    
    email = request.form['email']
    name,host = email.split('@')
    score=0
    
    user_path = os.path.join(app.config['UPLOAD_FOLDER'], name)
    if not os.path.isdir(user_path):
        os.mkdir(user_path)
        
    for assignment in request.files:
        
        file = request.files[assignment]
        filename = secure_filename(file.filename)
        path = os.path.join(user_path, assignment)
        additional_files = test_cases.additonal_files[assignment]
        
        
        if not os.path.isdir(path):   
            if len(os.listdir(additional_files)) > 0:
                dest = shutil.copytree(test_cases.additonal_files[assignment], path)
            else:
                os.mkdir(path)
        
        file.save(os.path.join(path, filename))
        
        input_file  = os.path.join(path, filename)
        output_file = os.path.join(path, filename[:-3]) + '.txt'
        
        for input,expected_output_file in test_cases.assignment_tests[assignment]:
            if input != "":
                os.system(f"cd uploads/{name}/{assignment} && python3 {assignment}.py <<< {input} > {output_file}")
            else:
                os.system(f"cd uploads/{name}/{assignment} && python3 {assignment}.py > {output_file}")
            
            if assignment != 'assignment2':
                result = helper.comparator(expected_output_file, output_file)
            else:
                result = helper.check_assignment2(path)
                pass
            
            if result:
                score+=10
            else:
                print(assignment)
                print("Failed for input: ", input)
                
       
        
        

    context = {"score": score}

    return render_template('score.html', context=context)





if __name__ == "__main__" :
    app.run()