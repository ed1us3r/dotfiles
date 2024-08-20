import os
import socket
from ..utils import BasicSegment


class Segment(BasicSegment):
    def add_to_powerline(self):
        env = os.getenv('POWERLINE_VIRTUAL_ENV_NAME') \
            or os.getenv('CONTAINER-ENV') \
            or os.getenv('container-env')
        if os.getenv('POWERLINE_VIRTUAL_ENV_NAME') \
            and socket.gethostname() == 'toolbox':
            env = socket.gethostname() 
        if not env:
            return
        env_name = "toolbox:" + env
        bg = self.powerline.theme.TOOLBOX_BG
        fg = self.powerline.theme.TOOLBOX_FG
        self.powerline.append(" " + env_name + " ", fg, bg)