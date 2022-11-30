#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * add_nodeint_end - prints all the elements
 * in a linked list
 *
 * @h: head of the list
 *
 * Return: the number of nodes
 */

// listint_t *add_nodeint_end(listint_t **head, const int n){

// }

struct node
{
    int data;
    struct node *next;
};

typedef struct node node;

/**
 * create_linked_list -  adds node to the list
 *
 * @head: head node
 * @data: data for new node
 * Return - pointer to the new node
 */
node *create_linked_list(int data)
{
    node *new_node = malloc(sizeof(node));
    new_node->data = data;
    new_node->next = NULL;

    return (new_node);
}

/**
 * print_list - prints a the items in the list
 *
 * @head: head node
 *
 * Return: nichts
 */
void print_list(node *head)
{
    node *temp = head;

    while (temp != NULL)
    {
        printf("%d\n", temp->data);
        temp = temp->next;
    }
}

/**
 * add_node_end - add node to the end of the list
 *  @head: head node
 * Return: the new node
 */
node *add_node_end(node **head, int data)
{
    node *new_node = malloc(sizeof(node));
    node *current = *head;

    if (new_node == NULL)
        return (NULL);

    new_node->data = data;
    new_node->next = NULL;

    if (*head == NULL)
    {
        *head = new_node;
        return (new_node);
    }

    while (current->next != NULL)
    {
        current = current->next;
    }

    current->next = new_node;
    return (new_node);
}

/**
 * add_node_beginning - add new node at the
 * beginning of the linked list
 *
 * @head: head node
 * @data: data of new node
 * Return: new node
 */
node *add_node_beginning(node **head, int data)
{
    node *new_node = malloc(sizeof(node));
    node *first_node = *head;

    if (new_node == NULL)
        return (new_node);

    new_node->data = data;
    new_node->next = NULL;

    if (*head == NULL)
    {
        *head = new_node;
        return (new_node);
    }

    *head = new_node;
    new_node->next = first_node;
    return (new_node);
}
/**
 * insert_node_at: insert new node at a particular
 * index
 *
 * @head : head node
 * @data : new node data
 * @index : index to insert new node
 * Return: node* new node
 */

node *insert_node_at(node **head, int data, int index)
{
    int count = 0;
    node *new_node = malloc(sizeof(node));
    node *temp = *head;

    if (new_node == NULL)
        return (new_node);

    new_node->data = data;
    new_node->next = NULL;

    if (*head == NULL)
    {
        *head = new_node;
        return (new_node);
    }

    if (index == 0)
    {
        *head = new_node;
        new_node->next = temp;
    }

    while (temp != NULL)
    {
        node *prev = temp;
        node *next = temp->next;
        if (count == index - 1)
        {
            prev->next = new_node;
            new_node->next = next;
            return (new_node);
        }
        temp = temp->next;
        count++;
    }
}

int delete_node_at_index(node **head, int index)
{
    node *temp = *head;
    int count = 0;

    if (index == 0)
    {
        *head = (*head)->next;
        free(temp);
        return (1);
    }

    while (temp != NULL)
    {
        // node *prev = temp;

        if (count == index - 1)
        {
            temp = temp->next->next;
            free(temp);
            return (1);
        }

        count++;
        temp = temp->next;
    }
}

/**
 * main - Entry point into program
 *
 * Return: 0
 */

int main()
{
    node *head;

    head = NULL;
    // create_linked_list(89);
    add_node_end(&head, 89);
    add_node_end(&head, 76);
    add_node_beginning(&head, 109);
    add_node_end(&head, 97);
    add_node_beginning(&head, 52);
    add_node_beginning(&head, 30);
    // insert_node_at(&head, 9, 0);
    delete_node_at_index(&head, 1);

    print_list(head);
    return (0);
}