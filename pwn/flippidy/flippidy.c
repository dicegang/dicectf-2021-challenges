#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>



typedef struct Bruh {
    char * menuitems[4];
    char bruh1[50];
    char bruh2[50];
    char bruh3[50];
    char bruh4[50];
} Bruh;


Bruh information = {
    .menuitems = {
        information.bruh1,
        information.bruh2,
        information.bruh3,
        information.bruh4,
    },
    .bruh1 = "----- Menu -----",
    .bruh2 = "1. Add to your notebook",
    .bruh3 = "2. Flip your notebook!",
    .bruh4 = "3. Exit"
};


int master_chunk_size;
void ** master_chunk_ptr;


void menu(){
    puts("\n");
    for(int i = 0; i < 4; ++i){
        puts(information.menuitems[i]);
    }
}


void welcome(){
    puts("---------- FLIPPIDYDIPPILF ----------");
    
    puts("In this very realistic scenario our protagonist (you!) finds himself in search of a notebook...");
    puts("That can flip itself!");
    puts("This notebook flips its pages very well. I hope it suits someone as powerful as you.\n\n");
    puts("Just give it the word, and the pages will reverse themselves!");
}


int get_integer(){
    char buf[20];
    memset(buf, 0, 20);
    if(fgets(buf, 20, stdin) == NULL) exit(0);
    
    int ret = atoi(buf);
    
    return ret;
}



void add_note(){
    int idx;
    printf("Index: ");
    idx = get_integer();
    
    if(!(idx >= 0) || !(idx < master_chunk_size)) {
        puts("Invalid index.");
        return;
    }
    
    master_chunk_ptr[idx] = malloc(0x30);
    
    printf("Content: ");
    
    fgets((char *)master_chunk_ptr[idx], 0x30, stdin);
}

void flip_notebook(){
    for(int i = 0; i <= master_chunk_size/2; i++){
        char a[0x40];
        char b[0x40];
        
        memset(a, 0, 0x40);
        memset(b, 0, 0x40);
        
        bool flag1 = false;
        bool flag2 = false;
        
        if (master_chunk_ptr[i] != NULL){
            strcpy(a, master_chunk_ptr[i]);
            free(master_chunk_ptr[i]);
            
        } else {
            flag1 = true;
        }
        
        
        if (master_chunk_ptr[master_chunk_size-i-1] != NULL){
            strcpy(b, master_chunk_ptr[master_chunk_size-i-1]);
            free(master_chunk_ptr[master_chunk_size-i-1]);
            
        } else {
            flag2 = true;
        }
        
        master_chunk_ptr[i] = NULL;
        master_chunk_ptr[master_chunk_size-i-1] = NULL;
        
        
        if(!flag1){
            master_chunk_ptr[master_chunk_size-i-1] = malloc(0x30);
            strcpy(master_chunk_ptr[master_chunk_size-i-1], a);
        } else {
            master_chunk_ptr[master_chunk_size-i-1] = NULL;
        }
        
        
        if(!flag2){
            master_chunk_ptr[i] = malloc(0x30);
            strcpy(master_chunk_ptr[i],  b);
            
        } else {
            master_chunk_ptr[i] = NULL;
        }
    };
    
}



int main(){
    setbuf(stdout, NULL);
    setbuf(stdin, NULL);
    setbuf(stderr, NULL);
    
    int choice;
    int note_counter;
    
    welcome();
    printf("%s", "To get started, first tell us how big your notebook will be: ");
    master_chunk_size = get_integer();
    
    master_chunk_ptr = malloc(8*master_chunk_size);
    
    memset(master_chunk_ptr, 0, 8*master_chunk_size);
    
    
    while(1){
        menu();
        
        printf(": ");
        choice = get_integer();
        
        switch(choice){
            case 1:
                add_note();
                break;
            case 2:
                flip_notebook();
                break;
            case 3:
                puts("Goodbye!");
                exit(0);
                break;
            default:
                puts("Invalid choice.");
                break;
        }
        
    }
    
}


