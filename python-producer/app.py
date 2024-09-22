from flask import Flask, request, render_template
from flask_restx import Api, Resource, fields
from flask_restx import reqparse
from werkzeug.datastructures import FileStorage
from markupsafe import escape
import os
from producer import cut_image
from flask import send_from_directory
from PIL import Image

app = Flask(__name__)
api = Api(app, version='1.0', title='Image Upload API',
          description='A simple API to upload images')


# Define a request parser for file upload
upload_parser = api.parser()
upload_parser.add_argument('file', location='files', type=FileStorage, required=True, help='The image file')

@api.route('/upload')
class UploadImage(Resource):
    @api.expect(upload_parser)
    def post(self):
        args = upload_parser.parse_args()
        uploaded_file = args['file']  # Get the uploaded file as a FileStorage object
        
        if uploaded_file.filename == '':
            app.logger.info(f"Someting went wrong with the file upload")
            return {"error": "No file selected"}, 400
        
        # Save the file in the uploads directory
        uploaded_file.save(f"/shared/{uploaded_file.filename}")
        cut_image(path=f"/shared/{uploaded_file.filename}")
        
        app.logger.info(f"File {uploaded_file.filename} uploaded successfully")
        return {"message": "File successfully uploaded"}, 201
    
@api.route('/talk')
# Define a class-based resource
class Talk(Resource):
    def get(self):
        return {"message": "Hello, World!"}
    
# Define the path to the shared directory
SHARED_FOLDER = '/shared'

def is_image(file_path):
    try:
        Image.open(file_path)
        return True
    except IOError:
        return False

@app.route('/display')
def index():
    # List all images in the shared directory
    images = [f for f in os.listdir(SHARED_FOLDER) if is_image(os.path.join(SHARED_FOLDER, f))]
    
    # Create a list to hold image pairs
    image_pairs = {}
    
    for image in images:
        # Check for centered version
        if image.endswith('_center'):
            base_name = image[:-len('_center')]
            if base_name not in image_pairs:
                image_pairs[base_name] = [None, None]  # [normal, centered]
            image_pairs[base_name][1] = image  # Centered image
        else:
            base_name = image
            if base_name not in image_pairs:
                image_pairs[base_name] = [None, None]  # [normal, centered]
            image_pairs[base_name][0] = image  # Normal image

    return render_template('index.html', image_pairs=image_pairs)

@app.route('/shared/<path:filename>')
def send_shared_file(filename):
    return send_from_directory(SHARED_FOLDER, filename)

if __name__ == '__main__':
    app.run(debug=True)