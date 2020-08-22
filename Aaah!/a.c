#include<stdio.h>
#include<string.h>

int main(){
    char doctor[999];
    char marius[999];
    unsigned int len_doctor;
    unsigned int len_marius;

    scanf("%s", doctor);
    scanf("%s",marius);

    len_doctor = strlen(doctor);
    len_marius = strlen(marius);

    if(len_doctor >= len_marius){
        printf("go");
    }else{
        printf("no");
    }
    return 0;
}