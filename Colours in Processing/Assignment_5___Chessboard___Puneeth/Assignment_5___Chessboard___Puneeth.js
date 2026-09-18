// Puneeth Suresh
//2107296@gscs.ca
//Assignment 5 - Chessboard
function setup() {
  createCanvas(200,200);

  for (let y = 0; y <= 150; y += 50) { //y starts out as 0, until y is less than or equal to 150. y increases by 50 each loop (since there is 4 layers : 0, 50, 100 and 150)
    for (let x = 0; x <= 100; x += 100) { //additionally, x starts as 0, adds 100 each loop, ends when x is 100 (since you only need to repeat the x axis twice to get 4 squares)
      if (y % 100 === 0) { //if the y value is 100 or 0, first square is white
        whiteBlackSquare(x, y); //calls function to place white square first then black
      } 
      else { //if its not 0 or 150 (aka 50 or 100), it starts with a black square
        blackWhiteSquare(x, y);
      }
    }
  }
}

function whiteBlackSquare(x,y){ // This function is called when you want to start with a white square, then go to black
  let x2= x + 50 //adds 50 to x in order push the 2nd square to be 50px away
  fill(255); //colour = white
  square(x,y, 50); // creates the first square with the x and y params, and size of 50
  fill(0); //colour = black
  square(x2,y, 50); //uses the x2 var defined above (so x+50px), but same y val so it's in the same line. Also 50 px in size
}

function blackWhiteSquare(x,y){ // This function is called when you want to start with a black square, then switch to white
  let x2 = x + 50; //same reason as above
  fill(0); //colour = black this time   
  square(x, y, 50);
  fill(255); //this time, the colour is white
  square(x2, y, 50);
}
function draw() {

}
