#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct      s_node {
    struct s_node   *next;
    struct s_node   *next1;
    struct s_node   *next2;
    int             fric;
    int             id;
    int             explored;
    int             a;
    int             b;
}                   t_node;

t_node  *create_node(int id, int fric)
{
    t_node *node;
    
    node = malloc(sizeof(t_node));
    node->next = NULL;
    node->next1 = NULL;
    node->next2 = NULL;
    node->fric = fric;
    node->id = id;
    node->explored = -1;
    node->a = -1;
    node->b = -1;
    return (node);
}

void    link_nodes(t_node *begin, t_node *src, int link_id)
{
    while (begin)
    {
        if (begin->id == link_id)
        {
            if (!src->next1)
                src->next1 = begin;   
            else
                src->next2 = begin;
            return ;
        }
        begin = begin->next;   
    }
}

int     backtracker(t_node *node)
{
    if (node->id == -2)
        return (0);
    node->explored = 0; 
    if (node->next1->explored == -1 && node->a == -1)
        node->a = backtracker(node->next1) + node->fric; 
    if (node->next2->explored == -1 && node->b == -1)
        node->b = backtracker(node->next2) + node->fric;
    node->explored = -1; 
    return (node->a > node->b ? node->a : node->b);
}

int main()
{
    int N;
    t_node *node;
    t_node *begin;
    t_node *node2;
    char * pch;
  
    begin = create_node(-1, -1);
    node = begin;
    scanf("%d", &N); fgetc(stdin);
    for (int i = 0; i < N; i++) {
        node->next = create_node(i, -1);
        node = node->next;
    }
    node = begin->next;
    node2 = node->next;
    for (int i = 0; i < N; i++) {
        char room[257];
        fgets(room, 257, stdin);
        pch = strtok (room," ,.-");
        pch = strtok (NULL, " ,.-");
        node->fric = atoi(pch);
        pch = strtok (NULL, " ,.-");
       if (pch[0] == 'E')
            node->next1 = create_node(-2, -2);
        else
            link_nodes(begin, node, atoi(pch));
        pch = strtok (NULL, " ,.-");
        if (pch[0] == 'E')
            node->next2 = create_node(-2, -2);
        else
            link_nodes(begin, node, atoi(pch));
        node = node->next;
    }
    printf("%d\n", backtracker(begin->next));
    return 0;
}