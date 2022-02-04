var myIndex = 0;
      var myInd = 0;
        
      carousel();
      carousel2();

      function carousel() {
        var i;
        var x = document.getElementsByClassName("mySlides");
        for (i = 0; i < x.length; i++) {
          x[i].style.display = "none";  
        }
        myIndex++;
        if (myIndex > x.length) {myIndex = 1}    
        x[myIndex-1].style.display = "block";  
        setTimeout(carousel, 3000); // Change image every 4 seconds
      }

      function carousel2() {
        var u;
        var l = document.getElementsByClassName("mySlips");
        for (u = 0; u < l.length; u++) {
          l[u].style.display = "none";  
        }
        myInd++;
        if (myInd > l.length) {myInd = 1}    
        l[myInd-1].style.display = "block";  
        setTimeout(carousel2, 3000); // Change image every 4 seconds
      }
      