/*About Us*/
function openAU() {
  document.getElementById("mySidenavAU").style.width = "20%";
}

function closeAU() {
  document.getElementById("mySidenavAU").style.width = "0";
}
/*contact us*/ 
function openNav() {
    document.getElementById("mySidenav").style.width = "23%";
  }
  
  function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
  }

/*Format validation*/
$("#upfile").change(function() {
    var valimg = document.getElementById("upfile");
    try {
    var extension = valimg.files[0].name.substring(valimg.files[0].name.lastIndexOf('.')+1).toLowerCase()

    if ((extension == 'jpg') || (extension == 'png') || (extension == 'jpeg')) {}
    else {
        document.getElementById("upfile").value = "";
    }}
    catch(err){}
})

/*Preview Img*/
const upfile = document.getElementById("upfile");
const previewContainer = document.getElementById("imgPreview");
const previewImg = previewContainer.querySelector(".image-preview__image");
const previewDefaultText = previewContainer.querySelector(".image-preview__default-text");

upfile.addEventListener("change", function() {
const file = this.files[0];
if (file) {
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

function fileDel() {
    console.log("file Del running")
}