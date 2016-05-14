
function dataRow(_name,_color,_values,_type)
{
	this.name = _name;
    this.color = _color;
    this.values = _values;
    this.type = _type;
}

function ISAPlot(canvasID) {
	this.canvas = document.getElementById(canvasID);
    this.context = this.canvas.getContext('2d');
    this.context.font = "7pt Calibri";
    this.Rows = new Array();
    this.XscaleValues = new Array();
    
    ISAPlot.prototype.addRow = function(name,color,values) {
    	var newRow=new dataRow(name,color,values,'DataRow');
    	this.Rows.push(newRow);
    }
    
    ISAPlot.prototype.addMarker = function(name,color,values) {
    	var newRow=new dataRow(name,color,values,'Marker');
    	this.Rows.push(newRow);
    }
    
    ISAPlot.prototype.addXScaleValues = function(XScaleValues) {
    	this.XscaleValues=XScaleValues;
    }
    
    ISAPlot.prototype._drawScales = function (XScale,YScale, scalei) {
    	var len = this.XscaleValues.length;
    	var StartX = 10;
    	var StartY = 10;
    	
    	var width=this.canvas.width;
    	var height=this.canvas.height;
    	
    	nscale = scalei;
    	//alert(nscale);
    	
    	//x-Raster
    	this.context.strokeStyle = '#999';
    	this.context.beginPath();
    	
    	for(var i=1; i<len; i++) {
    		this.context.moveTo(i*XScale+StartX+45,height-StartY-45);
    		//this.context.lineTo(i*XScale+StartX+45,10);
    	}
    	
    	this.context.fill();
    	this.context.stroke();
    	
    	this.context.strokeStyle = '#555';
    	this.context.beginPath();
    	
    	//x-Achse
    	this.context.moveTo(StartX+45,height-StartY-45);
    	this.context.lineTo((len-1)*XScale+StartX+45,height-StartY-45);
    	
    	//y-Ache
    	this.context.moveTo(StartX+45,height-StartY-45);
    	this.context.lineTo(StartX+45,10);
    	this.context.fill();
    	this.context.stroke();
    	
    	//x-Achsenbeschriftung
    	var angle=-45;
    	this.context.save();
    	this.context.rotate(angle * Math.PI/180);
    	this.context.beginPath();
    	this.context.strokeStyle = '#555';
    	this.context.fillStyle = '#00f';
    	this.context.textBaseline="bottom";
    	
    	//for(var i=0; i<len; i++) {
    	i = 0;
    	
    	str = this.XscaleValues[i] + " 23:15:00";
    	tmp = new Date(str).getDay();
    	
    	if(len > 45) {
    		while(i < len) {
    			str = this.XscaleValues[i] + " 23:15:00";
    			tmp = new Date(str).getDay();
    			if(tmp == 1) break;
    			i++;
    		}
    		
    		interval = 7;
    	}
    	else interval = 1;
    	/*
    	 interval = (len < 45) ? 1 : 7;
    	 */
    	while (i < len) {
    		this.context.fillText(
    			this.XscaleValues[i],
    			(StartX-10)*Math.sqrt(1/2)-((height-StartY)+10)*Math.sqrt(1/2)+i*Math.sqrt(XScale*XScale/2),
    			(StartX-10)*Math.sqrt(1/2)+((height-StartY)+10)*Math.sqrt(1/2)+i*Math.sqrt(XScale*XScale/2)
    		);
    		
    		this.context.moveTo(
    			(StartX-10)*Math.sqrt(1/2)-((height-StartY)+10)*Math.sqrt(1/2)+i*Math.sqrt(XScale*XScale/2),
    			(StartX-10)*Math.sqrt(1/2)+((height-StartY)+10)*Math.sqrt(1/2)+i*Math.sqrt(XScale*XScale/2)
    		);
    		
    		this.context.lineTo(
    			(StartX+45)*Math.sqrt(1/2)-((height-StartY)-45)*Math.sqrt(1/2)+i*Math.sqrt(XScale*XScale/2),
    			(StartX+45)*Math.sqrt(1/2)+((height-StartY)-45)*Math.sqrt(1/2)+i*Math.sqrt(XScale*XScale/2)
    		);
    		
    		i += interval;
    	}
    	
    	this.context.fill();
    	this.context.stroke();
    	this.context.restore();
    	
    	i = 0;
    	while(i < len) {
    		str = this.XscaleValues[i] + " 23:15:00";
    		tmp = new Date(str).getDay();
    		
    		if(tmp == 1) {
    			this.context.moveTo(StartX+45+i*XScale,height-StartY-45);
    			this.context.lineTo(StartX+45+i*XScale,10);
    		}
    		i += 1;
    	}
    	
    	for(j = 1; j < nscale; j++) {
    		this.context.fillText(j + "%",StartX+25 , height-StartY-45 - j*YScale);
    		this.context.moveTo(StartX+45 , height-StartY-45 - j*YScale);
    		this.context.lineTo((len-1)*XScale+StartX+45 , height-StartY-45 - j*YScale);
    	}
    	
    	this.context.stroke();
    	
    	//y-Achsenbeschriftung
    	var YLength = height-StartY-45-10;
    	var maxYLabel = Math.round(YLength/15);
    	var maxYValue = YLength/YScale;
    	//ToDO: Coming soon....
    	
    	
    	//xMarker
    	for(var i=0; i<this.Rows.length; i++) {
    		if (this.Rows[i].type=='Marker') {
	    		this.context.strokeStyle = this.Rows[i].color;
	    		this.context.beginPath();
	    		this.context.moveTo(StartX+45,height-StartY-45-YScale*this.Rows[i].values);
	    		this.context.lineTo((len-1)*XScale+StartX+45,height-StartY-45-YScale*this.Rows[i].values);
	    		this.context.fill();
	    		this.context.stroke();
	    	}
	    }
	}
    
    
    ISAPlot.prototype._drawGraph = function (count,X1,Y1,Xscale,Yscale) {
          var name=this.Rows[count].name;
          var color=this.Rows[count].color;
          var values=this.Rows[count].values;
          
          this.context.strokeStyle = color; 
          this.context.fillStyle = color;
          this.context.lineWidth=1;
 
          this.context.beginPath();
          this.context.fillText(name,this.canvas.width-90,(15*count)+30);
          
          var len=values.length;
          for(var i = 0; i < len; i++) {
              if (values[i] != "undef") {
                  this.context.lineTo(i * Xscale + X1, this.canvas.height - (values[i] * Yscale) - Y1);
                  
                  if (this.Rows[count].type=='DataRow') {
                      this.context.fillText( values[i] , i * Xscale - 5 + X1 , this.canvas.height-(values[i]*Yscale)+20-Y1);
                  }
              }
          }
          this.context.stroke();
          this.context.closePath();
          
          if (this.Rows[count].type=='DataRow') {
              for(var i=0; i<len; i++) {
                  if (values[i] != "undef") {
                      this.context.beginPath();  
                      this.context.arc(i * Xscale + X1, this.canvas.height - (values[i] * Yscale) - Y1, 2, 0, Math.PI*2, true);
                      this.context.fill();
                      this.context.closePath();
                  }
              }
          }
    }

	ISAPlot.prototype.draw = function(si) {
		var len = this.Rows.length;
		var maximumY = 0;
		var maximumX=this.XscaleValues.length;
		var Xscale=0;
		var Yscale=0;
		
		for(var i = 0; i < len; i++)
		{
			for(var j=0; j < this.Rows[i].values.length; j++)
			{
				if(maximumY < this.Rows[i].values[j])
				{
					maximumY = this.Rows[i].values[j];
				}
			}
		}
		
		//alert(maximumY);
		
		//maximumY = maxY;
		
		//alert(si);
		maximumY = (si == 0) ? 5 : maximumY;
		
		//alert("si = " + si + " maxy = " + maximumY);
		
		Xscale = Math.round((this.canvas.width-155)/maximumX);
		Yscale = Math.round(((this.canvas.height-75)/maximumY));
		
		//alert(Yscale);
		
		//Yscale = Math.round(Yscale*0.5);
		
		this._drawScales(Xscale, Yscale, maximumY);
		
		for(var i = 0; i < len; i++)
		{
			this._drawGraph(i, 55, 55, Xscale, Yscale);
		}
	}
}
