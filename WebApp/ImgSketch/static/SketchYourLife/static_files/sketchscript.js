
/*Preview Img*/
const upfile = document.getElementById("upfile");
const previewContainer = document.getElementById("imgPreview");
const previewImg = previewContainer.querySelector(".image-preview__image");
const previewDefaultText = previewContainer.querySelector(".image-preview__default-text");

upfile.addEventListener("change", function () {
  var valimg = document.getElementById("upfile");
  try {
    var extension = valimg.files[0].name.substring(valimg.files[0].name.lastIndexOf('.') + 1).toLowerCase()

    if ((extension == 'jpg') || (extension == 'png') || (extension == 'jpeg')) { }
    else {
      document.getElementById("upfile").value = "";
      window.alert("Please enter an image file with .jpg/.png/.jpeg extensions");
    }
  }
  catch (err) { }

  const file = this.files[0];
  if (file) {
<<<<<<< HEAD
    const reader = new FileReader();
    previewDefaultText.style.display = "none";
    previewImg.style.display = "block";


    reader.addEventListener("load", function () {
      previewImg.style.width = "100%";
      previewImg.style.height = "100%";
      previewImg.setAttribute("src", this.result);
    });
    reader.readAsDataURL(file);



  } else { }
});


function ImageCheck() {
  if (upfile.files[0]) { }
  else {
    window.alert("Please choose an Image first");
  }
}
=======
     const reader = new FileReader();
     previewDefaultText.style.display = "none";
     previewImg.style.display = "block"; 
     
  
     reader.addEventListener("load", function() {
          previewImg.style.width = "100%";
          previewImg.style.height = "100%";
          previewImg.setAttribute("src", this.result);
     });
     reader.readAsDataURL(file);
     
     
  
  }else {}
  });
  
  
  function ImageCheck(){
    if(upfile.files[0]){}
    else{
      window.alert("Please choose an Image first");
      }
  }

  (function(){
    var dropzone = document.getElementById("imgPreview");
    dropzone.ondrop = function(e){
      e.preventDefault();
      return false;
    }
    dropzone.ondragover = function(){
      this.className = 'image-preview dragover';
      return false;
    };
    dropzone.ondragleave = function(){
      this.className = 'image-preview';
      return false;
    };
  }());
>>>>>>> 2dc2c1f229cb5653302135704ae720359570bb22
