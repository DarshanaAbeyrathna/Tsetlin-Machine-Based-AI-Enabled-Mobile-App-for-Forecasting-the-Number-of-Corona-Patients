# AI enabled mobile app based on Tsetlin Machine to forecast Corona patients in different countries
In this project, you will learn how to create an AI enabled mobile app based on Tsetlin Machine (a new machine learning algorithm) using Kivy to forecast Corona patients in different countries


## Procedure

* In order to obtain more accurate predictions, Corona incidences in the "data" folder should be updated and Regression Tsetlin Machine (RTM) should be retrained.

* At end of training, four .npy files will be generated for each country.

* Resulting .npy files, images in the "Image" folder, and "main.py" file should be placed in the same directory.

* At this stage, you can run the "main.py" file and see how the app works.

* In order to build the application, see the instructions on https://kivy.org/doc/stable/guide/packaging.html.

* Once the suppoting packages on https://kivy.org/doc/stable/guide/packaging-android.html are installed, create the buildozer by running ``` "buildozer init" ``` command.

* In the generated "buildozer.spec" file, add ".npy" and ".gif" extensions to the ``` "source.include_exts" ``` property. 

* Now for an example, build the mobile application for Android by running "buildozer android debug deploy run" command.


<img src="https://github.com/DarshanaAbeyrathna/AI-enabled-mobile-app-based-on-Tsetlin-Machine/blob/master/first.PNG" width="600" height="550">
