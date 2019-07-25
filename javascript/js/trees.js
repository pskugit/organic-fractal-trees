function setup() {
	createCanvas(900,800)
}

function draw() {
	//initialization parameters
	var minlen = 5
	var stemsize = 100
	background(255);
	stroke(120, 80, 90)
	translate(width/2,height)
	angle = TWO_PI*0.06
	//draws the whole tree by recursively calling branch
	branch(stemsize, 1, minlen)
}

function branch(len, level, minlen){
	if(len > minlen){
		//define branch properties
		rlength = random() * len + len / 2
		rlength = random() * len * 2   + len / 4
		rangle = random()*TWO_PI*0.03+TWO_PI*0.03
		strokeWeight(2*len/(level+10))
		stroke(30, 210*(minlen/len), 80, 255);ramount = random()*100
		rside = random()*100
		if (rside>50) {
			rside=1
		} else{
			rside=-1
		}
		
		//check if root (it gets bonus width)
		if(level==1){
			line(0, 0, 0, -rlength*1.5);
			translate(0,-rlength*1.5);

		} else {
			line(0, 0, 0, -rlength);
			translate(0,-rlength);
		}
		scale = 0.78
		//create branches through recursive calls with a scaling factor
		//first branch
		push()
		rotate(rangle);
		branch(len*scale, level+1, minlen);
		pop()
		//second branch
		push()
		rotate(-rangle);
		branch(len*scale, level+1, minlen);
		pop()
		//third branch
		if(ramount>0.5){
			push()
			rotate(rside*2.5*rangle);
			branch(len*scale, level+1, minlen);
			pop()
		}		
	}
	noLoop()
}

//on click a new tree is created
function mouseClicked(){
	loop()
}

