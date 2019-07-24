
//var slider;
var fr

function setup() {
	createCanvas(900,800)
	fr = createP('')
	//slider = createSlider(0, TWO_PI, PI, 0.1)
	//randomSeed(4)

	//button = createButton('new');
	//button.position(width/2, 30);
	//button.mousePressed(repeat);

}

function draw() {
	var minlen = 5
	var stemsize = 100


	background(255);
	stroke(120, 80, 90)
	translate(width/2,height)

	//angle = slider.value()
	angle = TWO_PI*0.06
	branch(stemsize, 1, minlen)
	//fr.html(frameRate())



}

function branch(len, level, minlen){

	if(len > minlen){
	
		rlength = random()*len   +     len/2
		rlength = random()*len*2   +     len/4
		rangle = random()*TWO_PI*0.03+TWO_PI*0.03
		ramount = random()*100
		rside = random()*100
		if (rside>50) {
			rside=1
		} else{
			rside=-1
		}

		scale = 0.78
		strokeWeight(2*len/(level+10))


		stroke(30, 210*(minlen/len), 80, 255);

		if(level==1){
			line(0, 0, 0, -rlength*1.5);
			translate(0,-rlength*1.5);

		} else {
			line(0, 0, 0, -rlength);
			translate(0,-rlength);
		}


		
		
		//create branches
		push()
		rotate(rangle);
		branch(len*scale, level+1, minlen);
		pop()

		push()
		rotate(-rangle);
		branch(len*scale, level+1, minlen);
		pop()

		if(ramount>0.5){
			push()
			rotate(rside*2.5*rangle);
			branch(len*scale, level+1, minlen);
			pop()
		}
			
	}
	

	noLoop()
	
	
}


function mouseClicked(){
	loop()
}

