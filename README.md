
#Customer Classification System

This code classifies customers into two categories: "Yes" and "No", based on their rating and salary. The input parameters are the number of clusters (k), the rating of the customer, and the salary of the customer. The code first calculates the distance between the customer and each of the data points in the dataset. The data points are then ranked in ascending order of distance, and the top k data points are used to classify the customer. If the majority of the top k data points are "Yes", then the customer is classified as "Yes". Otherwise, the customer is classified as "No".
The code also includes a function called plotter(), which plots the data points in the dataset and the input customer. This function can be used to visualize the customer classification process.
To run the code, you will need to install the following Python libraries:
    • math
    • pandas
    • matplotlib
Once you have installed the required libraries, you can run the code by executing the following command:
The code will first ask you to enter the value of k, the rating of the customer, and the salary of the customer. Once you have entered these values, the code will classify the customer and print the classification result. The code will also plot the data points in the dataset and the input customer.


