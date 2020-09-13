
/*Preview Img*/
const upfile = document.getElementById("upfile");
const previewContainer = document.getElementById("imgPreview");
const previewImg = previewContainer.querySelector(".image-preview__image");
const previewDefaultText = previewContainer.querySelector(".image-preview__default-text");
const compressedImg = document.createElement("img");

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
     const reader = new FileReader();
     previewDefaultText.style.display = "none";
     previewImg.style.display = "block"; 
     
  
     reader.addEventListener("load", function() {
          previewImg.style.width = "100%";
          previewImg.style.height = "100%";
          previewImg.setAttribute("src", this.result);

          previewImg.onload = function(e){
            const canvas = document.createElement("canvas");
            const MAX_WIDTH = e.target.width*0.7;

            const scaleFactor = MAX_WIDTH/e.target.width;
            canvas.width = MAX_WIDTH;
            canvas.height = e.target.height * scaleFactor;

            const ctx = canvas.getContext("2d");

            const compressedImg = ctx.canvas.toDataURL(e.target,"image/*",0.3);

            console.log("this is compressed"+compressedImg);
            document.getElementById("upfile").value = compressedImg;

          }
          
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

