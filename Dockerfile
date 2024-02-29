FROM python:3.12

# Set environment variables and working directory
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /app

# Install pipx and pipenv
RUN python -m pip install --user pipx && \
    python -m pipx ensurepath

# Install Django and other project dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your project files
COPY . .

# Create a system user and group for running the application
RUN addgroup --system django \
  && adduser --system --ingroup django django

# Change ownership of the application directory to the django user
RUN chown -R django:django /app

# Grant execute permission to entrypoint.sh
RUN chmod +x entrypoint.sh

# Switch to the django user
USER django

EXPOSE 8000

# Set the entrypoint script
ENTRYPOINT [ "./entrypoint.sh" ]
