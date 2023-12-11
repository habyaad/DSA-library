
public class CustomLinkedList {
	public class Node {
		public int data;
		public Node next;

		public Node(int data) {
			this.data = data;
		}
	}

	public Node head = null;

	public void appendData(int val) {
		Node newDataNode = new Node(val);
		if (head == null) {
			head = newDataNode;
		} else {
			Node currentNode = head;
			while (currentNode.next != null) {
				currentNode = currentNode.next;
			}
			currentNode.next = newDataNode;
		}
	}
	public void pop() {
		if (head == null) {
			return;
		} else {
			Node currentNode = head;
			while (currentNode.next.next != null) {
				currentNode = currentNode.next;
			}
			currentNode.next = null;
		}
	}


	public void prependData(int val) {
		Node newDataNode = new Node(val);
		if (head == null) {
			head = newDataNode;
		} else {
			Node currentNode = head;
			head = newDataNode;
			newDataNode.next = currentNode;
		}
	}

	public int length() {
		if (head == null) {
			return 0;
		} else {
			int counter = 0;
			Node currentNode = head;
			while (currentNode != null) {
				counter++;
				currentNode = currentNode.next;
			}
			return counter;
		}
	}

	public boolean isEmpty() {
		if (length() == 0) {
			System.out.println("true");

			return true;
		} else {
			System.out.println("false");

			return false;
		}
	}

	public void printList() {
		StringBuilder linkedList = new StringBuilder();
		Node currentNode = head;
		while (currentNode != null) {
			linkedList.append(currentNode.data + "->");
			currentNode = currentNode.next;
		}
		System.out.println(linkedList);
	}

	public void insertAt(int index, int val) {
		Node newDataNode = new Node(val);
		if (index > length() || index < 0) {
			System.out.println("index error");
		} else if (index == 0) {
			prependData(val);
		} else if (index == length()) {
			appendData(val);
		} else {
			int counter = 1;
			Node currentNode = head;
			while (counter < index) {
				counter++;
				currentNode = currentNode.next;
			}
			newDataNode.next = currentNode.next;
			currentNode.next = newDataNode;
		}

	}
	public void removeAt(int index) {
		if (index >= length() || index < 0) {
			System.out.println("index error");
		}else if(index == 0) {
			head = head.next;
		}else {
			int counter = 0;
			Node currentNode = head;
			while (counter < index-1) {
				counter++;
				currentNode = currentNode.next;
			}
			currentNode.next = currentNode.next.next;
		}

	}
	public void getValueAt(int index) {
		if (index >= length() || index < 0) {
			System.out.println("index error");
		}else {
			int counter = 0;
			Node currentNode = head;
			while (counter <= index) {
				if(counter == index) {
					System.out.println(currentNode.data);
					return;
				}
				counter++;
				currentNode = currentNode.next;
			}
		}

	}

	public static void main(String[] args) {
		CustomLinkedList customLinkedList = new CustomLinkedList();
		customLinkedList.isEmpty();
		customLinkedList.appendData(50);
		customLinkedList.appendData(1);
		customLinkedList.appendData(32);
		customLinkedList.prependData(2);
		customLinkedList.insertAt(0, 100);
		customLinkedList.insertAt(5, 100);
		customLinkedList.insertAt(3, 21);
		customLinkedList.isEmpty();
		customLinkedList.printList();
		customLinkedList.getValueAt(6);
		customLinkedList.pop();
		customLinkedList.printList();
		customLinkedList.removeAt(0);
		customLinkedList.printList();
		customLinkedList.removeAt(2);
		customLinkedList.printList();

		System.out.println(customLinkedList.length());

	}
}
