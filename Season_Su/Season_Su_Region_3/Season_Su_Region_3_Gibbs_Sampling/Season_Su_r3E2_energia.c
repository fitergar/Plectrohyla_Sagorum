# include <stdlib.h>
# include <stdio.h>
# include <math.h>
# include <string.h>
# include <time.h>
# include <sys/time.h>
# include <sys/resource.h>

FILE *fsal1;

int i;
int j;
int k;

int V[8401];
int N[8401][4];
int D[8401];
int X[8401];

double E=0;
double ES[2007839];

int Iter=0; // Contador total de iteraciones
int nSitios=8401;
int maxIter=239;

double T=0.2;
double g=0.05;
int L = 5;

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

void gibbs_sampler(){
  int i,j,k;
  int x;
  int dex;
  double a,EXP;
  int aux1,aux2;

  for(i=0;i<nSitios;i++){
   E+=Energia(i,X[i]);
  }
  ES[Iter]=E;

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
            E+=dex;
      	  }
      	  else{
      	    a = drand48();
      	    EXP = exp(-dex/T);
  		      if (a<EXP){
  	          X[i] = x;
              E+=dex;
  	        }
      	  }
        }//if(x!=X[i])
      }//if(D[i]!=0)
      Iter++;
      ES[Iter]=E;
    }//for(i=0;i<nSitios;i++)
  }
}

/***********************************************/

int main () {
  unsigned seed;
  time_t t;

  seed = (unsigned) time(&t);
  srand48(seed);

  fsal1 = fopen("../Season_Su_Region_3_Results/r3E2_energia.txt","w");

/************************************************/

  FILE* ptr = fopen("../Season_Su_Region_3_Data/r3E2_datos.txt","r");
    if (ptr==NULL){
      printf("No such datos file.\n");
      return 0;
    }
    for(i=0;i<nSitios;i++){
      fscanf(ptr,"%d %d %d",&i,&D[i],&X[i]);
    }
  fclose(ptr);

  FILE* ve = fopen("../../../Neighborhood _Structure/r3_vecinos.txt","r");
    if (ve==NULL){
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

  printf("Iter=%d\n",Iter);

  for (k=0;k<Iter+1;k++){
    fprintf(fsal1,"%3f",ES[k]);
    if(k%1==0) fprintf(fsal1,"\n");
  }

  fclose(fsal1);

/***********************************/

  return 0;
}
