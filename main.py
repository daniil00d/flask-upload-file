from flask import Flask, render_template, jsonify, request, redirect
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage


UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__, template_folder='public')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/load_file', methods=['GET', 'POST'])
def upload_file():
  if request.method == 'POST':
    uploaded_file = request.files['file']

    if uploaded_file.filename == '':
      flash('No selected file')
      return redirect('/')

    filename = secure_filename(uploaded_file.filename)
    rel_filename = f"{UPLOAD_FOLDER}/{filename}"
    if uploaded_file and allowed_file(uploaded_file.filename):
      uploaded_file.save(rel_filename)

      with open(rel_filename,'r') as file:
        countriesStr = file.read()
      
      print(countriesStr)
      return 'file uploaded successfully'
    else:
      return 'error'

  return 'endpoint method must be POST'

if __name__ == '__main__':
  app.run()