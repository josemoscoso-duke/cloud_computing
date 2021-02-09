# Weatherapp using Flask-App-on-GCP
This project is an implementation of the  continuous delivery framework based on the guidelines of the Cloud computing at scale class @ Duke University.

## Overview
I use the [openweathermap](https://openweathermap.org/) API. This application uses Flask in python for interacting with the openweathermap API. By indicating the city of interest as an input, the app makes a call to Openweathermap using the api and the request library, and returns weather conditions on real time at the city  (temperature, wind speed and cloud conditions). The output of the Openweathermap is then sent over via flask on a html web page.

For the purpose of continuous delivery, Cloud Build on Google Cloud Platform (GCP) is used. The deployment is triggered whenever a push is made on the repository.

## Prerequisites

The only prerequisite for this project is the **openweathermap api key**, which is required to initialize communication of this application with openweathermap.

Once the **openweathermap api key** is obtained, this value should be stored in the weather.ini file.

## Description of required files

> main.py : The main python file with the application code.   
> requirements.txt : List of packages needs to be installed during app deployment.   
> app.yaml : Contains environment configuration.   
> Makefile : File containing shell commands to execute requirements.txt and other configurations.     
> config_weather : function to parse the weather.ini file that contains the openweathermap api key.
> cloudbuild.yaml : commandas for continuous integration in gcp, triggered by git pushes.
