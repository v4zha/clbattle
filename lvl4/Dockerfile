
FROM ubuntu:latest

LABEL "author"="v4zha"

ARG LVL=lvl4

RUN apt update && apt install  openssh-server sudo vim nano man -y

RUN useradd -rm -d /home/$LVL -s /bin/bash -g root $LVL &&\
echo "$LVL:ambala_pr4vu" | chpasswd

COPY  ./scripts /home/$LVL/.config/scripts

COPY  ./help.txt /home/$LVL/

COPY ./task.sh /home/$LVL/task.sh

COPY ./required.txt /$LVL/required.txt

RUN chmod +x /home/$LVL/task.sh &&\
    /home/$LVL/task.sh &&\
    rm /home/$LVL/task.sh &&\
    chown -R  /home/$LVL/* $LVL &&\
    chmod -R 505 /home/$LVL/.config/scripts &&\
    chmod -R 505 /home/$LVL/help.txt &&\
    service ssh start &&\
    echo "alias start='python3 /home/$LVL/.config/scripts/task.py' " >> /home/$LVL/.bashrc &&\
    echo "export ASSET_DIR='/home/$LVL/.config/scripts/assets/'" >> /home/$LVL/.bashrc &&\
    echo "alias help='clear && cat /home/$LVL/help.txt'" >> /home/$LVL/.bashrc &&\
    echo "python3 /clean.py && touch /home/$LVL/rahasyam && rm /home/$LVL/rahasyam && clear && cat /home/$LVL/.config/scripts/assets/intro.txt" >> /home/$LVL/.bashrc 

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]

