// gcc 4.7.2 +
// gcc -std=gnu99 -Wall -g -o Exc_2 Exc_2.c -lpthread

#include <stdio.h>
#include <pthread.h>

void* func1();
void* func2();

int i = 0;

int main()
{
	pthread_mutex_t mtx;
	pthread_t thread_1, thread_2;
	
	pthread_mutex_init(&mtx, NULL); /* Initialize mutex */
	
	pthread_create(&thread_1, NULL, func1, NULL);
	pthread_create(&thread_2, NULL, func2, NULL);
	
	pthread_join(thread_1, NULL);
	pthread_join(thread_2, NULL);
	
    printf("%d\n", i);
    return 0;
}

void* func1(){
	int j = 0;
	while(j<1000000)
	{
		pthread_mutex_lock(&mtx)
		i++;
		pthread_mutex_unlock(&mtx)
		j++;
	}
	return NULL;
}

void* func2(){
	int j = 0;
	while(j<1000001)
	{
		pthread_mutex_lock(&mtx)
		i--;
		pthread_mutex_unlock(&mtx)
		j++;
	}
	return NULL;
}
