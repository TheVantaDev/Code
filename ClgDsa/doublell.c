#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int rollno;
    int age;
    char name[20];
    struct Node *next;
    struct Node *previous;
} Node;
Node *head = NULL;
void insert() {
    Node *ptr = (Node *)malloc(sizeof(Node));
    printf("Enter rollno, name, age: ");
    scanf("%d %s %d", &ptr->rollno, ptr->name, &ptr->age);
    ptr->next = NULL;
    ptr->previous = NULL;

    if (head == NULL) {
        head = ptr;
    } else {
        Node *temp = head;
        while (temp->next != NULL) {
            temp = temp->next;
        }
        ptr->previous = temp;
        temp->next = ptr;
    }
}

void create() {
    for (int i = 0; i < 4; i++) {
        insert();
    }
}

void display() {
    Node *temp = head;
    while (temp != NULL) {
        printf("[Roll: %d, Name: %s, Age: %d] <-> ", temp->rollno, temp->name, temp->age);
        temp = temp->next;
    }
    printf("NULL\n");
}
void delete() {
    int key;
    printf("Enter rollno to delete: ");
    scanf("%d", &key);

    Node *temp = head;
    while (temp != NULL) {
        if (temp->rollno == key) {
            if (temp->previous != NULL)
                temp->previous->next = temp->next;
            else
                head = temp->next;

            if (temp->next != NULL)
                temp->next->previous = temp->previous;

            free(temp);
            printf("Node deleted.\n");
            display();
            return;
        }
        temp = temp->next;
    }
    printf("Node not found.\n");
}

void search() {
    int key;
    printf("Enter rollno to search: ");
    scanf("%d", &key);

    Node *temp = head;
    while (temp != NULL) {
        if (temp->rollno == key) {
            printf("Found: Roll = %d, Name = %s, Age = %d\n", temp->rollno, temp->name, temp->age);
            return;
        }
        temp = temp->next;
    }
    printf("Not found.\n");
}

void modify() {
    int key;
    printf("Enter rollno to modify: ");
    scanf("%d", &key);

    Node *temp = head;
    while (temp != NULL) {
        if (temp->rollno == key) {
            printf("Enter new name and age: ");
            scanf("%s %d", temp->name, &temp->age);
            printf("Node updated.\n");
            display();
            return;
        }
        temp = temp->next;
    }
    printf("Not found.\n");
}

void insertAtPosition() {
    int pos;
    printf("Enter position to insert (0-based index): ");
    scanf("%d", &pos);
    Node *newNode = (Node *)malloc(sizeof(Node));
    printf("Enter rollno, name, age: ");
    scanf("%d %s %d", &newNode->rollno, newNode->name, &newNode->age);
    newNode->next = NULL;
    newNode->previous = NULL;
    if (pos == 0) {
        newNode->next = head;
        if (head != NULL)
            head->previous = newNode;
        head = newNode;
        display();
        return;
    }

    Node *temp = head;
    int i = 0;

    while (temp != NULL && i < pos - 1) {
        temp = temp->next;
        i++;
    }

    if (temp == NULL) {
        printf("Invalid position.\n");
        free(newNode);
        return;
    }

    newNode->next = temp->next;
    newNode->previous = temp;

    if (temp->next != NULL)
        temp->next->previous = newNode;

    temp->next = newNode;
    display();
}

int main() {
    create();
    display();

    int ch;
    printf("\n1.search");
    printf("\n2.modify");
    printf("\n3.insert at any position");
    printf("\n4.delete");
    printf("\nenter choice: ");
    scanf("%d", &ch);

    switch (ch) {
        case 1:
            search();
            break;
        case 2:
            modify();
            break;
        case 3:
            insertAtPosition();
            break;
        case 4:
            delete();
            break;
        default:
            break;
    }

    return 0;
}