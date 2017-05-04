function validate() {
	var x = document.forms.input.username.value;
	var y = document.forms.input.password.value;
	var atPos = x.indexOF("@")
	var dotPos = x.lastIndexOf(".");

	
	
	if(atPos < 1)
		alert("This is not a valid email address!");
	else
		alert("Success!")
	if(dotPos < atPos+2)
		alert("This is not a valid email address!");
	else
		alert("Success!")
	if(dotPos + 2 > x.length)
		alert("This is not a valid email address!");
	else
		alert("Success!")
	if(y.length > 6)
		alert
		
}