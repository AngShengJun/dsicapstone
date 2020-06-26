# Part 5: Deployment

## Overview

This section documents the general steps for model deployment. 

After the hustle and bustle of Data cleaning, EDA, Model building, evaluation and tuning, we are in the home stretch of model deployment! Model deployment can be an exciting venture :rocket: and a hairy business at the same time, especially for novice coders like myself. The content below outlines some of the discoveries along my learning journey. Hopefully it will help explain what is needed to get a model up and running, and serve as a guide to those seeking to deploy models. Follow along and tailor the code to suit your own project needs.

---

## What is Needed Upfront

1. Install `Git` (if you haven't; chances are you have it installed by now)
2. Install `Heroku Command Line Interface`
3. Set up a `Heroku` account
4. html page (design can take significant time, so one may like to do this upfront first), name it `index.html`

___

Plan ahead how you want the deployed model to operate. For my capstone, the classifier model takes in a list of cleaned text, with custom stopwords removed. Therefore, I had to pickle the count vectorizer, custom stopwords, and model. In Jupyter.

```python
import pickle
# save model to disk 
filename1 = 'finalized_model.sav'
pickle.dump(model_lr2, open(filename1, 'wb'))
filename2 = 'finalized_cv.sav'
pickle.dump(cv2, open(filename2, 'wb'))
filename3 = 'finalized_stopwords.sav'
pickle.dump(s_words2, open(filename3, 'wb'))
```

___

## Set Up Virtual Environment

To host your application (model that you want to deploy), you will need `flask` and `virtualenv` as well. Install them using Anaconda Navigator or Anaconda prompt. Then setup a project directory space for hosting. In my case, I already had the master directory for holding various projects, so the codes is slightly different. In Anaconda Prompt 

```
cd virtualenvs
virtualenv capstone
# activate env from Scripts folder
cd Scripts
activate.bat
# to deactivate
deactivate.bat
```

Install gunicorn (for Heroku), freeze the python modules for your environment like so:

```
pip install gunicorn
pip freeze >> requirements.txt
```

I updated the modules within manually to trim the packages down (will affect deployment times downstream). Please refer to the `requirements.txt` file for details.

Create a `nltk.txt` file, populate it with the nltk modules used. This is for `heroku-python nltk` use.

---

## Flask script

Create a folder `templates`, this will hold the html form. Move the  `index.html` into this folder.  

```
mkdir templates
```

Copy the pickle files into the root directory of the project virtualenv folder (i.e. capstone).

## Python Script

Create python scripts in the capstone level of directory. These scripts are dependent on one's own model and functional flow. Refer to `Requiredfn.py` and `service.py` for more details. Note `service.py` is where I hold the application (model). This information is important for `Heroku` later on. 

---

## Local Prototyping

Run service. In Anaconda Prompt, enter the following sequentially. An url should display where I can access the webpage and tune the webpage as needed real-time. 

```
SET FLASK_APP=service.py
SET FLASK_DEBUG=1
flask run
```

___

## Heroku

Create a `Procfile` in root Project folder directory, note no extensions.  **Procfile only needs one line**. Filename is the name of the python script that contains the flask application with flask name app. 

```
# Within Procfile
web: gunicorn <filename>:<main method name>
# filename refers to the python script containing flask application with flask name app
# app = Flask(__name__)
# In this instance the line is
web: gunicorn service:app
```

Log in to `Heroku`, create app and deploy like so using Anaconda Prompt

```
heroku login
heroku create
# two url returned will be returned, the latter is the Heroku git remote repo where the application lives # on Heroku. The former is the web url where the application will be once deployed.
git add .
git commit -m"message"
git push heroku master
# Ensure at least one instance of application is running
heroku ps:scale web=1
# Say hello to your application!
heroku open
```



​																																									[Back to overview](https://github.com/AngShengJun/dsicapstone)

---

References:

[Overall steps](https://towardsdatascience.com/designing-a-machine-learning-model-and-deploying-it-using-flask-on-heroku-9558ce6bde7b) , [Pickle](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/) , [Html template starter1](https://github.com/ritvikkhanna09/Income-Prediction-Webapp/blob/master/WebApp/flaskr/templates/index.html) , [Html template starter2](https://www.w3schools.com/html/html_layout.asp) , [Heroku guide1](https://devcenter.heroku.com/articles/getting-started-with-python?singlepage=true) , [Heroku guide2](https://heartbeat.fritz.ai/guide-to-saving-hosting-your-first-machine-learning-model-cdf69729e85d) , [Heroku guide3](https://medium.com/the-andela-way/deploying-a-python-flask-app-to-heroku-41250bda27d0)