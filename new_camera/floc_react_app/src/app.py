import json
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from db import Image, Floc, DatabaseOperations, start

# Set up app and database
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///floc.db'
db = SQLAlchemy(app)
CORS(app)

# Routes

@app.route("/test", methods=["GET"])
def hello_world():
    return {"message": "Hello, World from Flask!"}

@app.route("/images/", methods=["GET"])
def get_images_data():
    """
    Gets all image data in database
    """
    session = start()
    db_ops = DatabaseOperations(session)
    images = db_ops.session.query(Image).all()
    image_list = []
    for image in images:
        image_dict = {
            "id": image.id,
            "name": image.name,
            "flocs": [{"id": floc.id, "size": floc.size} for floc in image.flocs]
        }
        image_list.append(image_dict)

    db_ops.close()
    return json.dumps(image_list), 200

@app.route("/images/<int:image_id>/data/")
def get_specific_image_data(image_id):
    """
    Gets the image data at for the specified image id
    """
    session = start()
    db_ops = DatabaseOperations(session)
    image = db_ops.session.query(Image).filter_by(id=image_id).first()

    if not image:
        return jsonify({"error": "Image not found"}), 404
    
    image_data = {
        "id": image.id,
        "name": image.name,
        "flocs": [{"id": floc.id, "size": floc.size} for floc in image.flocs]
    }

    db_ops.close()
    return json.dumps(image_data), 200


# Need to create a new column in database to represent the actual image before using upload/get image

@app.route("/upload/", methods=["POST"])
def upload_image():
    """
    Uploads an image to database
    """
    body = json.loads(request.data)
    image_name = body.get('image_name')

    session = start()
    db_ops = DatabaseOperations(session)
    new_image = db_ops.add_image(image_name)

    response = {
        "message": "Image uploaded",
        "image_id": new_image.id
    }

    session.commit()
    db_ops.close()

    return json.dumps(response), 200

#@app.route("/images/<int:image_id>/")
#def get_image(image_id):
  #  """
  #  Gets the image at the specified id
  #  """
  #  session = start()
  #  db_ops = DatabaseOperations(session)
  #  image = db_ops.session.query(Image).filter_by(id=image_id).first()

   # if not image:
   #     return jsonify({"error": "Image not found"}), 404

   # return send_file(image.data, mimetype='image/jpeg')




if __name__ == "__main__":
    app.run(debug=True)
