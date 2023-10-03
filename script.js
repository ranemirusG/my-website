var currentImageIndex = 0; // Initialize the current image index

// Manually list image filenames and captions
var imageInfo = [
    { src: "images/campo-duran.jpg", caption: "Campo Durán, Salta, Argentina. July 2023" },
    { src: "images/jardi-del-turia.jpg", caption: "Jardí del Túria, València. October 2023" },
    { src: "images/pic-bash.jpg", caption: "Me and my cousin playing AOE circa 2004" },
    // Add more images and captions as needed
];

// Function to handle the "Esc" key press
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeModal();
    } else if (event.key === 'ArrowLeft') {
        previousImage();
    } else if (event.key === 'ArrowRight') {
        nextImage();
    }
});

// Function to open the modal
function openModal() {
    var modal = document.getElementById('imageModal');
    modal.style.display = 'block';

    // Check if buttons already exist, if not, add them
    var modalButtons = document.querySelector('.modal-buttons');
    if (!modalButtons) {
        addModalButtons(); // Add navigation buttons
    }

    showImage(currentImageIndex); // Display the initial image
}

// Function to close the modal
function closeModal() {
    var modal = document.getElementById('imageModal');
    modal.style.display = 'none';
}

// Function to go to the previous image
function previousImage() {
    currentImageIndex = (currentImageIndex - 1 + imageInfo.length) % imageInfo.length;
    showImage(currentImageIndex);
}

// Function to go to the next image
function nextImage() {
    currentImageIndex = (currentImageIndex + 1) % imageInfo.length;
    showImage(currentImageIndex);
}

// Function to add buttons for cycling through images within the modal
function addModalButtons() {
    var modal = document.getElementById('imageModal');
    var prevButton = document.createElement('button');
    var nextButton = document.createElement('button');

    prevButton.textContent = 'Previous';
    prevButton.className = 'modal-button';
    prevButton.onclick = function() {
        previousImage();
    };

    nextButton.textContent = 'Next';
    nextButton.className = 'modal-button';
    nextButton.onclick = function() {
        nextImage();
    };

    modal.appendChild(prevButton);
    modal.appendChild(nextButton);
}

// Function to display the current image and caption
function showImage(index) {
    var modalImage = document.getElementById('modalImage');
    var imageCaption = document.getElementById('imageCaption');

    modalImage.src = imageInfo[index].src;
    modalImage.alt = imageInfo[index].caption;
    imageCaption.textContent = imageInfo[index].caption;
}
