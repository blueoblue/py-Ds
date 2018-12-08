'''
 SourceName > Stack.py
 Describe   > 单链表实现栈
 Version    > 1.0
 Time       > 2018-12-08 21:12:18
'''

from ..LinkedList.Unorder_linkedlist import (
	LinkedlistEmptyError as EmptyError,
	UnorderLinkedlist as ull)

class Stack(object):
	def __init__(self):
		self._stack=ull()
	def size(self):
		return self._stack.length
	def isempty(self):
		return self._stack.isempty()
	def top(self):
		if self.isempty():
			raise EmptyError('Stack is empty.')
		return self._stack.head.data
	def pop(self):
		return self._stack.pop()
	def push(self,data):
		self._stack.addhead(data)
	def getall(self):
		return self._stack.getall()

if __name__=="__main__":
	sk=Stack()