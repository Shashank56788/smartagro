import tensorflow as tf
from tensorflow.keras import layers, models
import os

print("🚀 Starting Disease Detection Model Training...\n")

# ================================
# DATASET PATH
# ================================
DATASET_PATH = "dataset/PlantVillage"

train_path = os.path.join(DATASET_PATH, "train")
val_path = os.path.join(DATASET_PATH, "val")

# ================================
# LOAD DATASET
# ================================
train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    train_path,
    image_size=(224, 224),
    batch_size=32
)

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    val_path,
    image_size=(224, 224),
    batch_size=32
)

class_names = train_ds.class_names
print("\n📊 Classes found:", class_names)

# ================================
# NORMALIZATION
# ================================
normalization_layer = layers.Rescaling(1./255)

train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))
val_ds = val_ds.map(lambda x, y: (normalization_layer(x), y))

# ================================
# MODEL ARCHITECTURE
# ================================
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
    layers.MaxPooling2D(),

    layers.Conv2D(64, (3,3), activation='relu'),
    layers.MaxPooling2D(),

    layers.Conv2D(128, (3,3), activation='relu'),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),

    layers.Dense(len(class_names), activation='softmax')
])

# ================================
# COMPILE MODEL
# ================================
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.summary()

# ================================
# TRAIN MODEL
# ================================
print("\n⏳ Training started...\n")

history = model.fit(
    train_ds,
    validation_data=val_ds,
    epochs=5
)

# ================================
# SAVE MODEL
# ================================
os.makedirs("models", exist_ok=True)
model.save("models/disease_model.h5")

print("\n✅ Model training completed!")
print("📁 Saved at: models/disease_model.h5")