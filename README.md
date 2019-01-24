# Br0c0de
Develop a python application to generate computer code (HTML source code) for the GUI sketch which is provided as an input.

## Inspiration
In the current day e-commerce world, every business needs a platform to showcase it's existence and reach. This can be done quickly and can reach a great number of audience over the internet, using  websites. Every business needs a good looking, simple and responsive website that shows information about their profession and be able to interact with their customers for many purposes like feedback, reviews and many more. But not everyone is a web developer. Companies need to hire web developers and designers to develop a website for them. 
Our motive is to make web development for such customers easier and a creative task.

## Our Solution
To overcome this problem and encourage people who aren't keen in learning computer languages to develop websites, we developed an 	application, an application that can transform a graphical user interface screenshot into computer code in order to build customized websites.

### Workflow
* User pens down a user interface sketch on a sheet of paper.
* He/she scans the page and generates a .png image of it.
* Provides the .png file to the Python application.
* Choose the theme and colour grading of the theme.
* Obtains a fully functional HTML structure of code.
* Also, the site is made live, as soon as the code is generated.

![wf1](https://user-images.githubusercontent.com/39125026/51636053-470ebf80-1f7e-11e9-918a-317b3d4f5ced.jpg)

![wf2](https://user-images.githubusercontent.com/39125026/51651572-7fc88c00-1fb2-11e9-8343-d24bec6d11c6.png)

## Establishing Phone Camera Scanner
* Application used : IP Webcam
### Python code
```
 urllib.urlretrieve("http://192.168.43.1:8080/shot.jpg","./index.jpg")
	Image.open("./index.jpg").save("./index.png")
	png_path="./index.png"
 ```

## Arguments Passed
```
python con_image.py --png_path ../examples/index.png --output_folder ./output_html --model_json_file ./weights/json_model.json --model_weights_file ./weights/weights.h5
```
Note: The user also requires the weights which are not in this repo because of the extended overheads. 

## Technology Stack
* Convolution Neural Network
* Recursive Neural Network (LSTM)
* OpenCV (To preprocess the given Image)
* Various Other python modules that is used in Deep learning like NumPy, SciPy, Matplotlib.
* HTML
* Bootstrap (to make the site responsive)

## Additional Perks (Security) [MIDNIGHT SURPRISE]
As our project is generally for non-techinical users, we assume they dont understand the *difference between HTTPS and HTTP protocols*. To address this problem, we have implemented additional configuration in the server side which redirects the user to HTTPS in case they have used HTTP. This would prevent them from *MITM (Man In The Middle) attacks* carried out by intruders.
We have implemented this in the *sslconfiguration.conf* file, in the repo above.

* We are trying to implement a python script that detects *DDOS attacks* on the particular website, and inform the user (owner) about the attack *via e-mail*, and once thats done, we would take down the server immediately to avoid further damage.



## Dependencies
* Keras
* Numpy
* Opencv
* Tensorflow

## I/O
![output](https://user-images.githubusercontent.com/39125026/51658021-a398cb80-1fcc-11e9-84b7-b502e184b916.jpg)

## Future Implementations
We are we keen in making this project a real world application and handy to use.
We are currently working on generating webpages. Further we would want to expand the reach of this project into Android app development.
* Making it market ready by developing a standalone application which is open source.
* Making the system open source would encourage contributers to generate more themes and add new externsions to the base application. 





 





