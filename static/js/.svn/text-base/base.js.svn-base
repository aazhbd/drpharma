
var timerId = 0;
var viewStr = "";
var urlStr = "";
var sortStr = "";
var directionStr = "";
var chain = null;

function clearSearchInput(view, url) {
    s = document.getElementById('SearchInput');
    if (s) {
        b = s.value != "";
        s.value = "";
        if (b) searchDelayed(13, view, url);
    }
}

function searchDelayed(key, view, url) {
    viewStr = view
    urlStr = url
    if (key == 13) { //enter was pressed call search() immediately
        clearTimeout(timerId);
        search();
    } else {
        clearTimeout(timerId);
        timerId = setTimeout("search()", 900);
    }
}

function updateGraph(url, rvmid, timeunit) {
    var date = document.getElementById('datepicker');
    if (date) searchDate = date.value;
    
    var date1 = document.getElementById('datepicker1');
    if (date1) endDate = date1.value;

    var smr = document.getElementById('chkbx-smr');
    if (smr) smrValue = smr.checked;
    
    var ean = document.getElementById('chkbx-ean');
    if (ean) eanValue = ean.checked;
    
    var kol = document.getElementById('chkbx-cal');
    if (kol) kolValue = kol.checked;
    
    //console.log("SMR" + smrValue);
    var data = {
        id: rvmid,
        date : searchDate,
        edate : endDate,
        smr : smrValue,
        ean : eanValue,
        kol : kolValue,
        unit : timeunit
    };
    
    var args = {
        type : "POST",
        url : url,
        data : data,
        success : function(result) {
            $(document).append(result);
        }
    };
	$.ajax(args);	
};


function updateGraph1(url, timeunit) {
	var chain = document.getElementById('SearchInput');
    if (chain) vchain = chain.value;
    
    var date = document.getElementById('ndatepicker');
    if (date) searchDate = date.value;
    
    var date1 = document.getElementById('ndatepicker1');
    if (date1) endDate = date1.value;

    var smr = document.getElementById('chkbx-smr1');
    if (smr) smrValue = smr.checked;
    
    var ean = document.getElementById('chkbx-ean1');
    if (ean) eanValue = ean.checked;
    
    var kol = document.getElementById('chkbx-cal1');
    if (kol) kolValue = kol.checked;
    
    //console.log("SMR" + smrValue);
    var data = {
    	chain : vchain,
        date : searchDate,
        edate : endDate,
        smr : smrValue,
        ean : eanValue,
        kol : kolValue,
        unit : timeunit
    };
    
    var args = {
        type : "POST",
        url : url,
        data : data,
        success : function(result) {
            $(document).append(result);
        }
    };
	$.ajax(args);	
};

var xhr = null;

function GraphRequest(url, timeunit) {
	var searchtag = document.getElementById('SearchInput');
    if (searchtag) searchtxt = searchtag.value;
    
    var date = document.getElementById('ndatepicker');
    if (date) searchDate = date.value;
    
    var date1 = document.getElementById('ndatepicker1');
    if (date1) endDate = date1.value;

    var smr = document.getElementById('chkbx-smr1');
    if (smr) smrValue = smr.checked;
    
    var ean = document.getElementById('chkbx-ean1');
    if (ean) eanValue = ean.checked;
    
    var kol = document.getElementById('chkbx-cal1');
    if (kol) kolValue = kol.checked;
    
    //console.log("SMR" + smrValue);
    var data = {
    	searchtxt : searchtxt,
        startdate : searchDate,
        enddate : endDate,
        smr : smrValue,
        ean : eanValue,
        kol : kolValue,
        unit : timeunit
    };
    
    var args = {
        type : "POST",
        url : url,
        data : data,
        success : function(result) {
            $(document).append(result);
        }
    };
    
    if(xhr != null) {
    	xhr.abort();
    }
    
	xhr = $.ajax(args);
	
	xhr.success(function() {
		xhr = null;
	});
	
	xhr.complete(function() {
		xhr = null;
	});
	
	xhr.done(function() {
		xhr = null;
	});
};



function search(p, v, u, s, d) {

	// if there's a search request then the graph is reset to blank
	canvas =  document.getElementById('statistic-graph');
    if (canvas && canvas.getContext("2d")) {
        var ctx = canvas.getContext("2d");
        ctx.clearRect(0, 0, canvas.width, canvas.height);
    }

    if (v) viewStr = v;
    if (u) urlStr = u;
    if (s) sortStr = s;
    if (typeof d !== 'undefined') directionStr = d;

    searchStr = document.getElementById('SearchInput').value;
    searchDate = "";
    var date = document.getElementById('datepicker');
    if (date) searchDate = date.value
        
    inactives = 0;
    if (document.getElementById('inactives')) {
        inactives = document.getElementById('inactives').checked
    }
    var r = document.getElementById('page_results');
    results=20;
    if (r) results = r.value;
    var data = {
        name : searchStr,
        date : searchDate,
        page : p,
        view : viewStr,
        sort : sortStr,
        direction  : directionStr,
        inactives : inactives,
        results : results
    };
    var args = {
        type : "POST",
        url : urlStr,
        data : data,
        success : function(result) {
            if ( document.getElementById('js-response')==null ) {
                document.getElementById('searchResult').innerHTML = result;
                tabTooltip("tooltips");
            }else{
                eval( result );
            };
        }
    };
    $.ajax(args);
};

function filterChain(u, v) {
    var args = {
        type : "POST",
        url : u,
        data : { id: document.getElementById('id_organisation').value},
        success : function(result) {
                document.getElementById('div_chain').innerHTML = result;
                if (v != null) chain = v;
                if (chain != null) {
                    e = document.getElementById('id_chain');
                    for (i=0; i < e.length; i++) { if (e[i].value == chain) {e.selectedIndex = i; break;} }
                }
            }
    };
    $.ajax(args);
};

function monkeyPatchAutocomplete() {
    $.ui.autocomplete.prototype._renderItem = function( ul, item) {
        var re = new RegExp(this.term, "i");
        var m = item.label.match(re);
        if (m == null) return;
        var t = item.label.replace(re,"<span style='font-weight:bold;color:Red;'>" +
        m[0] +
        "</span>");
        return $( "<li></li>" )
        .data( "item.autocomplete", item )
        .append( "<a>" + t + "</a>" )
        .appendTo( ul );
    };
}

function buttonLink(url, question) {
    if (question) {
        res = confirm(question);
        if (!res)
            return;
    }
    location.href=url
}

$(document).ready(function() {
    $("#spinner").bind("ajaxSend", function() {
        $(this).show();
    }).bind("ajaxStop", function() {
        $(this).hide();
        addjQueryCss();
    }).bind("ajaxError", function() {
        $(this).hide();
    });
    addjQueryCss();
});

window.onDomReady = initReady;
// Initialize event
function initReady(fn) {
    //W3C-compliant browser
    if (document.addEventListener) {
        document.addEventListener("DOMContentLoaded", fn, false);
    }
}

window.onDomReady(onReady);

//do when DOM is ready
function onReady() {
    //clear all forms after reload
    elementsForms = document.getElementsByTagName("input");
    for ( var i = 0; i < document.getElementsByTagName("input").length; i++) {
        //                     elementsForms[i].value = "";
    }
    
    monkeyPatchAutocomplete();
}
$(document)
.ajaxSend(
    function(event, xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for ( var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie
                        .substring(name.length + 1));
                        break;
                }
        }
    }
    return cookieValue;
    }
    
    
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0,
                                           origin.length + 1) == origin + '/')
        || (url == sr_origin || url.slice(0,
                                          sr_origin.length + 1) == sr_origin
                                          + '/') ||
                                          // or any other URL that isn't scheme relative or absolute i.e relative.
                                          !(/^(\/\/|http:|https:).*/.test(url));
    }


    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }


    if (!safeMethod(settings.type)
        && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken",
                             getCookie('csrftoken'));
        }
    });


function addjQueryCss() {
    $( "input:submit, button" ).button();
}



