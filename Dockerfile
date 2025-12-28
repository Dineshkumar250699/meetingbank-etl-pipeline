# Start from the base Airflow image version 2.7.3-python3.9
FROM apache/airflow:2.7.3-python3.9

# 1. Install System Dependencies (as root)
# Switch to root to run system commands, required for packages like psycopg2-binary
USER root

# Install build tools (build-essential) and postgres client libraries (libpq-dev)
# This prevents compilation errors for certain Python packages during pip install.
RUN apt-get update -qq \ 
    && apt-get install -y --no-install-recommends \
       build-essential \
       libpq-dev  \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 2. Install Python Dependencies (as airflow user)
# Switch back to the non-root 'airflow' user for security and best practice
USER airflow

# Copy your requirements.txt file into the image build context
COPY requirements.txt /requirements.txt

# Install dependencies using pip
# --user ensures packages are installed to a location the 'airflow' user can access
RUN pip install --no-cache-dir --user -r /requirements.txt