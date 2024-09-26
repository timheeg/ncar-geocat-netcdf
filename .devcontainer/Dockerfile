ARG BASE_IMAGE_NAME="repo.nextgenfed.com/ng-docker/navair-jse/ubi9"
ARG BASE_IMAGE_TAG="9.4"
FROM $BASE_IMAGE_NAME:$BASE_IMAGE_TAG

# Install tools
#
# git obviously
# sudo for non-root user sudo support
# vim-enhanced for vi/vim and color vi support in git
#
RUN dnf update -y \
  && dnf -y install \
  git \
  sudo \
  vim-enhanced \
  && dnf clean all \
  && rm -rf /var/cache/yum

# 🐍⭕ Install Miniconda
#
# Per instructions here https://docs.anaconda.com/miniconda/
#
WORKDIR /opt/miniconda3
RUN curl --fail -LO https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
  && bash Miniconda3-latest-Linux-x86_64.sh -b -u -p . \
  && rm Miniconda3-latest-Linux-x86_64.sh

# Install root user .bashrc
COPY .bashrc /root/

# 🧑‍💻 Create the developer (non-root) user
ARG USERNAME
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# Create the user and group
#
# Note, most of our usernames use the `first.last` template. Having a `.` in a
# username is POSIX compliant (good). However, `sudoers.d` ignores any file
# containing a `.` as a way to disable changes; so files named `first.last` are
# simply ignored. Instead, use the `USER_UID` as the file name.
# See https://superuser.com/a/869145
#
RUN groupadd --gid $USER_GID $USERNAME \
  && useradd -s /bin/bash --uid $USER_UID --gid $USER_GID -m $USERNAME \
  && echo $USERNAME ALL=\(ALL\) NOPASSWD: ALL > /etc/sudoers.d/$USER_UID \
  && chmod 0440 /etc/sudoers.d/$USER_UID

# Install the .bashrc for the user
COPY .bashrc /home/$USERNAME
RUN chown $USER_UID:$USERNAME "/home/$USERNAME/.bashrc" \
  && chmod 644 "/home/$USERNAME/.bashrc"

# 🌊 Setup the container environment

# Add conda to path
ENV CONDA_HOME=/opt/miniconda3
ENV PATH="$CONDA_HOME/bin:$PATH"

# Create geocat conda environment
RUN conda create -n geocat -c conda-forge -y geocat-comp geocat-viz

# 🧑‍💻 Change to non-root user
USER $USERNAME

CMD [ "bash" ]
