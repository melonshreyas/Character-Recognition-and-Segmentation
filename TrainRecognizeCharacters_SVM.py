import os
import numpy as np
import cv2
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
from sklearn.externals import joblib
from skimage.io import imread
from skimage.filters import threshold_otsu

letters = [
            '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y', 'Z'
        ]
#Read the Data
def read_training_data(training_directory):
    image_data = []
    target_data = []
    for each_letter in letters:
        for each in range(24):
            image_path = os.path.join(training_directory, each_letter,each_letter+ '-' + str(each) + '.jpg')
            # read each image of each character
            img_details = cv2.imread(image_path,0)
            # converts each character image to binary image
            ret,binary_image = cv2.threshold(img_details,100,255,cv2.THRESH_BINARY)  
            flat_bin_image = binary_image.reshape(-1)
            image_data.append(flat_bin_image)
            target_data.append(each_letter)

    return (np.array(image_data), np.array(target_data))

def cross_validation(model, num_of_fold, train_data, train_label):

    accuracy_result = cross_val_score(model, train_data, train_label,
                                      cv=num_of_fold)
    print("Cross Validation Result for ", str(num_of_fold), " -fold")

    print(accuracy_result * 100)



print('reading data')
training_dataset_dir = 'F:\MAJOR PROJECT\code exceution\Character Recognition - SVM\Traning'
image_data, target_data = read_training_data(training_dataset_dir)
print('reading data completed')


svc_model = SVC(kernel='linear', probability=True)

cross_validation(svc_model, 4, image_data, target_data)

print('training model')

# let's train the model with all the input data
svc_model.fit(image_data,target_data)

#Save Model

import pickle
print("model trained.saving model..")
filename = 'character_model_svm1.sav'
pickle.dump(svc_model, open(filename, 'wb'))
print("model saved")

