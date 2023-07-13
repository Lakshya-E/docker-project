FROM python

ENV PYTHONUNBUFFERED=1

RUN apt-get update -qq && apt-get install -y build-essential
RUN apt-get -y install sudo
# for postgres
RUN apt-get install -y libpq-dev
RUN apt-get -y install --no-install-recommends postgresql-client

WORKDIR /shop

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

# CMD ["python", "manage.py", "runserver"]
