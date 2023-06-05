#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
* check_cycle - a function that checks if a singly
*linked list has a cycle in it.
* @list: singly linked list
* Return: 0 if there is no cycle, 1 if there is a cycle
**/

int check_cycle(listint_t *list)
{
	listint_t *f, *s;

	if (!list || !list->next)
		return (0);
	f = list->next;
	s = list;
	while (f && f->next)
	{
		f = f->next->next;
		s = s->next;
		if (f == s)
			return (1);
	}
	return (0);
}
