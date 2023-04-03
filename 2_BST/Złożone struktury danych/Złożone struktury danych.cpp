#include <stdio.h>
#include <stdlib.h>


#define REL(a,b) (a)>(b) ? (1):(0)

typedef struct bstree{
    int key;
    struct bstree* left;
    struct bstree* right; 
    struct bstree* parent;
    }bstree;

bstree* CreateLeaf(int a, bstree* p){
    bstree* t = malloc(sizeof(bstree));

    if(!t) {
        printf ("Brak pamieci !!!\n");
    return NULL;
    }

    t -> key = a;
    t -> left = NULL;
    t -> right = NULL;
    t -> parent = p;

    return t;
}

void AddLeaf(int a, bstree** tr, bstree* parent){
    if (*tr){
        if(REL((*tr) -> key, a))
            AddLeaf(a , &(*tr) -> left, *tr);
        else
            AddLeaf(a , &(*tr) -> right, *tr);
    }
    else
        *tr = CreateLeaf(a, parent);
}

bstree* DeleteTree(bstree* tr){
    if (tr -> left)
        DeleteTree(tr -> left) ;
    if (tr -> right)
    DeleteTree(tr -> right);

    free(tr) ;

    return NULL ;
}

void PrintTreeInorder(const bstree* tr){
    if(tr){
        PrintTreeInorder(tr -> left);
        printf("%d ", tr -> key);
        PrintTreeInorder (tr -> right);
    }
}

void PrintTreePreorder(const bstree* tr){
    if(tr){
        printf("%d ", tr -> key);
        PrintTreePreorder(tr -> left);
        PrintTreePreorder (tr -> right);
    }
}

void PrintTreePostorder(const bstree* tr){
    if(tr){
        PrintTreePostorder(tr -> left);
        PrintTreePostorder (tr -> right);
        printf("%d ", tr -> key);
    }
}

int Find(bstree *tr, int val){
    int node = 0;

    while(tr){
        if(val < tr -> key)
        {
            tr = tr -> left;
            node++;
            if(val == tr -> key)
                return node;
        }
        else
        {
            tr = tr -> right;
            node++;
            if(val == tr -> key)
                return node;
        }
    }
}


int Level(bstree *tr, int* tab, int length){
    int max = 0, node = 0;


    for(int i = 0; i < length; i++)
    {
        node = Find(tr, tab[i]);
        if(node > max)
            max = node;
    }

    return max;
}


int main(void)
{
    int liczba[] =  {15 ,5 ,16 ,20 ,3 ,12 ,18 ,23 ,10 ,13 ,6 ,7};
    bstree* root = NULL;

    for(int i = 0; i < sizeof(liczba)/sizeof(int); i++)
    {       
        // liczba[i] = rand() % 41;
        // printf("%d ", liczba[i]);
        AddLeaf(liczba[i], &root, NULL);
    }
    // printf("\n--------------------\n\n");
    // printf("Inorder (rosnąco): \n");
    PrintTreeInorder(root);
    printf("\n\n");

    // printf("Preorder (od korzenia): \n");
    PrintTreePreorder(root);
    printf("\n\n");
    
    // printf("Postorder (do korzenia): \n");
    // PrintTreePostorder(root);
    // printf("\n\n");

    int find;
    printf("find: ");
    scanf("%d", &find);
    int search = Find(root, find);
    printf("search = %d\n", search);

    int level = Level(root, liczba, sizeof(liczba)/sizeof(int));
    printf("level = %d\n", level);






    root = DeleteTree(root);

    return 0;
}