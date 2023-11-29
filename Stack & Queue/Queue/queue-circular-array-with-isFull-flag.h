#ifndef QUEUE_H
#define QUEUE_H

#include <string>
#include <vector>
#include <iostream>
#include <utility>
#include <algorithm>
using namespace std;

static const int MAX_SIZE = 30;

template <class T>
class Queue {

    private:
        bool isFull;
        T items[MAX_SIZE];
        int front;
        int back;

    public:
        Queue();
        void deQueue();
        T getFront();
        void enQueue(const T data);
        bool isEmpty();
        void print();
        int size() const;
};


template <class T>
Queue<T>::Queue(){
    front = 0;
    back = MAX_SIZE-1;
    isFull = false;
}

template <class T>
T Queue<T>::getFront(){
    return items[front];
}

template <class T>
void Queue<T>::enQueue(const T data){
    if(isFull){
        std::cout << "Queue is full!"<<std::endl;
    }
    else{
        back = (back + 1) % MAX_SIZE;
        items[back] = data;
        if ((back + 1) % MAX_SIZE == front){
            isFull = true;
        }
    }
    
}

template <class T>
void Queue<T>::deQueue(){
    front = (front + 1) % MAX_SIZE;
    isFull = false;
}

template <class T>
bool Queue<T>::isEmpty(){
    return (isFull == false) && ((back + 1) % MAX_SIZE == front);
}


template <class T>
void Queue<T>::print(){

    if(isEmpty()){
        std::cout<<"Queue is empty.";
    }
    else{
        int index = front;
        std::cout << "Queue: ";
        do {
            std::cout << items[index] << " ";
            index = (index + 1) % MAX_SIZE;
        } while (index != (back + 1) % MAX_SIZE);
        std::cout << std::endl;
    }
}

template <class T>
int Queue<T>::size() const {
    if (back >= front) {
        return back - front + 1;
    } else {
        return back + MAX_SIZE - front + 1;
    }
}





















#endif
