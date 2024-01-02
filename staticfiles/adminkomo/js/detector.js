
document.getElementById('excel').onchange = function() {
 var fileName = this.value.split("\\").pop();
 
 document.getElementById('file-name').innerText = fileName;
}