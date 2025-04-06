#include <stdio.h>
#include <stdlib.h>
#include <string.h>


#define MAX_TASKS 100


typedef struct {
    char description[100];
    int completed;
} Task;


void add_task(Task tasks[], int *count, const char *description) {
    if (*count >= MAX_TASKS) {
        printf("Cannot add more tasks. Maximum limit reached.\n");
        return;
    }
    snprintf(tasks[*count].description, sizeof(tasks[*count].description), "%s", description);
    tasks[*count].completed = 0;
    (*count)++;
}


void display_tasks(Task tasks[], int count) {
    if (count == 0) {
        printf("No tasks available.\n");
        return;
    }
    for (int i = 0; i < count; i++) {
        printf("%d. %s [%s]\n", i + 1, tasks[i].description,
               tasks[i].completed ? "Completed" : "Pending");
    }
}


void display_task_list(Task tasks[], int count) {
    if (count == 0) {
        printf("No tasks available.\n");
        return;
    }
    for (int i = 0; i < count; i++) {
        printf("%d. %s\n", i + 1, tasks[i].description);
    }
}


void complete_task(Task tasks[], int *count, int task_number) {
    if (task_number <= 0 || task_number > *count) {
        printf("Invalid task number.\n");
        return;
    }
    tasks[task_number - 1].completed = 1;
    printf("Task marked as completed.\n");
}


void remove_task(Task tasks[], int *count, int task_number) {
    if (task_number <= 0 || task_number > *count) {
        printf("Invalid task number.\n");
        return;
    }
    for (int i = task_number - 1; i < *count - 1; i++) {
        tasks[i] = tasks[i + 1];
    }
    (*count)--;
    printf("Task removed successfully.\n");
}


void handle_help() {
    printf("\nTo-Do List Application CLI Help\n");
    printf("--------------------------------\n");
    printf("add <description>      - Adds a new task with the given description.\n");
    printf("list                   - Lists all tasks.\n");
    printf("--list                 - Lists only the task descriptoins.\n");
    printf("complete <task_number> - Marks the specified task as completed.\n");
    printf("remove <task_number>   - Removes the specified task.\n");
    printf("exit                   - Exits the application.\n");
}


void handle_command(Task tasks[], int *count, const char *command) {
    if (strncmp(command, "add", 3) == 0 && strlen(command) > 4) {
        add_task(tasks, count, command + 4);
	} else if (strcmp(command, "list") == 0 || strcmp(command, "--list") == 0) {
        if (strcmp(command, "list") == 0) {
            display_tasks(tasks, *count);
        } else if (strcmp(command, "--list") == 0) {
            display_task_list(tasks, *count);
        }

    } else if (strncmp(command, "complete", 8) == 0 && strlen(command) > 9) {
        int task_number = atoi(command + 9);
        complete_task(tasks, count, task_number);
    } else if (strncmp(command, "remove", 6) == 0 && strlen(command) > 7) {
        int task_number = atoi(command + 7);
        remove_task(tasks, count, task_number);
    } else if (strcmp(command, "exit") == 0) {
        printf("Exiting the application. Goodbye!\n");
        exit(0);
    } else if (strcmp(command, "--help") == 0 || strcmp(command, "help") == 0) {
        handle_help();
    } else {
        printf("Unknown command. Try 'help' for a list of commands.\n");
    }
}


int main() {
    Task tasks[MAX_TASKS];
    int count = 0;
    char input[256];

    while (1) {
        printf("$ ");
        if (fgets(input, sizeof(input), stdin) == NULL) {
        	// Handle error or end-of-file
        	printf("Error reading input.\n");
        	exit(1);
		}

        // Remove newline character if present
        size_t len = strlen(input);
        if (len > 0 && input[len - 1] == '\n') {
            input[len - 1] = '\0';
        }
        handle_command(tasks, &count, input);
    }

    return 0;
}
