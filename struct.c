#include <stdio.h>

int main(void) {
    char *myCats[] = {"Cookie", "Luna", "Lucy", "Lotus", "Coconut", "Father of 20"};
    size_t catsCount = sizeof(myCats) / sizeof(myCats[0]); // counts the array size "mathematically"

    printf("You had %zu cats!\n", catsCount);

    for (int i = 0; i < catsCount; i++)
    {
        printf("%s\n", myCats[i]);
    }
}