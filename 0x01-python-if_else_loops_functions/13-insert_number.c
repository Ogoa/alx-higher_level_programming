#include "lists.h"

/**
 * insert_node - Inserts a number into a sorted singly linked list
 * @head: Pointer to the address of the first node in the list
 * @number: The data value of the node being inserted
 *
 * Return: The address of the new node otherwise NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *temp;
	listint_t *prev = NULL;

	new_node = malloc(sizeof(listint_t));
	if (!new_node) /* Check if malloc has failed */
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	/* Inserting the node into the sorted list */
	if (!head || !*head)
	{
		*head = new_node;
		return (new_node);
	}
	else
	{
		temp = *head;
		while (temp)
		{
			if (number <= temp->n)
			{
				new_node->next = temp;
				if (prev)
					prev->next = new_node;
				else
					*head = new_node;
				return (new_node);
			}
			prev = temp;
			temp = temp->next;
		}
	}
	if (prev)
		prev->next = new_node;
	else
		*head = new_node;
	return (new_node);
}
