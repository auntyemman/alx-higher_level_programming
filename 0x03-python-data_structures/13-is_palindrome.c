#include "lists.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Reverses a singly-linked listint_t list.
 * @head: A pointer to the starting node of the list to reverse.
 *
 * Return: A pointer to the head of the reversed list.
 */

listint_t *reverse_listint(listint_t **head)
{
    listint_t *temp = *head, *current, *prev = NULL;

    while (temp)
    {
        current = temp->next;
        temp->next = prev;
        prev = temp;
        temp = current;
    }

    *head = prev;
    return (*head);
}
/**
 * is_palindrome - A function that checks if a list is a palindrome.
 * @head: The pointer to the head of the list.
 * Return: 0 if list not a palindrome, 1 if it is.
 */

int is_palindrome(listint_t **head)
{
    listint_t *temp, *rev, *mid;
    size_t size = 0, i;

    if (*head == NULL || (*head)->next == NULL)
        return (1);

    temp = *head;
    while (temp)
    {
        size++;
        temp = temp->next;
    }

    temp = *head;
    for (i = 0; i < (size / 2) - 1; i++)
        temp = temp->next;

    if ((size % 2) == 0 && temp->n != temp->next->n)
        return (0);

    temp = temp->next->next;
    rev = reverse_listint(&temp);
    mid = rev;

    temp = *head;
    while (rev)
    {
        if (temp->n != rev->n)
            return (0);
        temp = temp->next;
        rev = rev->next;
    }
    reverse_listint(&mid);

    return (1);
}
