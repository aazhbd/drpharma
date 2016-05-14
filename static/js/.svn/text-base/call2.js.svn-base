//alert( 'This is call.js' );

var parameters = new GetParameters( window.location.search );
var sourceIP

if(typeof(String.prototype.trim) === "undefined")
{
    String.prototype.trim = function()
    {
        return String(this).replace(/^\s+|\s+$/g, '');
    };
}

function GetParameters( querystring )
{
	if ( querystring == '' )
		return;

	var parameterstring = unescape( querystring );
	parameterstring = parameterstring.slice( 1 );
	var pairs = parameterstring.split( '&' );

	for ( var i=0; i<pairs.length; i++ )
	{
		var name = pairs[i].substring ( 0, pairs[i].indexOf( '=' ) );
		var value = pairs[i].substring( pairs[i].indexOf( '=' ) + 1, pairs[i].length );
		this[name] = value;
	}
}

function StatusLine(state_text) {
    var create=false;
    var divTag = document.getElementById('state-line-tel');
    
    if (! (document.getElementById('state-line-tel')) )
    {
        divTag = document.createElement("div");
        create=true;
    }
    
    divTag.id = "state-line-tel";
    divTag.style.margin = "0px";
    divTag.style.position ="fixed";
    divTag.style.top = "0px";
    divTag.style.right = "0px";
    divTag.style.backgroundColor = "lightgray";
    divTag.style.display = "block"
    divTag.innerHTML = state_text;
    if ( create )
        document.body.appendChild(divTag);
}


function Call( destination )
{
    if ( 'phone_ip' in parameters )
    {
        sourceIP=parameters['phone_ip']
    }

    if ( destination == '' )
    {
        alert( 'Ich weiß nicht, welche Telefonnummer ich wählen soll!' );
        return;
    }

    var url = 'http://'+location.host+'/javascript/call.php?do=dial&phone-ip=' + sourceIP + '&number=' + destination;
    //alert(url)
    var TELxmlhttp = null;
    // Mozilla
    if (window.XMLHttpRequest) {
        TELxmlhttp = new XMLHttpRequest();
    }
    // IE
    else if (window.ActiveXObject) {
        TELxmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
    }
    StatusLine(sourceIP+': dialing '+destination);
    TELxmlhttp.open("GET", url , true);
    TELxmlhttp.onreadystatechange = function() {
        if(TELxmlhttp.readyState == 4 && xmlhttp.status == 200) {
            StatusLine('');
        }

    }
    TELxmlhttp.send(null);
}


function scall(e) {
        if (!e) var e = window.event;
        if (e.target.title == "") Call(e.target.innerHTML.replace(/-/g,""));
        else Call(e.target.title.replace(/-/g,""))
        return;
}

var xmlhttp = null;
if (window.XMLHttpRequest) {                        // Mozilla
    xmlhttp = new XMLHttpRequest();
}
else if (window.ActiveXObject) {                    // IE
    xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");
}

xmlhttp.open("GET", '/javascript/rdns.php', true);
xmlhttp.onreadystatechange = function() {
    if(xmlhttp.readyState == 4 && xmlhttp.status == 200) {
        sourceIP = 'tel-'+xmlhttp.responseText.trim();
    }
}
xmlhttp.send(null);

