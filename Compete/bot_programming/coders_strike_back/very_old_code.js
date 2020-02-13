/**
 * Auto-generated code below aims at helping you parse
 * the standard input according to the problem statement.
 **/

function d_to_r(angle){
    return angle*Math.PI/180;
}
function getRad(deg){ //return radiant
    return (deg * Math.PI / 180) < 0 ? 2*Math.PI+(deg * Math.PI / 180) : (deg * Math.PI / 180) ;
}
function new_angle(angle1, angle2){
    return (angle1+angle2) < 0 ? 360+(angle1+angle2) : (angle1+angle2)%360;   
}
function getAngle(x1,y1,x2,y2){
    return Math.round((getDeg(Math.atan2(y2 - y1, x2 - x1)))%360);
}
function getDeg(rad){
    return (rad * 180 / Math.PI) < 0 ? 360+(rad * 180 / Math.PI) : (rad * 180 / Math.PI);
}
function getCirclePos(x1,y1,angle,radius){
    var pos = {};
    pos.x = Math.round(x1+radius*Math.cos(getRad(angle)));
    pos.y = Math.round(y1+radius*Math.sin(getRad(angle)));
    return pos;
}

// game loopx1
var start_bool = true;
var zone = 600;
var b_func = 30; // min speed of range
var speed = 100;
while (true) {

    

    var inputs = readline().split(' ');
    var x = parseInt(inputs[0]);
    var y = parseInt(inputs[1]);
    var nextCheckpointX = parseInt(inputs[2]); // x position of the next check point
    var nextCheckpointY = parseInt(inputs[3]); // y position of the next check point
    var nextCheckpointDist = parseInt(inputs[4]); // distance to the next checkpoint
    var nextCheckpointAngle = parseInt(inputs[5]); // angle between your pod orientation and the direction of the next checkpoint
    var inputs = readline().split(' ');
    var opponentX = parseInt(inputs[0]);
    var opponentY = parseInt(inputs[1]);

    // Write an action using print()
    // To debug: printErr('Debug messages...');


    // You have to output the target position
    // followed by the power (0 <= thrust <= 100)
    // i.e.: "x y thrust"

        
        /*if(nextCheckpointDist > 7000 && nextCheckpointAngle < 10 && nextCheckpointAngle > -10){
            speed = "BOOST";   
        }*/
        if(nextCheckpointDist<zone){// && nextCheckpointAngle < 30 && nextCheckpointAngle > -30){  
            var a_func = (100 - b_func) / zone; //delta_y/delta_x
            speed = Math.round(a_func*nextCheckpointDist+b_func);
        }
        else if(nextCheckpointAngle > 20 || nextCheckpointAngle < -20){
            speed = Math.round(-0.0030864197530864  *(nextCheckpointAngle*nextCheckpointAngle)+100);
        }

        else{
            speed = 100;   
        }
        printErr('LA VITESSE = ' + speed);
        printErr('L\'ANGLE = ' + nextCheckpointAngle);
        
        
        
        printErr('distance' + nextCheckpointDist);
      //  else if(nextCheckpointAngle < -30){
          // speed = nextCheckpointAngle * 100 / 180;
      //  }
      
        var next_x = nextCheckpointX;
        var next_y = nextCheckpointY;
      /*  if(nextCheckpointAngle>0){
            var max_point =  new_angle(getAngle(x,y,nextCheckpointX,nextCheckpointY), 45);
            var newpos = getNewPos(nextCheckpointX,nextCheckpointY,max_point);
            next_x = newpos.x;
            next_y = newpos.y;
        }
        else if(nextCheckpointAngle<0){
            var max_point =  new_angle(getAngle(x,y,nextCheckpointX,nextCheckpointY), -45);
            var newpos = getNewPos(nextCheckpointX,nextCheckpointY,max_point);
            next_x = newpos.x;
            next_y = newpos.y;
        }*/

        if(start_bool == true){
         start_bool = false;
         speed = "BOOST";
 
         
         
         var angle = getAngle(opponentX,opponentY,nextCheckpointX,nextCheckpointY);
         printErr('angle' + angle);
         var pos = getCirclePos(opponentX,opponentY,angle,1400);
         next_x = pos.x;
         next_y = pos.y;
        }
      


    print(next_x + ' ' + next_y + ' ' + speed.toString());
}