'''
 > SourceName : Doubly_linklist.py
 > Describe   : 双向链表
 > Version    : 0.1
'''
from Unorder_linkedlist import *
class DiubleNode(Node):
	def __init__(self,data):
		super().__init__(data)
		self._previous=None
	@property
	def previous(self):
		return self._previous
	@previous.setter
	def previous(self,node):
		self._previous=node
class DoubleLinkedlist(UnorderLinkedlist):
	def addhead(self,data):
		node=Node(data)
		if not self._head:
			self._head=node
		else:
			node.next=self._head
			self._head.previous=node
			self._head=node
		self._length+=1
		return self._length
	def addtail(self,data):
		if not self._head:
			self.addhead(data)
		else:
			number=1
			current=self._head
			while number!=self._length:
				number+=1
				current=current.next
			node=Node(data)
			node.previous=current
			current.next=node
			self._length+=1
		return self._length
	def insert(self,data,position):
		if not self._head:
			raise LinkedlistEmptyError()
		elif not position or position>=self._length:
			raise IndexError('Cannot insert data')
		else:
			index=0
			current=self._head
			node=Node(data)
			while index!=position:
				index+=1
				current=current.next
			node.next=current
			node.previous=current.previous
			current.previous.next=node
			current.previous=node
			self._length+=1
			return self._length
	def pop(self,position=0):
		if not self._head:
			raise LinkedlistEmptyError()
		elif position>=self._length:
			raise IndexError('index is too large')
		else:
			rubbish=None
			if not position:
				rubbish=self._head.data
				self._head.next.previous=None
				self._head=self._head.next
			else:
				index=0
				current=self._head
				if position==-1:
					position=self._length-1
				while index!=position:
					index+=1
					current=current.next

				if index==self._length-1:
					current.previous.next=None
				else:
					current.previous.next=current.next
				rubbish=current.data
			self._length-=1
			return rubbish
if __name__=='__main__':
	dl=DoubleLinkedlist()