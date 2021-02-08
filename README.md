# Weatherapp using Flask-App-on-GCP
This project is an implementation of the  continuous delivery framework based on the guidelines of the Cloud computing at scale class @ Duke University. 

## Overview
I use an API of the Openweathermap [openweathermap](https://openweathermap.org/). This application uses Flask in python for interacting with the openweathermap API. By indicating the city of interest as an input, the app makes a call to Openweathermap using the api and the request library, and returns weather conditions on real time at the city  (temperature, wind speed and cloud conditions). The output of the Openweathermap is then sent over via flask on a html web page.

For the purpose of continous delivery, Cloud Build on Google Cloud Platform (GCP) is used. The deployment is trigerred whenver a push is made on the the repository. 

