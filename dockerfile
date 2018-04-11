from debian:latest
RUN apt-get update
RUN apt-get -y install vim python-pip tmux locales
RUN pip install pytest
RUN echo "en_US.UTF-8 UTF-8" > /etc/locale.gen && locale-gen
COPY map/tmux.conf /etc/tmux.conf
WORKDIR /root/project
