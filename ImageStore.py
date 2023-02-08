import numpy as np

# Initialize the data array
data = []

# Loop over the images and labels
for image, label in zip(images, labels):
    # Resize the image to a fixed size (e.g., 32x32)
    image = cv2.resize(image, (32, 32))
    # Flatten the image into a 1D array
    image = image.flatten()
    # Add the image and label to the data array
    data.append(np.concatenate((image, [label])))

# Convert the data array to a numpy array
data = np.array(data)
