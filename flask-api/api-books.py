from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten

app = Flask(__name__)

# Sample data (can be replaced with a database)
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Flask Development", "author": "Jane Smith"}
]

# Read all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Read a specific book
@app.route('/books/<int:id>', methods=['GET'])
def get_book(id):
    book = next((book for book in books if book['id'] == id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Create a new book
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()
    new_book = {"id": len(books) + 1, "title": data['title'], "author": data['author']}
    books.append(new_book)
    return jsonify(new_book), 201

# Update a book
@app.route('/books/<int:id>', methods=['PUT'])
def update_book(id):
    data = request.get_json()
    book = next((book for book in books if book['id'] == id), None)
    if book:
        book.update(data)
        return jsonify(book)
    else:
        return jsonify({"message": "Book not found"}), 404

# Delete a book
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    global books
    books = [book for book in books if book['id'] != id]
    return jsonify({"message": "Book deleted"}), 200

# Endpoint for uploading image
@app.route('/books/upload', methods=['POST'])
def upload_image():
    # Check if a file is in the request
    if 'image' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['image']

    # If the user submits an empty part without a filename
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Assuming you want to save the image to a directory named 'uploads'
    # Make sure the 'uploads' directory exists
    # file.save('files/' + file.filename)
    file.save('files/' + "digit.png")

    return jsonify({'message': 'File successfully uploaded'}), 200


# Endpoint for classification image
@app.route('/books/classify', methods=['GET'])
def classify_image():
    # Load the pre-trained model
    model = load_model('./model/model.h5')

    # Preprocess input images
    def preprocess_image(image_path):
        img = Image.open(image_path).convert('L')  # Convert to grayscale
        img = img.resize((28, 28))  # Resize to the input size expected by the model
        img_array = np.array(img)  # Convert image to numpy array
        img_array = img_array / 255.0  # Normalize pixel values
        img_array = img_array.reshape((1, 28, 28))  # Reshape to match model input shape
        return img_array

    # Perform inference
    def predict_digit(image_path):
        preprocessed_img = preprocess_image(image_path)
        prediction = model.predict(preprocessed_img)
        predicted_class = np.argmax(prediction)
        return predicted_class

    # Example usage
    image_path = './files/digit.png'
    predicted_digit = predict_digit(image_path)
    return (f'Predicted digit: {predicted_digit}')


# Endpoint for training image
@app.route('/books/train', methods=['GET'])
def train_image():
    # Load the MNIST dataset
    (x_train, y_train), (x_test, y_test) = mnist.load_data()

    # Normalize the pixel values to range [0, 1]
    x_train, x_test = x_train / 255.0, x_test / 255.0

    # Define the model
    model = Sequential([
        Flatten(input_shape=(28, 28)),  # Flatten the input images
        Dense(128, activation='relu'),  # Fully connected layer with 128 units
        Dense(10, activation='softmax') # Output layer with 10 units (one for each digit)
    ])

    # Compile the model
    model.compile(optimizer='adam',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

    # Train the model
    model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))
    model.save("./model/model.h5")

    return "Model Saved Successfully"

if __name__ == '__main__':
    app.run(debug=True)
