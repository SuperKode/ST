#include <stdio.h>
#include <pthread.h>

void* func1();
void* func2();

int i = 0;

int main()
{
	pthread_t thread_1, thread_2;
	
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
		i++;
		j++;
	}
	return NULL;
}

void* func2(){
	int j = 0;
	while(j<1000000)
	{
		i--;
		j++;
	}
	return NULL;
}
