'''
 SourceName > Loop_linklist.py
 Describe   > 循环单链表
 Version    > 0.1
'''
from Unorder_linkedlist import *

class LoopLinkedlist(UnorderLinkedlist):
	def __init__(self):
		super().__init__()
		self._tail=None
	def addhead(self,data):
		node=Node(data)
		if not self._head:
			node.next=node
			self._head=self._tail=node
		else:
			node.next=self._head
			self._head=node
			self._tail.next=self._head
		self._length+=1
		return self._length
	def addtail(self,data):
		if not self._head:
			self.addhead(data)
		else:
			node=Node(data)
			self._tail.next=node
			self._tail=node
			self._tail.next=self._head
			self._length+=1
		return self._length
	def insert(self,data,position):
		if not self._head:
			raise LinkedlistEmptyError('Linkedlist is empty !')
		elif not position or position>=self._length or self._length==1:
			raise IndexError('Cannot insert data')
		else:
			index=0
			previous=self._head
			while index!=position-1:
				index+=1
				previous=previous.next

			node=Node(data)
			node.next=previous.next
			previous.next=node
			self._length+=1
			return self._length
	def pop(self,position=0):
		if not self._head:
			raise LinkedlistEmptyError()
		elif position>=self._length:
			raise IndexError('Cannot delete data')
		elif not position:
			rubbish=self._head.data
			if self._length>1:
				self._head=self._head.next
			else:
				self._head=None
			self._tail=self._head
		else:
			index=0
			previous=self._head
			while index!=position-1:
				index+=1
				previous=previous.next

			rubbish=previous.next.data
			previous.next=previous.next.next
			if self._length-position==1:
				self._tail=previous
		self._length-=1
		return rubbish
	def delete(self):
		if not self._head:
			raise LinkedlistEmptyError()
		else:
			self._head=self._tail=None
			self._length=0
		return self._length
	def getall(self):
		count=1
		current=self._head
		while count<=self._length:
			count+=1
			yield current.data
			current=current.next

if __name__ == '__main__':
	lll=LoopLinkedlist()