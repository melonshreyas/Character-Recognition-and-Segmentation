# Character-Recognition-and-Segmentation using SVM
The License Plate have been extracted from Preprocessing Step and then Character segmenation is done using Connected Component Analysis based on the width, height and area we can threshold the values and segment the characters.
<br/>
For Recognition Training of characters is used Alphabets(A-Z) and Numerals(0-9) each having 25images and Trained for 17 images and Genetrate the .sav file.
<br/>
Then the segment characters are then passed to the Recognizer for Recognition of Characters using Support Vector Machine(SVM).

# Character Segmentation
Standard license plates offer a great advantage in LPR because they mostly consist ofsmooth backgrounds and highly contrasted characters. A smaller percentage of vehiclescarry standard license plates. However, the license plates with different stylish fonts areincreasing in popularity, and it is important to consider strategies for proper segmentationand recognition since significant majority of vehicles carry such license plate. In thischapter, the segmentation of alphanumeric symbols from the license plate is discussed.Performance of the character recognition module in LPR, will rely heavily on the efficiency
of the plate text segmentation.<br/>

# Connected Component Analysis Approach
The CCA can be applied to an entire license plate. Each object extracted is thus acharacter extracted. Hence this method of character extraction requires the characters tobe just separated in the license plate. The objects with very small or a very large widthor height can be neglected as they dont correspond to characters.The CCA stats for sample image is as shown in the Figure 5.3. Based on the aspect ratio,area and height of characters, extraction of the characters from the license plate is shownin Figure.
#
#
![](a40.jpg)
![](b40.jpg)

# Support Vector Machine Classification
SVM belongs to kernel methods or class of maximum margin hyperplane classifiers. The SVM map data from original space to the higher dimensional feature space. SVM classifier is utilized for recognition between two classes by finding a optimum hyperplane that has most extreme separation to the closet points in the preparation set named as support vectors.

SVM is used as a multi - class classifier. One against one is the approach employed for the classification. The system is
trained with the number of classes set at 36 including 10 numerals and 26 English alphabet letters. The size of segmented characters varies greatly. In this phase, all characters are standardized by image mapping technique to a size of 27 X 36.

