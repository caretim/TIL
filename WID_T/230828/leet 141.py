def hasCycle(self, head: Optional[ListNode]) -> bool:
	seen = [] #list of nodes we have already seen
	while head: 
		if head in seen: #if we already saw this node then there is a cycle
			return True
		seen.append(head) #add node to our list of seen nodes
		head = head.next 
	return False #we reached the end of the list -- no cycle!




