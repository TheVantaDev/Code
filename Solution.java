class MyLinkedList {
    class Node{
        int val;
        Node next;
        Node prev;

        public Node(int v) {
            this.val=v;
        }
    }
    Node head;
    Node tail;
    int size;
    public MyLinkedList() {
        head=new Node(0);
        tail=new Node(0);
        head.next=tail;
        tail.prev=head;
        size=0;
    }
    Node getNode(int index)
    {
        Node curr;
        if(index<size/2)
        { curr=head.next;
            for(int i=0;i<index;i++)
            {
                curr=curr.next;
            }
        }
        else{
            curr=tail.prev;
            for(int i=size-1;i>index;i--)
            {
                curr=curr.prev;
            }

        }
        return curr;
    }
    public int get(int index) {
        Node curr=getNode(index);
        return curr==null ? -1:  curr.val;
    }
    
    public void addAtHead(int val) {
   addAtIndex(0, val);
    }
    
    public void addAtTail(int val) {
        addAtIndex(size, val);
        
    }
    
    public void addAtIndex(int index, int val) {
        if(index<0 || index>=size) return;
        Node curr=head;
        Node newNode=new Node(val);
        if(index==0)
        {  newNode.next=head;
            head.prev=newNode;
            newNode=head;
            newNode.prev=null;
             
        }
        for(int i=0;i<index;i++)
        {
            curr=curr.next;
        }
        newNode.prev=curr;
        curr.next.prev=newNode;
        newNode.next=curr.next;
        curr.next=newNode;
        size++;
    }
    
    public void deleteAtIndex(int index) {
       if(index<0 || index>=size) return;
        Node curr=head;
        if(index==0)
        {
            curr=curr.next;
            curr.prev=null;
        }
        for(int i=0;i<index;i++)
        { curr=curr.next;
            
        }
        Node currBack=curr.prev;
        currBack.next=curr.next;
        curr.next.prev=currBack;
        size--;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */