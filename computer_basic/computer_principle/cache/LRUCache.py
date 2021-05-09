# coding=utf-8

from computer_basic.computer_principle.DoubleLinkedList import DoubleLinkList, Node


class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.list = DoubleLinkList(self.capacity)

    def get(self, key):
        if key not in self.map:
            return -1
        node = self.map.get(key)
        self.list.remove(node)
        self.list.append_front(node)
        return node.value

    def put(self, key, value):
        if key in self.map:
            node = self.map.get(key)
            self.list.remove(node)
            node.value = value
            self.list.append_front(node)
        else:
            node = Node(key, value)
            if self.list.size >= self.list.capacity:
                old_node = self.list.remove()
                self.map.pop(old_node.key)
            self.list.append_front(node)
            self.map[key] = node

    def print(self):
        self.list.print()
