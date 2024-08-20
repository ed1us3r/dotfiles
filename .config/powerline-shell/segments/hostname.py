import os
import socket
from powerline_shell.utils import BasicSegment


class Segment(BasicSegment):
    def add_to_powerline(self):
        env = os.getenv('HOSTNAME') \
            or os.getenv('hostname') \
            or os.getenv('host')
        if os.getenv('HOSTNAME') \
            and socket.gethostname() != 'toolbox':
            env = socket.gethostname()
        if os.getenv('HOSTNAME') \
            and socket.gethostname() == 'toolbox':
            env = '' 
        if not env:
            return
        env_name = env 
        bg = self.powerline.theme.HOSTNAME_BG
        fg = self.powerline.theme.HOSTNAME_FG
        self.powerline.append(" " + env_name + " ", fg, bg)