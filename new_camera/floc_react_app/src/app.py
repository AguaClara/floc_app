import json
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from db import Image, Floc, DatabaseOperations, start
import base64

# from electron import app, dialog, ipcMain


# Set up app and database
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///floc.db"
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
            "image": image.base64_data,
            "flocs": [{"id": floc.id, "size": floc.size} for floc in image.flocs],
        }
        image_list.append(image_dict)

    db_ops.close()
    return jsonify(image_list), 200


@app.route("/images/<int:image_id>/data/", methods=["GET"])
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
        "image": image.base64_data,
        "flocs": [{"id": floc.id, "size": floc.size} for floc in image.flocs],
    }

    db_ops.close()
    return jsonify(image_data), 200


@app.route("/upload", methods=["POST"])
def upload_image():
    """
    Uploads an image to database
    """
    body = json.loads(request.data)
    image_base64_data = body.get("image")
    filePath = body.get("filePath")

    if filePath is None:
        return jsonify({"error": "No file path provided"}), 400
    session = start()
    db_ops = DatabaseOperations(session)
    current_id = db_ops.get_current_image_id()

    if current_id is None:
        image_name = "image0"
    else:
        image_name = f"image{current_id+1}"

    filePath = filePath + "/" + image_name + ".jpeg"
    if "," in image_base64_data:
        image_base64_data = image_base64_data.split(",")[1]
    image_data = base64.b64decode(image_base64_data)
    print(image_base64_data)
    with open(filePath, "wb") as file:
        file.write(image_data)
    new_image = db_ops.add_image(image_name, image_base64_data)

    response = {"message": "Image uploaded", "image_id": new_image.id}

    session.commit()
    db_ops.close()

    return jsonify(response), 200


@app.route("/images/<int:image_id>/", methods=["GET"])
def get_image(image_id):
    """
    Gets the image at the specified id
    """
    session = start()
    db_ops = DatabaseOperations(session)
    image = db_ops.session.query(Image).filter_by(id=image_id).first()

    if not image:
        return jsonify({"error": "Image not found"}), 404

    response = {"image": image.base64_data}
    db_ops.close()

    return jsonify(response), 200


@app.route("/images/latest", methods=["GET"])
def get_last_n_images():
    """
    Gets the last n images
    """
    body = json.loads(request.data)
    n = body.get("limit")
    session = start()
    db_ops = DatabaseOperations(session)
    images = db_ops.session.query(Image).order_by(Image.id.desc()).limit(n).all()
    image_list = []
    for image in images:
        image_dict = {
            "id": image.id,
            "name": image.name,
            "image": image.base64_data,
            "flocs": [{"id": floc.id, "size": floc.size} for floc in image.flocs],
        }
        image_list.append(image_dict)
    db_ops.close()
    return jsonify(image_list), 200

# @app.expose
# def choose_path():
#     print("choose_path called")
#     options = {
#         "title": "Select Save Location",
#         "properties": ["openDirectory"],
#     }

#     # Show the directory selection dialog
#     result = dialog.showOpenDialog(options)
#     print(result)

#     # Return the selected path to the renderer process
#     selected_path = result["filePaths"][0] if result.get("filePaths") else None
#     print("Selected Path (main process):", selected_path)
#     return selected_path


@app.route("/images/<int:image_id>/", methods=["DELETE"])
def delete_image(image_id):
    """
    Deletes the image at the specified id
    """
    session = start()
    db_ops = DatabaseOperations(session)

    image = db_ops.session.query(Image).filter_by(id=image_id).first()

    if not image:
        return jsonify({"error": "Image not found"}), 404

    db_ops.session.delete(image)
    db_ops.session.commit()

    db_ops.close()
    return jsonify({"message": "Image deleted successfully"}), 200

@app.route("/images/", methods=["DELETE"])
def delete_all_images():
    """
    Deletes all images in the database
    """
    session = start()
    db_ops = DatabaseOperations(session)

    images = db_ops.session.query(Image).all()

    for image in images:
        db_ops.session.delete(image)
    db_ops.session.commit()

    db_ops.close()
    return jsonify({"message": "All images deleted successfully"}), 200


if __name__ == "__main__":
    app.run(debug=True)
