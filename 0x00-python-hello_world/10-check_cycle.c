#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Pointer to the head node of an existing list
 *
 * Return: 1 if the list has a cycle, otherwise 0
 */
int check_cycle(listint_t *list)
{
	listint_t *current;

	/* Return 0 if the list is empty */
	if (!list)
		return (0);
	current = list;
	while (current)
	{
		/* Condition if the list has a cycle */
		if (current->next == list)
			return (1);
		current = current->next;
	}
	return (0);
}
