#ifndef BST_H
#define BST_H

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
        int counter;
        T items[MAX_SIZE];
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
    back = MAX_SIZE-1;
    counter = 0;
}

template <class T>
T Queue<T>::getFront(){
    return items[front];
}

template <class T>
void Queue<T>::enQueue(const T data){
    if(isFull()){
        std::cout << "Queue is full!"<<std::endl;
    }
    else{
        back = (back + 1) % MAX_SIZE;
        items[back] = data;
        counter++;
    }
    
}

template <class T>
void Queue<T>::deQueue(){
    front = (front + 1) % MAX_SIZE;
    counter--;
}

template <class T>
bool Queue<T>::isEmpty(){
    return counter == 0;
}

template <class T>
bool Queue<T>::isFull(){
    return counter == MAX_SIZE;
}


template <class T>
void Queue<T>::print(){

    if(isEmpty()){
        std::cout<<"Queue is empty.";
    }
    else{
        int index = front;
        std::cout << "Queue: ";
        while (index != (back + 1) % MAX_SIZE) {
            std::cout << items[index] << " ";
            index = (index + 1) % MAX_SIZE;
        }
        std::cout << std::endl;
    }
}

template <class T>
int Queue<T>::size() const {
    return (back-front+1+MAX_SIZE)%MAX_SIZE;
}





















#endif