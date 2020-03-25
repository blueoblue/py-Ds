'''
 > SourceName : Unorder_linklist.py
 > Describe   : 无序单链表
 > Version    : 0.2
'''
class LinkedlistEmptyError(Exception):
	def __init__(self,obj):
		super().__init__()
		self.msg=f'{obj} is empty.'
	def __str__(self):
		return self.msg
class Node(object):
	def __init__(self,data):
		self._data=data
		self._next=None
	@property
	def data(self):
		return self._data
	@data.setter
	def data(self,data):
		self._data=data
	@property
	def next(self):
		return self._next
	@next.setter
	def next(self,node):
		self._next=node

class UnorderLinkedlist(object):
	def __init__(self):
		self._head=None
		self._length=0
	@property
	def length(self):
		return self._length
	@property
	def head(self):
		return self._head
	def isempty(self):
		return self._head==None
	def addhead(self,data):
		node=Node(data)
		node.next=self._head
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
			current.next=node
			self._length+=1
		return self._length
	def insert(self,data,position):
		'''
		position:0~self.length
		position=-1 ->self.length
		'''
		if not self._head:
			raise LinkedlistEmptyError(self)
		elif position>self._length:
			raise IndexError('index is too large')
		if position==0:
			self.addhead(data)
		elif position in (-1,self.length):
			self.addtail(data)
		else:
			index=0
			current=self._head
			while index!=position:
				index+=1
				previous=current
				current=current.next
			node=Node(data)
			node.next=current
			previous.next=node
			self._length+=1
		return self._length
	def pop(self,position=0):
		if not self._head:
			raise LinkedlistEmptyError(self)
		elif position>=self._length:
			raise IndexError('index is too large')
		else:
			rubbish=None
			if not position or self.length==1:
				rubbish=self._head.data
				self._head=self._head.next
			else:
				index=0
				current=self._head
				if position==-1:
					position=self._length-1

				while index!=position:
					index+=1
					previous=current
					current=current.next
				if index==self._length-1:
					previous.next=None
				else:
					previous.next=current.next
				rubbish=current.data
			self._length-=1
			return rubbish
	def delete(self):
		self._head=None
		self._length=0
		return self._length
	def getall(self):
		current=self._head
		while current:
			yield current.data
			current=current.next
if __name__ == '__main__':
	ul=UnorderLinkedlist()
