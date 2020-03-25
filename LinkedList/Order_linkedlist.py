from Unorder_linkedlist import (Node,
	LinkedlistEmptyError as EmptyError,
	UnorderLinkedlist as Ulinkedlist)

class OrderLinkedlist(Ulinkedlist):
	def __shield(self,method):
		raise AttributeError(f'{self} has not method {method}.')
	def addhead(self):
		self.__shield('addhead')
	def addtail(self):
		self.__shield('addtail')

	def insert(self):
		self.__shield('insert')
	def add(self,data):
		node=Node(data)
		if not self._head:
			self._head=node
		else:
			previous=None
			current=self._head
			try:
				while current.data<=data:
					previous=current
					current=current.next
				if not previous:
					node.next=self._head
					self._head=node
				else:
					previous.next=node
					node.next=current
			except AttributeError:
				previous.next=node
		self._length+=1
		return self.length

	def pop(self,data):
		if not self._head:
			raise EmptyError(self)
		else:
			try:
				previous=None
				current=self._head
				while current.data!=data:
					previous=current
					current=current.next
				if not previous:
					self._head=self._head.next
				else:
					previous.next=current.next
				self._length-=1
			except AttributeError:
				raise ValueError(f'Value <{data}> does not exist.')
			return self.length

if __name__ == '__main__':
	ol=OrderLinkedlist()