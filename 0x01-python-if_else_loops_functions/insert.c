#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - inserts a number into a sorted
 * singly linked list
 *
 * @head: head node
 * @number: number to insert
 * Return: pointer to the address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
listint_t *temp = *head;
listint_t *new_node = malloc(sizeof(listint_t));
listint_t *current;
if (new_node == NULL)
return (NULL);
new_node->n = number;
new_node->next = NULL;
if (*head == NULL)
{
*head = new_node;
return (new_node);
}
while (temp != NULL)
{
if (number < temp->n)
{
new_node->next = temp;
*head = new_node;
return (new_node);
}
else if ((temp->n < number && temp->next->n > number) || temp->n == number)
{
current = temp->next;
temp->next = new_node;
new_node->next = current;
return (new_node);
}
temp = temp->next;
}

if (temp->next == NULL)
{
temp->next = new_node;
return (new_node);
}
return (new_node);
}