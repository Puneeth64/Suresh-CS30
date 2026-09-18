  /* Puneeth Suresh 2107296@gscs.ca Assignement 4 */
function setup() {
  
  createCanvas(1000,1000);
      
      /* Calls the function to draw a square, with the corner on 50,50*/
    draw_fixed_square();
    
    /* calls the draw_circle function, and the params being (x,y,d)*/
    draw_circle(200, 200, 50);
    
    /*Calls the draw stacked circles function, and the params are (x,y)*/
    draw_concentric_circles(500,500);
}

  /* Defines the function to draw a square*/
function draw_fixed_square(){
    /*First line goes fron bottom left to top left*/
    line(50,50,50,100);
    /*2nd line goes from top left to top right */
    line(50,100,100,100);
    /*3rd line goes from top right to bottom right*/
    line(100,100,100,50);
    /*Final line goes from bottom left to bottom right*/
    line(50,50,100,50);

}

  /*defines the draw a circle function*/
function draw_circle(x, y, d){
    /*Takes the x and y coords, and makes the diameter the height and width*/
    ellipse(x, y, d, d);
}

  /*defines the draw a concentric circle function*/
  function draw_concentric_circles(x,y){
    /*Creates a circle centered on the provided x and y coords, and a fixed radius of 90*/
   ellipse(x,y, 180, 180); 
   /*Now the radius is 60*/
   ellipse(x,y, 120,120);
   /*Finally, it is 30*/
   ellipse(x, y, 60, 60);
  }

function draw() {


}
