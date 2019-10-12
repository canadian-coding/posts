/** A demo of the processing language.
@author Canadian Coding
@since Processing V3.5.3
@date 14-10-19

This file is meant to do a few things:
1. Demonstrate void and setup
2. Show variables, for loops and functions
3. Draw 3 snowman.

To run this file hit the play icon in the top left*/

/**A function that runs once, intended to 'set up' your project (hence the name)
@see https://processing.org/reference/setup_.html
*/
void setup(){
  size(400,400);                                                        // Sets up a 500,500 canvas; SEE https://processing.org/reference/size_.html
  println("Do you wanna build a snowman?\nCome on let's go and play!"); // Prints a string to the console; SEE https://processing.org/reference/println_.html
  noLoop();                                                             // only draw stuff once; SEE https://processing.org/reference/noLoop_.html
  background(50);                                                       // Set background colour; SEE https://processing.org/reference/background_.html
  
  // Simplified manual version of drawing 3 snowmen
  // drawSnowman(80, 100);
  // drawSnowman(320, 100);
  // drawSnowman(200, 200);
  
   // The for loop version of drawing 3 snowmen
   int snowmanY;                                                        // Variable to keep track of the snowmen's y position
   for(int counter=0;counter<=2;counter++){                             // Draw 3 snowmen while offsetting the x position by 120 each time
   int snowmanX = 80;                                                   // The x position of where to draw each snowman in the loop
   if ((counter % 2) == 0){                                             // Set snowmanY based on if the counter is even or odd
        snowmanY = 100;                                                 // If counter is even set snowmanY to 100
        } else {
        snowmanY = 200;                                                 // If counter is odd set snowmanY to 200
        }
      drawSnowman(snowmanX+=(counter*120),snowmanY);                    // Draw the current iterations snowman
    } 
}

/**Not used in this example, but it's a function that runs over and over again (like a main loop). Useful for animations.
@see https://processing.org/reference/draw_.html*/
void draw(){}

/** Draws a full snowman (carrot nose included)
@param xPos The x position of where you would like to draw the snowman
@param yPos The y position of where you would like to draw the snowman*/
void drawSnowman(int xPos, int yPos) {
  drawHead(xPos, yPos);            // Draws the snowman's head
  fill(255);                       // Fill snowman peices white
  ellipse(xPos, yPos+60, 70, 70);  // Draw second body peice (offset by 60 pixels down)
  ellipse(xPos, yPos+140, 90, 90); // Draw bottom body peice (offset by 140 pixels down)
}

/**Draws the head of the snowman; An ellipse with two eyes (black circles) and a carrot nose (orange triangle)
@param xPos The x position of where you would like to draw the snowman head
@param yPos The y position of where you would like to draw the snowman head*/
void drawHead(int xPos, int yPos){
  fill(255);                                           // Fill snowman head white
  ellipse(xPos, yPos, 50, 50);                         // Draw head peice
  
  fill(0);                                             // Fill eyes black
  rect(xPos-13, yPos-15, 5, 5);                        // Draw left eye
  rect(xPos+7, yPos-15, 5, 5);                         // Draw right eye
  
  fill(255, 127, 80);                                  // Fill Carrot orange
  triangle(xPos-5, yPos, xPos+5, yPos, xPos, yPos+15); // Draw Carrot
}
