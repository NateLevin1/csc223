#include <stdio.h>
#include <stdlib.h>
#include "pqueue.h"

Node* make_pq_node(char data, int weight) {
    Node* new = malloc(sizeof(Node));
    if (new == NULL) {
        printf("Memory allocation failed\n");
        exit(1);
    }
    new->node = make_tree_node(data);
    new->weight = weight;
    new->next = NULL;

    return new;
}

void sortedAppend(Node** head, Node* temp) {
    Node* start = *head;

    if (*head == NULL || (*head)->weight > temp->weight)
    {
        temp->next = *head;
        *head = temp;
    } else {
        while (start->next != NULL && start->next->weight <= temp->weight)
        {
            start = start->next;
        }

        temp->next = start->next;
        start->next = temp;
    }
}

void print_pq(Node* head) {
    Node* start = head;
    while (start != NULL) {
        printf("%c (%d) -> ", start->node->data, start->weight);
        start = start->next;
    }
    printf("NULL\n");
}
