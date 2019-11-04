/**Used to demo the C language, demonstrates: functions, variables, imports, string formatting etc. */

#include <stdio.h> // Used to print to stdin and stdout
#include <math.h>  // Contains the value of PI as M_PI; Used in area_of_circle function

/** Calculates the area of a circle and returns it based on radius
* 
* Parameters
* ----------
* radius: 
*		  The radius of the circle you want the area of.
* 
* Returns
* -------
* The area of a circle with the given radius as an int
*/
int area_of_circle(int radius){
  int area = M_PI * (radius*radius); // pi times radius squared
  return area;
  }

/**Function that runs in the binary after compile.*/
int main(){
    int radius = 5; // Setup variable to be used in next format string
    printf("\nThe area of a circle with radius: %d is %d\n", radius, area_of_circle(radius));
    return 0;  // Causes the function to exit
    }
