# EfficientNetVsCONV5
1. Download the files named "test.zip.007", "train.zip.005", "sampleSubmission.csv.zip", and "trainLabels.csv.zip" from the Kaggle diabetic retinopathy dataset wbsite in the following link: https://www.kaggle.com/competitions/diabetic-retinopathy-detection/data.
2. Extract the files. Store the test and train folders, along with the sampleSubmission.csv and trainLabels.csv files in the same directory titled diabeticRetinopathy.
3. In the same link, click on the discussion tab on the website and click on the pinned topic named "Solution File". Download the file named "retinopathy_solution.csv" attached to this topic. Save this file in the same directory specified in step 2.
4. Launch a python IDE like Anaconda Spyder or use the command prompt for the following steps.
5. Navigate to the diabeticRetinopathy directory containing the files specified in step 2 and 3. Store the files named "sortDR.py", "sortTestDR.py", and "trainValSplitDiabeticRetinopathy.py" from this repository in the diabeticRetinopathy directory. Execute the file named "sortDR.py" by running the command python sortDR.py. Do the same with the file named "sortTestDR.py" afterwards.
6. Execute the file named "trainValSplitDiabeticRetinopathy.py" by running the command python trainValSplitDiabeticRetinopathy.py.
7. Download the folders named 'test' and 'train' containing the subfolders 'benign' and 'malignant' as specified in the data explorer of the following Kaggle Skin Cancer: Malignant vs. Benign website link by clicking the download button near the top right-hand side of the page: https://www.kaggle.com/datasets/fanconic/skin-cancer-malignant-vs-benign.
8. Extract all folders and store in another directory titled skinCancer. Store the file named "trainValSplitSkinCancer.py" in the skinCancer directory.
9. Execute the file named "trainValSplitSkinCancer.py" by running the command python trainValSplitSkinCancer.py
10. In each directory, diabeticRetinopathy and skinCancer, there should now be three folders named train, test, and val. In each of these three folders, for the diabeticRetinopathy directory, there should be two more folders named normal and anomaly and for the skinCancer directory, there should be two more folders named benign and malignant.
11. Open your own Google drive account and upload both of these directories: diabeticRetinopathy and skinCancer to your Google drive.
12. Open colab.research.google.com and upload the file from this repository titled EfficientNetVsConv5.ipynb.
13. It is strongly suggested to utilize the GPU that Google Colab Pro offers for the purposes of this comparison pipeline. To do so, click on the tab titled runtime and select "change runtime type". Then, under the hardware accelerator dropdown, select GPU.
14. Click on the tab titled runtime and select "Run all".
