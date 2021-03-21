class MinStack {
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }    
    void push(int x) {
        mystack.push_back(x);
        length++;
    }
    
    void pop() {
        mystack.pop_back();
        length--;
    }
    
    int top() {
        return mystack[length-1];
    }
    
    int getMin() {
        int result = *min_element(mystack.begin(), mystack.end());
        return result;
    }
private:
    vector<int> mystack;
    int length = 0;                                  
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */


// answer 2: use second stack to save sorted data
// class MinStack {
// private:
//     stack<int> mystack;
//     stack<int> small_;
// public:
//     /** initialize your data structure here. */
//     MinStack() {
        
//     }    
//     void push(int x) {
//         mystack.push(x);
//         if(small_.empty() || getMin()>=x){
//             small_.push(x);
//         }
//     }
    
//     void pop() {
//         if(mystack.top() == getMin()){
//             small_.pop();
//         }
//         mystack.pop();
        
//     }
    
//     int top() {
//         return mystack.top();
//     }
    
//     int getMin() {
//         return small_.top();
//     }

// };
