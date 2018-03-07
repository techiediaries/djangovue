# Django Vue and Auth0

This repository contains code for the first and second part of a demo application built using Django, Django REST framework and Vue.js

* The master branch contains the initial app with separate django and vue apps

* The part2 branch contains the code for the app after integrating both the Django and Vue apps (the frontend will be served from Django) 

For the final and complete demo you need to check this [repo](https://github.com/techiediaries/django-auth0-vue)

This repo accompanies a [tutorial series](https://www.techiediaries.com/django-vuejs-auth0) where you can learn:

* how to integrate Vue with Django so you can serve the front end application using Django instead of having complete separate front end and back end apps
* how to fix Hot Code Reloading when using Django to serve the Vue application
* how to add JWT authentication via Auth0
* how to update the Callback URL for Auth0 authentication

* Building the REST API: You will create a simple REST API around one model (*Product*) with DRF and learn how to add pagination to your APIs. 
* Creating the Service to Consume the API: You will create the class that interfaces with your API using Axios.   
