#inlude "lists.h"
/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to be checked
 * Rturn: 1 if the list has a cycle, 0 if it does not
 */
int check_cycle(listint_t *list){
	listint_t slow*  = list;
	list *fast = list;

	while (slow != NULL && fast->next != NULL){
		slow = slow->next;
		fast = slow->next->next;

		if (slow == fast){
			return (1);
	}
	return (0);

}
