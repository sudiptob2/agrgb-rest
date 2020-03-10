# Ag RGB rest API

This rest API is developed to detect mungbean leaf diseases using image processing. This API receives an Image and process it and evaluate it with our ML model. It replies with a JSON response which includes the detected disease.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

* Python 3.7
* Flask
* Tensorflow
* Keras
* OpenCV

```
pip install --upgrade tensorflow
pip install Flask
pip install opencv-python
```

### Installing

Please follow the following steps to set up your development environment.

Set up your virtual environment 

```
pip install virtualenv
python3 -m venv env
source env/bin/activate
env/Scripts/activate (Windows)

```

Run the app

```
python app/run.py
```


## Deployment

#####Deploy the the dockerized app to heroku
Appropriate files are given.
* Dockerfile 
* heroku.yml

## Built With

* [Flask](https://palletsprojects.com/p/flask/) - The web framework used
* [OpenCV](https://opencv.org/) - Image Processing tool

## Authors

* **Sudipto Baral** - *Initial work* - [sudiptob2](https://github.com/sudiptob2)

See also the list of [contributors](https://github.com/sudiptob2/agrgb-rest/contributors.txt) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone whose code was used
* Department of EEE Patuakhali Science and Technology University


