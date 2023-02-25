# Import libraries
from flask import Flask, request
from like_db import LikeDB
# Create an instance of Flask
app = Flask(__name__)
likeDB = LikeDB('like_db.json')
@app.route("/")
def home():
    return "Hello World!"

# End point for getting image
@app.route("/api/addImage", methods=["POST"])
def addImage():
    # Get the image from the request
    if request.method == "POST":
        # Get json data from request
        data = request.get_json(force=True)
        # Get the image id from data
        image_id = data["image_id"]
        # Get the message id from data
        message_id = data["message_id"]
        likeDB.add_image(image_id, message_id)
        print(f'Image id: {image_id} Message id: {message_id}')
@app.route('/api/all-like-dislike', methods=['GET'])
def all_like_dislike():
    data = request.get_json(force=True)
    image_id = data["image_id"]
    like, dislike = LikeDB.all_dislikes(image_id)
    return like, dislike
# Run the app
if __name__ == "__main__":
    app.run(debug=True)

