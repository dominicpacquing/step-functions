
#### Setup

1. (Optional) Install `python-3.9`. Easier way to manager python version is to use [pyenv](https://github.com/pyenv/pyenv)

         pyenv install 3.9

2. (Optional) Create and activate virtualenv

         python3 -m venv venv (only done once)
         source venv/bin/activate

3. Install [pip-tools](https://github.com/jazzband/pip-tools)

         pip install pip-tools

4. Install aws packages

        pip install -r requirements.txt


#### Build and deploy

Simple demo that utilises AWS EventBridge to trigger AWS Step Functions workflow


1. Build the application

         sam build

2. Deploy the application
   
   2.1 (Optional) Create a bucket that is going to be used to store the artifacts such as sam template.

          AWS_PROFILE=xxxxxx sam deploy \ 
               --stack-name droid-sfn \
               --s3-bucket [bucket-for-artifact] \
               --capabilities CAPABILITY_IAM


#### Architecture
![Workflow](https://github.com/dominicpacquing/step-functions/raw/master/common/images/step-functions.png "Workflow")
