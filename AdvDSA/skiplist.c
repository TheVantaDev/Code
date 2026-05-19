#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
# define MAX_LEVEL 16
typedef struct Node {
    int value;
    struct Node* forward[MAX_LEVEL];
    int key; // Array of forward pointers
} Node;
int currLevel=0;
Node * head;
Node* newNode(int key) {
    Node* ptr = (Node*)malloc(sizeof(Node));
    ptr->key = key;
    ptr->value = 1; 
    for (int i = 0; i < MAX_LEVEL; i++) {
        ptr->forward[i] = NULL;
    }
    return ptr;
}
int randomLevel() {
    int lvl = 0;
    while (rand() % 2 == 0 && lvl < MAX_LEVEL - 1) {
        lvl++;
    }
    return lvl;
}
void insert(int key) {
    Node* update[MAX_LEVEL];
    Node* temp = head;
    for (int i = currLevel; i >= 0; i--) {
        while (temp->forward[i] != NULL && temp->forward[i]->key < key) {
            temp = temp->forward[i];
        }
        update[i] = temp;
    }
    int rLevel = randomLevel();
    if (rLevel > currLevel) {
        for (int i = currLevel + 1; i <= rLevel; i++) {
            update[i] = head;
        }
        currLevel = rLevel;
    }
    Node* n = newNode(key);
    for (int i = 0; i <= rLevel; i++) {
        n->forward[i] = update[i]->forward[i];
        update[i]->forward[i] = n;
    }
}
bool search(int key)
{
     Node * temp =head;
     for(int i= currLevel;i>=0;i--)
     {
        while(temp->forward[i]!=NULL && temp->forward[i]->key < key) temp=temp->forward[i];

     }
        temp = temp->forward[0];
        return temp!=NULL && temp->key == key;
}
void display() {
    for (int i = 0; i <= currLevel; i++) {
        Node* temp = head->forward[i];
        printf("Level %d: ", i);
        while (temp != NULL) {
            printf("%d ", temp->key);
            temp = temp->forward[i];
        }
        printf("\n");
    }
}
int main()
{   head = newNode(-1);
    insert(5);
    insert(15);
    insert(10);
    insert(20);
    insert(2);
    display();
    bool found = search(100);
    printf("Element found: %s\n", found ? "Yes" : "No");
    return 0;
}
