#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#define BUFFER_SIZE 1024

int main() 
{
	char command[BUFFER_SIZE];
	char *args[10];

	while (1)
	{
		printf("SimpleShell> ");

        
        	if (fgets(command, BUFFER_SIZE, stdin) == NULL) 
		{
           		 break; 
        	}

		if (strncmp(command, "exit", 4) == 0) 
		{
            		break;
        	}
		/*
		 *eger bu hisseye qeder olan hisseleri anlamirsizsa, meslehet gorulur ki,1-main.c file-na kecid edesiz
		 *
		 */

		//Davam edek ^_^
		/*
		 *fgets ile aldigimiz her bir komandanin sonuna \n (abzas) elave olunur
		 *buna gorede biz bunu strcspn ile silirik
		 *eslinde \n olan indeks yerini \0(null terminated ile evezleyirik)
		 */
        	command[strcspn(command, "\n")] = 0;

		int i = 0;

		/*
		 *Gerek linux-da komanda mentiqini anlayaq 
		 *meselen , ls -l komandasinda 
		 *burada ls (command) -l (flag | option) sayilir
		 *bizim shellimizde bunu etmek ucun strtok istifade edirik ki 
		 *eger ls -l yazsq o zaman ayirsin
		 *
		 */
		args[i] = strtok(command, " ");


		while (args[i] != NULL) 
		{
			i++;
			/*
			 *komandamiz tutaq ki: ls -l => kimidir
			 *bu hhissede deyirik ki eger sonuna qeder yoxlamasini isteyirik 
			 *ve netice olaraq bizde 
			 *args[0]= ls
			 *args[1]= -l
			 *args[2]=NUll 
			 *olacaq
			 */
			args[i] = strtok(NULL, " ");
		}
		/*
		 *Proqram evvelinde unistd.h kitabxanasi fork,execvp ucun
		 *pid_t ucun sys\types.h
		 *wait.h  da wait ucun daxil edilib
		 */

		/*
		 *biz proqramla bir yeni child proses yaratmasini isteyirik.
		 *child proses olub olmadigini ise pid == 0 ile yoxlayiriq
		 */
		pid_t pid = fork();
		if (pid == 0) 
		{
			/*
			 *komandani ishe salan execvp -dir .
			 *eger komand ishe duserse (/bin/....) parent process gozleyer 
			 *eks halda perror yazdigimizi bize geriqaytarar
			 *
			 */
			if (execvp(args[0], args) == -1)
			{
				perror("Komanda ishe dusmedi(Sebeb: execvp)....±");
			}
			/*
			 *hemin komand ucun proses sonlanar
			 */
			exit(EXIT_FAILURE);
		} 
		
		/*
		 *eger child pid <0 olarsas fork xetasi vermelidir
		 */
		else if (pid < 0) 
		{ 	
			perror("Komanda ishe dusmedi (Sebeb: fork)");
		}	 
	
		else 
		{  
			/*
			 *eks halda yeni pid ne 0 ve ne de pid<0 olmadigindan demekki 
			 *pid bizde pid> 0 olacaq.
			 *bu ise o demekdir ki parent process bizde gozlemelidir
			 */
			wait(NULL);
		}
	}
	return 0;
}

