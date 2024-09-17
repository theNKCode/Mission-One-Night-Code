# Use an official Ubuntu as a parent image
FROM ubuntu:20.04

# Set environment variables to prevent user prompts during installation
ENV DEBIAN_FRONTEND=noninteractive

# Update the package repository and install VLC
RUN apt-get update && \
    apt-get install -y vlc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install additional dependencies for audio playback
RUN apt-get update && \
    apt-get install -y \
    pulseaudio \
    alsa-utils && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set up PulseAudio
RUN useradd -ms /bin/bash vlcuser

# Add entrypoint script and change permissions
COPY entrypoint.sh /home/vlcuser/entrypoint.sh
RUN chmod +x /home/vlcuser/entrypoint.sh

# Change to the non-root user
USER vlcuser
WORKDIR /home/vlcuser

# Set the entrypoint
ENTRYPOINT ["/home/vlcuser/entrypoint.sh"]

