FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /m_y_shopping
WORKDIR /m_y_shopping
#COPY requirements.txt /code/
COPY . /m_y_shopping
RUN pip install -r requirements.txt
#COPY . /m_y_shopping
