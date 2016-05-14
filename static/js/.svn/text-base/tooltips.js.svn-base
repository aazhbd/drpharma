function tabTooltip(id) {
    this.showTooltip = function(e) {
        var th = headers.firstChild;
        while (th && th.cellIndex != curTarget.cellIndex)
        th = th.nextSibling;
        if (!th) return;

        if (!th.title) th = th.firstChild;
        if (!th || !th.title) return;

        var x = document.all ? e.x + tooltip.offsetParent.scrollLeft : e.pageX;
        var y = document.all ? e.y + tooltip.offsetParent.scrollTop  : e.pageY;
        tooltip.style.left = x +  0 + "px";
        tooltip.style.top  = y + 20 + "px";
        tooltip.style.display = "block";
        tooltip.innerHTML = th.title;
    }

    this.hideTooltip = function() {
        tooltip.style.display = "none";
    }

    this.updateTooltip = function(e) {
        if (!e) var e = window.event;
        var target = e.target || e.srcElement;
        if (target == curTarget) return;

        obj.hideTooltip();
        if (!/td/i.test(target.tagName)) return;

        curTarget = target;
        obj.showTooltip (e);
    }

    var obj = this;
    var curTarget = null;

    var headers = document.getElementById(id);
    var table = headers;
    while (table && table.tagName != "TABLE")
    table = table.parentNode;
    if (!table) return;

    var tooltip = document.createElement("div");
    tooltip.className = "tooltip";
    document.body.appendChild(tooltip);

    table.onmousemove = this.updateTooltip;
    table.onmouseout = this.hideTooltip;
}