# GitHub Actions with Azure Container Registry and Azure Container Instances
This demo shows how to build a Docker container from a Python Flask app, push it to an Azure Container Registry, and then run the container on an Azure Container Instance. The app itself is simple but unimportant -- replace with any other app and the constructs of the GitHub action should remain the same.

## Pre-requisites
- An Azure Subscription
- A resource group called "Demo"
- An Azure Container Repository resource created in the Demo resource group
- Enable the Admin User Login/Password in the Azure Container Registry
![Screenshot](https://github.com/marlinspike/flask-container-action/blob/master/img/acr_enable_admin_user.png)


## Step 1: Create a simple Flask app
Clone the repository and you've got it. Install dependencies with the requirements.txt file

## Step 2: Create a Dockerfile
The Dockerfile supplied will work for any Flask app on Ubuntu

## Step 3: Build a Docker image
This is optional, but a useful step on a Developer machine, to verify that your Docker image will build properly.

`docker build -t flask-container-action:latest .`

Here, the image is called **flask-container-action**, and it's tagged as **latest**.

## Step 4: Run the container
This is optional, but a useful step on a Developer machine, to verify that your Docker image will run properly.

`Docker run -p 80:80 flask-container-action`

Here, the local port 80 is mapped to a container port 80.

## Step 5: Create a Service Principal in Azure for your GitHub Action to use
You can do this on your own machine if you have Azure CLI installed, or simply in the portal from the Cloud Shell (Bash).

`az ad sp create-for-rbac --name "rc-az-action" --sdk-auth --role contributor --scopes /subscriptions/xxx-xxx-xxx-xxx-xxx/resourceGroups/Demo`

Here, the **create-for-rbac** command is used to create a Service Principal called rc-az-action, and it's granted **contributor** rights on the scope of the **Demo** Resource Group in the subscription specified. Replace the "xxx.." with your actual subscription id.

Copy the resulting JSON response, and save it in a GitHub secret in your repository, as shown below:

![JSON Response](https://github.com/marlinspike/flask-container-action/blob/master/img/JSON_Response.png)

![GitHub Secret](https://github.com/marlinspike/flask-container-action/blob/master/img/create_secret.jpg)

The **Demo** Resource Group is where I've created the Azure Container Repository.

## Step 6: Create GitHub Secrets
GitHub Secrets to create:
- "AZ_CREDS": JSON Response from step Above
- "REGISTRY_PASSWORD": The Password for the Azure Container Registry
- "REGISTRY_USERNAME": The Username for the Azure Container Registry

## Step 7: Create the GitHub Action YAML Script
The script supplied in the workflows folder should work if you've followed the directions accurately.