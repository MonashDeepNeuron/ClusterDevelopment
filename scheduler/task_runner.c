#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char command[100];
    char output[1000];
    char filename[100];

    // Get the command to run
    printf("Enter the command to run: ");
    fgets(command, sizeof(command), stdin);

    printf("%s", command);


    // Get the filename to append output to
    printf("Enter the filename to append output to: ");
    fgets(filename, sizeof(filename), stdin);

    // Remove newline characters from command and filename
    strtok(command, "\n");
    strtok(filename, "\n");

    // Open the file in append mode
    FILE *fp;
    fp = fopen(filename, "a");

    // Run the command and capture the output
    FILE *cmd;
    cmd = popen("ls -l", "r");

    while ( fgets( output, sizeof output, cmd))

  {

    fprintf(fp, "%s", output);

  }



    // Write the output to the file
    

    // Close the file and command
    fclose(fp);
    pclose(cmd);

    return 0;
}
