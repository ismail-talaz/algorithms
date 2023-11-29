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
        T items[MAX_SIZE+1];
        int front;
        int back;

    public:
        Queue();
        void deQueue();
        T getFront();
        void enQueue(const T data);
        bool isEmpty();
        bool isFull();
        void print();
        int size() const;
};


template <class T>
Queue<T>::Queue(){
    front = 0;
    back = 0;
}

template <class T>
T Queue<T>::getFront(){
    return items[front+1];
}

template <class T>
void Queue<T>::enQueue(const T data){
    if(isFull()){
        std::cout << "Queue is full!"<<std::endl;
    }
    else{
        back = (back + 1) % (MAX_SIZE+1);
        items[back] = data;
    }
    
}

template <class T>
void Queue<T>::deQueue(){
    front = (front + 1) % (MAX_SIZE+1);
}

template <class T>
bool Queue<T>::isEmpty(){
    return front == back;
}

template <class T>
bool Queue<T>::isFull(){
    return ( (back + 1) % (MAX_SIZE+1) == front );
}


template <class T>
void Queue<T>::print(){

    if(isEmpty()){
        std::cout<<"Queue is empty.";
    }
    else{
        int index = front+1;
        std::cout << "Queue: ";
        while (index != (back + 1) % (MAX_SIZE+1)) {
            std::cout << items[index] << " ";
            index = (index + 1) % (MAX_SIZE+1);
        }
        std::cout << std::endl;
    }
}

template <class T>
int Queue<T>::size() const {
    return (back-front+1+MAX_SIZE)%(MAX_SIZE+1);
}





















#endif
