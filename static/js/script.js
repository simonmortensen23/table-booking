var m = document.getElementsByClassName("messages");  // Return an array

setTimeout(function(){
   if (m && m.length) {
       m[0].classList.add('hide');
   }
}, 3000);
