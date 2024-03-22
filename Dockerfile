FROM python:3.11.2-alpine

# python app
ADD main.py .
ADD ipdata.py .
ADD middleware.py .

# database and extension
ADD bin/inet.so bin/inet.so
ADD ips.db .

# install python reqs
RUN pip3 install falcon python-dotenv

EXPOSE 8123

# run the app
CMD ["python3", "./main.py"]