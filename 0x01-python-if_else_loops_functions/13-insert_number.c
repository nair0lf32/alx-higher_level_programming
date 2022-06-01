#include "lists.h"
/**
*insert_node - inserts a number into a sorted singly linked list
*@head: list
*@number: element to insert
*Return: the address of the new node, or NULL if it failed
*/
listint_t *insert_node(listint_t **head, int number)
{
listint_t *new_node;
listint_t *temp;
new_node = malloc(sizeof(listint_t));
if (new_node == NULL)
{
return (NULL);
}
new_node->n = number;
new_node->next = NULL;
if (*head == NULL)
{
*head = new_node;
return (new_node);
}
temp = *head;
while (temp->next != NULL)
{
if (temp->n > number)
{
break;
}
temp = temp->next;
}
if (temp->n > number)
{
new_node->next = temp;
*head = new_node;
}
else
{
new_node->next = temp->next;
temp->next = new_node;
}
return (new_node);
}
