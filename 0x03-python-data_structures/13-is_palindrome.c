#include "lists.h"
#include <stdio.h>
/**
*is_palindrome - checks if a singly linked list is a palindrome
*@head: pointer to the first node of the list
*Return: 1 if palindrome and 0 if not
*/
int is_palindrome(listint_t **head)
{
listint_t *slow = *head;
listint_t *fast = *head;
listint_t *prev = NULL;
listint_t *curr = *head;
listint_t *next = NULL;
while (fast != NULL && fast->next != NULL)
{
next = fast->next;
fast->next = prev;
prev = fast;
fast = next;
}
if (fast != NULL)
{
slow = slow->next;
}
while (prev != NULL)
{
if (prev->n != slow->n)
{
return 0;
}
prev = prev->next;
slow = slow->next;
}
return 1;
}
