#include <stdio.h>

// typedef

int main(void) {
    char *myCats[] = {"Cookie", "Luna", "Lucy", "Lotus", "Coconut", "Father of 20"};
    size_t catsCount = sizeof(myCats) / sizeof(myCats[0]);

    printf("You had %zu cats!\n", catsCount);

    for (int i = 0; i < catsCount; i++)
    {
        printf("%s\n", myCats[i]);
    }
}