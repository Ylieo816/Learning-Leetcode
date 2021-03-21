class MyCircularDeque {
private:
    int count=0;
    int maxvalue=0;
    vector<int> arr;
public:
    /** Initialize your data structure here. Set the size of the deque to be k. */
    MyCircularDeque(int k) {
        maxvalue = k;
    }
    
    /** Adds an item at the front of Deque. Return true if the operation is successful. */
    bool insertFront(int value) {
        if(count<maxvalue){
            arr.insert(arr.begin(),value);
            count++;
            return true;
        }else{
            return false;
        }
    }
    
    /** Adds an item at the rear of Deque. Return true if the operation is successful. */
    bool insertLast(int value) {
        if(count<maxvalue){
           arr.push_back(value);
            count++;
            return true;
        }else{
            return false;
        }
    }
    
    /** Deletes an item from the front of Deque. Return true if the operation is successful. */
    bool deleteFront() {
        if(count>0){
            arr.erase(arr.begin());
            count--;
            return true;
        }else{
            return false;
        }
    }
    
    /** Deletes an item from the rear of Deque. Return true if the operation is successful. */
    bool deleteLast() {
        if(count>0){
            arr.erase(arr.begin()+count-1);
            count--;
            return true;
        }else{
            return false;
        }
    }
    
    /** Get the front item from the deque. */
    int getFront() {
        if(count !=0){
            return arr[0];
        }else{
            return -1;
        }
    }
    
    /** Get the last item from the deque. */
    int getRear() {
        if(count !=0){
            return arr[count-1];
        }else{
            return -1;
        }
    }
    
    /** Checks whether the circular deque is empty or not. */
    bool isEmpty() {
        if(count ==0){
            return true;
        }else{
            return false;
        }
    }
    
    /** Checks whether the circular deque is full or not. */
    bool isFull() {
        if(count == maxvalue){
            return true;
        }else{
            return false;
        }
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */