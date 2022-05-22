
FROM ubuntu:latest

LABEL "author"="v4zha"

ARG LVL=lvl3

RUN apt update && apt install  openssh-server sudo vim nano -y

RUN useradd -rm -d /home/$LVL -s /bin/bash -g root $LVL &&\
    echo "$LVL:k4rukaVay4l_kuruv1" | chpasswd

COPY  ./scripts /home/$LVL/.config/scripts

COPY  ./help.txt /home/$LVL/

COPY ./file_gen.py /home/$LVL/file_gen.py

RUN python3 /home/$LVL/file_gen.py &&\
    rm /home/$LVL/file_gen.py &&\
    chmod -R 555 /home/$LVL/.config/scripts &&\
    chmod -R 555 /home/$LVL/help.txt &&\
    chmod 555 /home/$LVL/spell-book.txt &&\
    service ssh start &&\
    echo "alias start='python3 /home/$LVL/.config/scripts/task.py' " >> /home/$LVL/.bashrc &&\
    echo "export ASSET_DIR='/home/$LVL/.config/scripts/assets/'" >> /home/$LVL/.bashrc &&\
    echo "alias help='clear && cat /home/$LVL/help.txt'" >> /home/$LVL/.bashrc &&\
    echo "clear && cat /home/$LVL/.config/scripts/assets/intro.txt" >> /home/$LVL/.bashrc 

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]
