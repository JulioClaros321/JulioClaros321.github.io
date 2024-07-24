# Use the official AWS Lambda Python 3.9 base image
FROM public.ecr.aws/lambda/python:3.10

# Set the working directory
WORKDIR /var/task

# Copy the requirements file
COPY requirements.txt ./

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the function code
COPY app.py ./

# Command to run the Lambda function handler
CMD ["app.lambda_handler"]
