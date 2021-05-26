# -*- coding: utf-8 -*-
import os
import sys

_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, _path)

import json
import socket

from computer_networks.processor.net.parser import IPParser
from operate_system.pool import ThreadPool as tp
from operate_system.task import AsyncTask


class ProcessTask(AsyncTask):
    def __init__(self, packet, *args, **kwargs):
        self.packet = packet
        super().__init__(func=self.process, *args, **kwargs)

    def process(self):
        ip_header = IPParser.parse(self.packet)
        return ip_header


class Server(object):
    def __init__(self):
        # 工作协议类型、套接字类型、工作具体的协议
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP)
        # 自己的主机ip
        self.ip = "172.19.6.43"
        self.port = 8888
        self.sock.bind((self.ip, self.port))

        # 混杂模式
        self.sock.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)

        self.pool = tp(10)
        self.pool.start()

    def loop_serve(self):
        while True:
            # 1. 接收
            packet, addr = self.sock.recvfrom(65535)
            # 2. 生成Task
            task = ProcessTask(packet)
            # 3. 提交
            self.pool.put(task)
            # 4. 获取结果
            result = task.get_result()
            result = json.dumps(
                result,
                indent=4
            )
            print(result)


if __name__ == '__main__':
    server = Server()
    server.loop_serve()
