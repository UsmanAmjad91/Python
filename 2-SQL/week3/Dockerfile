# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the working directory
COPY requirements.txt requirements.txt

# Install the Python dependencies
# The --no-cache-dir flag reduces the size of the image
# We're installing `alembic` and `psycopg2-binary`
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code from the current directory
# on your host machine to the /app directory inside the container
COPY . .

# Define the command to run when the container starts
# We now use the full path to the 'alembic' executable to ensure it's found
# The path is typically /usr/local/bin/alembic in a Python container
CMD ["/usr/local/bin/alembic", "upgrade", "head"]
