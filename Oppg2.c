#include <pthread.h>
#include <stdio.h>

int i = 0;
int N = 1000000;

// Note the return type: void*
void* Inkrementer(){
    for (int j = 0; j < N; j++)
    	i++;
    return NULL;
}

void* Dekrementer(){
    for (int j = 0; j < N; j++)
    	i--;
    return NULL;
}



int main(){
    pthread_t someThread;
    pthread_t someThread2;
    pthread_create(&someThread, NULL, Inkrementer, NULL);
    pthread_create(&someThread2, NULL, Dekrementer, NULL);
    
    pthread_join(someThread, NULL);
    pthread_join(someThread2, NULL);
    printf("%d\n", i);
    return 0;
    
}

