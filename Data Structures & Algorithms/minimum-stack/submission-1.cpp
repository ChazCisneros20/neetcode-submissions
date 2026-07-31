class MinStack {
public:
        
        vector<int> stack;
        vector<int> minStack;
    MinStack() {
        
    }
    
    void push(int val) {
        if (minStack.size() == 0)
        {
            minStack.push_back(val);
        }
        else if (minStack.size() > 0 && val <= minStack.back())
        {
            minStack.push_back(val);
        }
        stack.push_back(val);

    }
    
    void pop() {
        if (stack.size() > 0)
        {
            if (minStack.size() > 0 && stack.back() == minStack.back())
            {
                minStack.pop_back();
            }
            stack.pop_back();
        }
    }
    
    int top() {
        if (stack.size() > 0)
        {
            return stack.back();
        }
            
        else
        {
            return 0;
        }
    }
    
    int getMin() {
        if (minStack.size() > 0)
        {
            return minStack.back();
        }
        else
        {
            return 0; 
        }
    }
};
