from flask import Flask, render_template , request
import os
import uuid

from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'user_uploads'
ALLOWED_EXTENSIONS = { 'pdf', 'png', 'jpg', 'jpeg'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/create", methods=["GET","POST"])
def create():
    myid = uuid.uuid1()
    if request.method == "POST":
        print(request.files.keys())
        rec_id = request.form.get("uuid")
        desc = request.form.get("text")
        input_files= [] 
        
        for key, value in request.files.items():
            print(key, value)
            #Upload Files
            file =request.files[key]
            if file :
                filename = secure_filename(file.filename)
                folder_path = os.path.join(app.config['UPLOAD_FOLDER'], rec_id)
                os.makedirs(folder_path, exist_ok=True)
                file.save(os.path.join(folder_path, filename))
                input_files.append(file.filename)
            #Capture the description and save it in a file.
            with open( os.path.join(app.config['UPLOAD_FOLDER'], rec_id ,"decs.txt"), "w") as f:
                f.write(desc)
                
        for fl in input_files:
           with open(os.path.join(app.config['UPLOAD_FOLDER'], rec_id, "input.txt"),"a") as f:
                f.write(f"file '{fl}'\nduration 1\n")
    return render_template("create.html" , myid=myid)

@app.route("/gallery")
def gallery():
    reels = os.listdir("static/reels")
    print(reels)
    return render_template("gallery.html", reels =reels)

app.run(debug=True)