import os
import socket
from powerline_shell.utils import BasicSegment


class Segment(BasicSegment):
    def add_to_powerline(self):
        env = os.getenv('TOOLBOX_NAME') \
            or os.getenv('toolbox_name') \
            or os.getenv('HOSTNAME')
        if os.getenv('CONTAINER_ENV') or os.getenv('container_env'):
            env = os.getenv('IMAGE_NAME') or os.getenv('image_name')
        if not os.getenv('TOOLBOX_PATH'):
            return
        if socket.gethostname() != 'toolbox':
            return
        if not env:
            return
        env_name = "  toolbox::" + env + " "
        bg = self.powerline.theme.TOOLBOX_BG
        fg = self.powerline.theme.TOOLBOX_FG
        self.powerline.append(env_name, fg, bg)
