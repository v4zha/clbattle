
FROM ubuntu:latest

LABEL "author"="v4zha"

ARG LVL=lvl8

RUN apt update && apt install  openssh-server sudo vim nano man -y

RUN useradd -rm -d /home/$LVL -s /bin/bash -g root $LVL &&\
    echo "$LVL:p4rzm_p0r1" | chpasswd

COPY  ./scripts /home/$LVL/.config/scripts

COPY  ./help.txt /home/$LVL/

COPY ./required.txt /$LVL/required.txt

RUN useradd -rm -d /home/gopan -s /bin/bash -g root gopan &&\
    chown -R  /home/$LVL/* $LVL &&\
    echo "gopan:agentX" | chpasswd &&\
    echo -e "============\null1_v4da\n============\n" > /home/gopan/rahasyam &&\
    echo -e "thaka thaka..thalayude_vilayattu..\n [agentX]\n" > /home/$LVL/.thaka_thaka.txt &&\
    chmod -R 505 /home/$LVL/.config/scripts &&\
    chmod -R 505 /home/$LVL/help.txt &&\
    chmod -R 505 /home/gopan/rahasyam &&\
    chmod -R 505 /home/$LVL/.thaka_thaka.txt &&\
    service ssh start &&\
    echo "alias start='python3 /home/$LVL/.config/scripts/task.py' " >> /home/$LVL/.bashrc &&\
    echo "export ASSET_DIR='/home/$LVL/.config/scripts/assets/'" >> /home/$LVL/.bashrc &&\
    echo "alias help='clear && cat /home/$LVL/help.txt'" >> /home/$LVL/.bashrc &&\
    echo "python3 /clean.py && clear && cat /home/$LVL/.config/scripts/assets/intro.txt" >> /home/$LVL/.bashrc 

EXPOSE 22

CMD ["/usr/sbin/sshd","-D"]

