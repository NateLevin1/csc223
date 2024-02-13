typedef struct node {
    int val;
    struct node* next;
} Node;

Node* make_node(int);
void insert_in_front(Node**, Node**);
int list_length(Node*);
char* print_list(Node*);
int find_in_list(Node*, Node* tofind);
void insert_at_end(Node* head, Node* newnode);
void insert_in_order(Node* head, Node* newnode);
void remove_from_list(Node* head, int value);
