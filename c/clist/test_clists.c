#include <stdio.h>
#include <ctest.h>
#include "clist.h"

int main() {
    BEGIN_TESTING("clist.h");

    TEST("Can create node") {
        Node* n = make_node(3);
        ASSERT_EQ(n->val, 3);
        ASSERT_EQ(n->next, NULL);
    }

    TEST("Can print list") {
        Node* mylist = NULL;
        RETURNS_STR(print_list, "", (mylist));

        mylist = make_node(1);
        mylist->next = mylist;
        RETURNS_STR(print_list, "1", (mylist));

        Node* two = make_node(2);
        two->next = mylist;
        mylist->next = two;

        Node* n = make_node(1024);
        n->next = mylist;
        two->next = n;

        RETURNS_STR(print_list, "1 -> 2 -> 1024", (mylist));
    }

    END_TESTING();
}