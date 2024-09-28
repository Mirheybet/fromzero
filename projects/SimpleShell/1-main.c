#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFFER_SIZE 1024

int main(void) 
{
	/*
	 * komandalar ucun yaratdigimiz buferimiz 
	 * (1024 byte olacaq)
	 * Yeni 1024 character-li komanda adi ola biler
	 * normalda {ls(buferdeki uzunlugu 2 byte olacaq)}
	 */
	char command[BUFFER_SIZE];
	
	/*
	 *Normalda bir shell her zaman bizden komanda gozleyir 
	 *komanda deyerken nezerde tutdugum klaviaturadan olan inputdur (ls,cd,pwd,cp,mkdir) 
	 * bunu bizden gozleyerken mentiqi olaraq biz bir dovr aciriq ve deyirik ki 
	 *sonsuza qeder gozle
	 *eks hal ucun sertimizi vermisem
	 */
	while (1) 
	{
		//Sade print setri
		printf("SimpleShell> ");
		
		/*
		 *fgets - bizden inputu(command) oxuyur,olcusunu bilir(Buffer), bunu standart inputdan(klaviatura) oxuyur
		 *Null serti onun ucundur ki , xeta yaxod EOF olarsa , bizim TRUE olan dovrumuz sonlansin(break)
		 */
		if (fgets(command, BUFFER_SIZE, stdin) == NULL) 
		{
			break;
		}

		/*
		 *strncmp - n elemente gore iki stri muqayise edir: eger eynidirlerse 0,eks halda 0-dan ferqli
		 *biz commandda eger exit* yazsaq o zaman dovrumuz yene sonlanacaq(break)
		 */
		if (strncmp(command, "exit", 4) == 0) 
		{
			break;
		}

		/*
		 *eger yuxaridaki if-ler odemese comanda print olacaq
		 */
		printf("Command: %s", command);
		}

	return 0;
}
