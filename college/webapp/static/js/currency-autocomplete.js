$(function(){

	var col=document.getElementById("college").value;

  var college = [
    { value: col, data: col },
    
  ];
  
  // setup autocomplete function pulling from currencies[] array
  $('#autocomplete').autocomplete({
    lookup: college,
    onSelect: function (suggestion) {
      
    }
  });
  

});