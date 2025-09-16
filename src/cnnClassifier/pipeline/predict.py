import os
import numpy as np
import base64
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def predict(self):
        model = load_model(os.path.join("artifacts", "training", "model.h5"))
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        result = np.argmax(model.predict(test_image), axis=-1)
        print(result)

        if result[0] == 1:
            prediction = "Healthy"
        else:
            prediction = "Coccidiosis"

        # Encode the image as base64
        with open(self.filename, "rb") as img_file:
            img_base64 = base64.b64encode(img_file.read()).decode('utf-8')

        return [
            {
                "prediction": prediction,
                "status": "success",
                "message": "Prediction completed successfully"
            },
            {"image": img_base64}
        ]