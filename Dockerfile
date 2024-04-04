FROM python:3.11.5

WORKDIR /

# Copy main.py
COPY ./main.py ./


RUN pip install flask==3.0.0
RUN pip install Flask==3.0.0
RUN pip install Flask-Cors
RUN pip install gunicorn
RUN pip install Flask-Bcrypt
RUN pip install mysqlclient
RUN pip install Flask-SQLAlchemy==3.0.0
RUN pip install SQLAlchemy==1.4.31
# Clean up unnecessary files
RUN apt-get purge -y build-essential \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Copy the rest of the files
COPY . .

# Expose the specified port
EXPOSE 5000

# Specify the command to run on container start
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"]