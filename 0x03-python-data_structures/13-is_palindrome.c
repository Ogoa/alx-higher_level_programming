#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome
 * @head: Pointer to the first node in the linked list
 *
 * Return: 0 if it is not a palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int i = 0, list_len = 0, j = 0;
	int *list;

	if (!*head) /* An empty list is a palindrome */
		return (1);
	temp = *head;
	while (temp) /* Evaluate the length of the list */
	{
		temp = temp->next;
		list_len++;
	}
	list = malloc(sizeof(list_len));
	if (!list)
		return (0);
	temp = *head;
	while (temp)
	{
		list[i] = temp->n;
		i++;
		temp = temp->next;
	}
	for (i = 0, j = list_len - 1; i < list_len / 2; i++, j--)
	{
		if (list[i] != list[j])
			return (0);
	}
	return (1);
}
