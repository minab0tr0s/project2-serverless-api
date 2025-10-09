# Project 2: Fully Serverless To-Do List API

## 🚀 Description

This project demonstrates the creation of a cost-effective, highly scalable, and fully serverless REST API for a simple to-do list application. The entire backend is built on AWS using the Serverless Framework for infrastructure definition and deployment.

The architecture is event-driven and follows a "pay-per-use" model, meaning it incurs no costs when idle. This project showcases the ability to build and deploy modern, cloud-native applications without managing any servers.

***

## 🏛️ Architecture Diagram

The architecture is simple and powerful. An **API Gateway** provides the public HTTP endpoints. Each endpoint is connected to a specific **AWS Lambda** function that contains the business logic. The Lambda functions then interact with a **DynamoDB** table to store and retrieve data.



***

## 🛠️ Technologies Used

* **Framework:** Serverless Framework
* **Cloud Provider:** AWS (Amazon Web Services)
* **Programming Language:** Python

### ### Key AWS Services:

* **AWS Lambda:** Provides the serverless compute for our business logic (Create, Read, Update, Delete).
* **Amazon API Gateway:** Creates and manages the RESTful API endpoints that trigger our Lambda functions.
* **Amazon DynamoDB:** A fully managed, serverless NoSQL database for storing the to-do items.
* **IAM Roles:** Manages the permissions for Lambda functions to access DynamoDB.

***

## 🌐 API Endpoints

The API provides the following endpoints for managing to-do items:

| Method | Path              | Description                 |
| :----- | :---------------- | :-------------------------- |
| `POST` | `/todos`          | Create a new to-do item.    |
| `GET`  | `/todos`          | Retrieve all to-do items.   |
| `GET`  | `/todos/{id}`     | Retrieve a single to-do item. |
| `PUT`  | `/todos/{id}`     | Update an existing to-do item.|
| `DELETE`| `/todos/{id}`     | Delete a to-do item.        |

***

## ⚙️ Setup and Deployment

### ### Prerequisites:

* An AWS Account
* Serverless Framework installed
* AWS CLI installed and configured

### ### Deployment Steps:

1.  **Clone the repository:**
    ```bash
    # Replace [YOUR_GITHUB_USERNAME] with your actual username
    git clone [https://github.com/](https://github.com/)[YOUR_GITHUB_USERNAME]/project2-serverless-api.git
    cd project2-serverless-api
    ```

2.  **Deploy the service:**
    This single command deploys the entire stack (API Gateway, Lambda, DynamoDB) to your AWS account.
    ```bash
    serverless deploy
    ```

***

## 🧪 Usage & Testing

After deployment, you can test the live endpoints using `curl` or any API client.

**Example: Create a new to-do item**
```bash
# Replace [API_ENDPOINT_URL] with the URL from the deploy output
curl -X POST -H "Content-Type: application/json" -d '{"todo": "Learn Serverless Framework"}' [API_ENDPOINT_URL]/todos
```

### Cleanup

To avoid ongoing charges, you can remove the entire service from your AWS account with one command.
```bash
serverless remove
```
