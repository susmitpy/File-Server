from flask import Flask, request, jsonify, render_template, send_from_directory
import os
from flask_ngrok import run_with_ngrok

app = Flask(__name__, static_url_path="")
app.config['UPLOAD_PATH'] = './recd'
run_with_ngrok(app)

def zip_contents():
    os.system("zip -r send_this send")
    os.system("rm -f ./send/*")
    
    
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/download")
def send_files():
    print("Sending files")
    zip_contents()
    return send_from_directory("./",as_attachment=True,filename="send_this.zip")
    
  
@app.route("/upload",methods=["POST"])
def get_files():
    print(request.files)
    if request.method == 'POST' and 'file' in request.files:
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOAD_PATH'], f.filename))
        return 'Upload completed.'
    return jsonify({"Hi":"Hey"})

if __name__ == "__main__":
    app.run()
    
    










