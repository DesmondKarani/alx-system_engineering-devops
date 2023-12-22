#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/types.h>
/**
 * infinite_while - Runs an infinite loop to keep the program running
 *
 * Return: Always 0 (success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Creates 5 zombie processes
 *
 * Return: Always 0 (success)
 */
int main(void)
{
	pid_t pid;
	int i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			/* Child process */
			printf("Zombie process created, PID: %d\n", getpid());
			exit(0); /* Child exits immediately */
		}
	}

	/* Parent process */
	infinite_while();

	return (0);
}
