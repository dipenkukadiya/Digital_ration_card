
function customer() {
	document.getElementById("shopno").disabled = true;
	document.getElementById("shopaddress").disabled = true;
	document.getElementById("rationbooktype").disabled = false;
	document.getElementById("sel").disabled = false;
	document.getElementById("income").disabled = false;
	document.getElementById("gas").disabled = false;
	document.getElementById("electricity").disabled = false;
}

function dealer() {
	document.getElementById("rationbooktype").disabled = true;
	document.getElementById("sel").disabled = true;
	document.getElementById("income").disabled = true;
	document.getElementById("gas").disabled = true;
	document.getElementById("electricity").disabled = true;
	document.getElementById("shopno").disabled = false;
	document.getElementById("shopaddress").disabled = false;
}