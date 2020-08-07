  FROM python
  LABEL maintainer="Abhishek Shetty aushetty@in.ibm.com"
  RUN apt-get  -y update  && apt-get install -y
  RUN apt-get -y upgrade 

  WORKDIR /app

  COPY . /app

  RUN pip install -r requirements.txt

  EXPOSE 5000

  CMD ["python" , "app.py"]