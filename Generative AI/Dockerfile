## Use the official Python 3.9 image
FROM python:3.9

## Set the working directory in the container
WORKDIR /code

## Copy the dependencies file and working directory to container at /code
COPY ./requirements.txt /code/requirements.txt

##Install the requirements .txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

## Set up a new user
RUN useradd user
## Switch to this new user
USER user

## Set home to user's home directory
ENV HOME=/home/user \
    PATH=$HOME.local/bin:$PATH

## set working directory to user's home directory
WORKDIR $HOME/app

## Copy the current directory contents into the container at /app
COPY --chown=user . $HOME/app

## Start FASTAPI App on aapla port 6789
EXPOSE 7860
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]