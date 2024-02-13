#include <stdio.h>
#include <ctest.h>
#include "linkedlist.h"

int main() {
    BEGIN_TESTING("list.h");

    TEST("Can create a node") {
        Node* n = make_node(3);
        ASSERT_EQ(n->val, 3);
        ASSERT_EQ(n->next, NULL);
    }

    TEST("Can create two nodes and link them together") {
        Node* n1 = make_node(3);
        Node* n2 = make_node(2);
        n1->next = n2;
        ASSERT_EQ(n1->val, 3);
        ASSERT_EQ(n1->next->val, 2);
        ASSERT_NOT_EQ(n1->next, NULL);
        ASSERT_EQ(n1->next->next, NULL);
    }

    TEST("Can add a node to an empty list") {
        Node* mylist = NULL;
        Node* n = make_node(2);
        insert_in_front(&mylist, &n);
        ASSERT_EQ(mylist->val, 2);
        ASSERT_EQ(mylist->next, NULL);
    }

    // TEST("Can output list length") {
    //     Node* mylist = NULL;
    //     Node* n = make_node(1);
    //     insert_in_front(&mylist, &n);
    //     ASSERT_EQ(list_length(mylist), 1);

    //     Node* n2 = make_node(2);
    //     insert_in_front(&mylist, &n2);
    //     ASSERT_EQ(list_length(mylist), 2);
    // }

    TEST("Can print list") {
        Node* mylist = NULL;
        RETURNS_STR(print_list, "", (mylist));

        Node* n = make_node(1);
        insert_in_front(&mylist, &n);

        RETURNS_STR(print_list, "1", (mylist));

        Node* n2 = make_node(2);
        insert_in_front(&mylist, &n2);
        Node* n3 = make_node(3);
        insert_in_front(&mylist, &n3);
        Node* n4 = make_node(4);
        insert_in_front(&mylist, &n4);

        RETURNS_STR(print_list, "4 -> 3 -> 2 -> 1", (mylist));

        Node* n5 = make_node(1024);
        insert_in_front(&mylist, &n5);
        RETURNS_STR(print_list, "1024 -> 4 -> 3 -> 2 -> 1", (mylist));
    }

    END_TESTING();
}
