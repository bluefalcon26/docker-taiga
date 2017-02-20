FROM ubuntu:16.04
MAINTAINER Daniel Prejean "daprejean@gmail.com"

RUN apt-get update && \
	apt-get install -y \
	build-essential binutils-doc autoconf flex bison libjpeg-dev \
	libfreetype6-dev zlib1g-dev libzmq3-dev libgdbm-dev libncurses5-dev \
	automake libtool libffi-dev curl git tmux gettext \
	postgresql-9.5 postgresql-contrib-9.5 \
	postgresql-doc-9.5 postgresql-server-dev-9.5 \
	python3 python3-pip python-dev python3-dev python-pip virtualenvwrapper \
	libxml2-dev libxslt-dev

# RUN useradd -ms /bin/bash taiga doesn't work with static volumes, need root

# RUN mkdir -p /home/taiga/media && chown taiga:taiga /home/taiga/media
# RUN mkdir -p /home/taiga/static && chown taiga:taiga /home/taiga/static
# VOLUME /home/taiga/media
# VOLUME /home/taiga/static

# USER taiga
RUN mkdir -p /home/taiga
WORKDIR /home/taiga

RUN git clone https://github.com/taigaio/taiga-back.git taiga-back && \
	cd taiga-back && \
	git checkout stable

WORKDIR /home/taiga/taiga-back

RUN bash -c "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh \
	&& mkvirtualenv -p /usr/bin/python3.5 taiga \
	&& pip install -r requirements.txt"

COPY local.py settings/local.py

CMD bash -c "source /usr/share/virtualenvwrapper/virtualenvwrapper.sh \
        && workon taiga \
        && python manage.py runserver '0.0.0.0:8000'"

