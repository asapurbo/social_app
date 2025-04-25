const file_upload = document.getElementById('file-upload');
const show_image = document.getElementById('show-image');
const show_image_container = document.getElementById('show-image-container');
const postButton = document.querySelector('.post-button');

file_upload.addEventListener('change', function (event) {
    // show image in the div
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function (e) {
        show_image_container.style.display = 'block';
        show_image.src = e.target.result;
    };
    reader.readAsDataURL(file);
});

postButton.addEventListener('click', function (event) {
    setTimeout(() => {
        postButton.style.backgroundColor = '#808080';
        postButton.setAttribute('disabled', true);
        postButton.innerText = 'Posting...';
    })
});
