import os
import socket
from powerline_shell.utils import BasicSegment


class Segment(BasicSegment):
    def add_to_powerline(self):
        env = os.getenv('TOOLBOX_NAME') \
            or os.getenv('CONTAINER_ENV') \
            or os.getenv('container_env')
        if os.getenv('TOOLBOX_NAME') \
            and socket.gethostname() == 'toolbox':
            env = socket.gethostname() 
        if not env:
            return
        env_name = "toolbox:" + env
        bg = self.powerline.theme.HOSTNAME_BG
        fg = self.powerline.theme.HOSTNAME_FG
        self.powerline.append(" " + env_name + " ", fg, bg)
