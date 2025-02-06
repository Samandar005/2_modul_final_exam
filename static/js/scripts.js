document.addEventListener("DOMContentLoaded", function() {
    const fileInput = document.querySelector("input[name='image']");
    const imagePreview = document.getElementById("imagePreview");
    const placeholderIcon = document.getElementById("placeholderIcon");

    fileInput.addEventListener("change", function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                imagePreview.src = e.target.result;
                imagePreview.classList.remove("hidden");
                if (placeholderIcon) {
                    placeholderIcon.classList.add("hidden");
                }
            };
            reader.readAsDataURL(file);
        } else {
            imagePreview.classList.add("hidden");
            if (placeholderIcon) {
                placeholderIcon.classList.remove("hidden");
            }
        }
    });
});