# include <stdlib.h>
# include <stdio.h>
# include <math.h>
# include <string.h>
# include <time.h>
# include <sys/time.h>
# include <sys/resource.h>

FILE *fsal1, *fsal2, *fsal3;

int i;
int j;
int k;
int V[13715];
int N[13715][4];
int D[13715];
int X[13715];
int Xs[13715];
float Xp[13715];

int nSitios=13715;
int maxIter=1000000;
double ultIter=10000;
int ES[1000000];
double T=0.2;
double g=0.06;
int L = 7;

/********************************************/

int Energia(int i, int x)
{
  int j, suma, factor, energia;
  suma = 0;
  for(j=0;j<V[i];j++){
    suma += (x-X[N[i][j]])*(x-X[N[i][j]]);
}
 factor = g*(D[i]*D[i])*x;
 energia = suma + factor;
 return(energia);
}

int EnergiaSistema()
{
  int i, enes;
  enes = 0;
  for(i=0;i<nSitios;i++){
    enes += Energia(i,X[i]);
  }
  return(enes);
}

/*********************************************/

void gibbs_sampler()
{
 int i,j,k;
 int x;
 int dex;
 double a,EXP;
 int aux1,aux2;

 for(k=1;k<maxIter+1;k++){
    for(i=0;i<nSitios;i++){
  	if(D[i]!=0){
    	     x =  (int)(lrand48()%L);
    	  if(x!=X[i]){
    	     aux1 = Energia(i,x) ;
    	     aux2 = Energia(i,X[i]);
    	     dex = aux1- aux2;
    	     if(dex<=0){
    	     	X[i] = x;
    	     }
    	     else{
    	     	a =  drand48();
    	        EXP =  exp(-dex/T );
		if (a<EXP){
	           X[i] = x;
	        }
    	     }
          }
       }
    }
		if(k>maxIter-ultIter){
			for(i=0;i<nSitios;i++){
		 Xs[i]+=X[i];
	 }
}
   ES[k]=EnergiaSistema();
 }
}

#define ARCHIVO "../Season_Su_Region_4_Results/r4E2gs"
/***********************************************/

/* int main () { */
/*   unsigned seed; */
/*   time_t t; */

/*   seed = (unsigned) time(&t); */
/*   srand48(seed); */

/*     fsal1 = fopen("../Season_Su_Region_4_Results/r4E2gs_x.txt","w"); */
/*     fsal2 = fopen("../Season_Su_Region_4_Results/r4E2gs_e.txt","w"); */
/*     fsal3 = fopen("../Season_Su_Region_4_Results/r4E2gs_p.txt","w"); */

int main (int argc, char *argv[]) {
  int R;
  char nomArch[300];
  unsigned seed;
  time_t t;


  seed = (unsigned) time(&t);
  srand48(seed);

  R = atoi(argv[1]);

  sprintf(nomArch,"%s_x%d.txt",ARCHIVO,R);
  fsal1 = fopen(nomArch,"w");
  //printf("\n Arch %s\n",nomArch); 

  sprintf(nomArch,"%s_e%d.txt",ARCHIVO,R);
  fsal2 = fopen(nomArch,"w");
  //printf("\n Arch %s\n",nomArch); 

  sprintf(nomArch,"%s_p%d.txt",ARCHIVO,R);
  fsal3 = fopen(nomArch,"w");

/************************************************/

  FILE* ptr = fopen("../Season_Su_Region_4_Data/r4E2_datos.txt","r");
      if (ptr==NULL)
      {
          printf("No such datos file.\n");
          return 0;
      }
      for(i=0;i<nSitios;i++){
      fscanf(ptr,"%d %d %d",&i,&D[i],&X[i]);
      }
  fclose(ptr);

  FILE* ve = fopen("../../../Neighborhood _Structure/r4_vecinos.txt","r");
      if (ve==NULL)
      {
          printf("No such vecinos file.\n");
          return 0;
      }
  	  for(i=0;i<nSitios;i++){
  	   fscanf(ve,"%d",&V[i]);
  		for(j=0;j<V[i];j++){
  		  fscanf(ve,"%7d",&N[i][j]);
  		}
      }
  fclose(ve);

/************************************/

  gibbs_sampler();

	for(i=0;i<nSitios;i++){
    Xp[i]=Xs[i]/ultIter;
	}

	int sumX=0;
	int sumXs=0;
	float sumXp=0;

	for(i=0;i<nSitios;i++){
		sumX+=X[i];
	}

	for(i=0;i<nSitios;i++){
		sumXs+=Xs[i];
	}

	for(i=0;i<nSitios;i++){
		sumXp+=Xp[i];
	}

	printf("%d\n",sumX);
  printf("%d\n",sumXs);
	printf("%f\n",sumXp);

  printf("%d\n",ES[maxIter-1]);

/***********************************/

for(i=0;i<nSitios;i++){
   fprintf(fsal1,"%3d",X[i]);
   if(i%1==0) fprintf(fsal1,"\n");
 }

 for (k=1;k<maxIter+1;k++){
   fprintf(fsal2,"%6d",ES[k]);
   if(k%1==0) fprintf(fsal2,"\n");
 }

 for(j=0;j<nSitios;j++){
    fprintf(fsal3,"%3f",Xp[j]);
    if(j%1==0) fprintf(fsal3,"\n");
  }
 fclose(fsal3);
 fclose(fsal2);
 fclose(fsal1);

/***********************************/

   return 0;
}
