#ifndef BST_H
#define BST_H

#include <string>
#include <vector>
#include <iostream>
#include <utility>
#include <algorithm>
using namespace std;

template <class T>
class Queue {

    private:
        struct QueueNode{
            T data;
            QueueNode* next;
            QueueNode(T nData = T(), QueueNode* nNext = NULL):data(nData),next(nNext) {}
        };
        QueueNode* backptr;
        QueueNode* getFront(){
            return backptr?backptr->next:NULL;
        };
    public:
        Queue();
        ~Queue();
        void deQueue();
        void enQueue(const T data);
        bool isEmpty();
        void print();
};


template <class T>
Queue<T>::Queue(){
    backptr=NULL;
}

template <class T>
Queue<T>::~Queue(){
    while(isEmpty()){
        deQueue();
    }
    backptr=NULL;
}

template <class T>
void Queue<T>::enQueue(const T data){
    if(isEmpty()){
        QueueNode* newNode = new QueueNode(data);
        backptr=newNode;
        backptr->next=backptr;
    }
    else{
        QueueNode* newNode = new QueueNode(data,backptr->next);
        backptr->next=newNode;
        backptr=newNode;
    }

}

template <class T>
void Queue<T>::deQueue(){
    if (isEmpty()){return;}
    if (backptr==backptr->next){
        delete backptr;
        backptr=NULL;
    }
    else{
        QueueNode* temp = getFront();
        backptr->next = backptr->next->next;
        temp->next = NULL;
        delete temp;
    }
}

template <class T>
bool Queue<T>::isEmpty(){
    return backptr==NULL;
}

template <class T>
void Queue<T>::print(){
    if (isEmpty()){
        std::cout<< "Queue is empty.";
    }
    else{
        QueueNode* currNode = getFront();
        do{
            std::cout<< currNode->data<<" ";
            currNode=currNode->next;
        }while(currNode!=backptr->next);
    }
    std::cout<<std::endl;

}



















#endif
