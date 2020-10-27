#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
/**
 * infinite_while - Infinite loop with 1min of delay
 *
 * Return: 0
 *
 **/
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - Entry point
 *
 * Return: Always return 0
 *
 **/
int main(void)
{
	pid_t pid;
	int x;

	for (x = 0; x < 5; x++)
	{
		pid = fork();
		if (pid > 0)
		{
			printf("Zombie process created, PID: %d\n", pid);
		}
		else if (pid == 0)
		{
			exit(0);
		}
	}
	infinite_while();
	return (0);
}
