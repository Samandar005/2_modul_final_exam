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

function createStars() {
    const background = document.querySelector('.cosmic-background');
    for (let i = 0; i < 100; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        star.style.width = `${Math.random() * 3}px`;
        star.style.height = star.style.width;
        star.style.left = `${Math.random() * 100}%`;
        star.style.top = `${Math.random() * 100}%`;
        star.style.animationDelay = `${Math.random() * 5}s`;
        background.appendChild(star);
    }
}
createStars();

// Live profile picture preview
document.getElementById("id_image").addEventListener("change", function(event) {
    let reader = new FileReader();
    reader.onload = function() {
        document.getElementById("profilePreview").src = reader.result;
    };
    reader.readAsDataURL(event.target.files[0]);
});