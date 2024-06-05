#include <stdio.h>
#include <wait.h>
#include <sys/types.h>
#include <unistd.h>

/**
 * infinite_while - infinite loop.
 *
 * Return: 0
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
 * main - Creates 5 zombie processes.
 *
 * Return: 0 on Success.
*/
int main(void)
{
	pid_t pid;
	size_t i;

	for (i = 0; i < 5; i++)
	{
		pid = fork();
		if (pid == 0)
		{
			printf("Zombie process created, PID: %d\n", getpid());
			return (0);
		}
		else
			continue;
	}
	infinite_while();
	return (0);
}
