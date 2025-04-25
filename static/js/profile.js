const bioButtonEdit = document.querySelector('.df34kas64kd3');
const bioTextDiv = document.getElementById('bioTextDiv');
const bioInputDiv = document.getElementById('bioInputDiv');
const bioButtonSave = document.querySelector('.df34kaEReER4kEd3');
const bioInput = document.querySelector('.bioInput');
const bio_p = document.querySelector('.bio_p');


(function () {
    bioButtonEdit.addEventListener('click', () => {
        bioTextDiv.style.display = 'none';
        bioInputDiv.style.display = 'block';
    });
})();

// get csrftoken


const updateUI = () => {
    bio_p.innerHTML = bioInput.value;
    bioTextDiv.style.display = 'block';
    bioInputDiv.style.display = 'none';
};

const handler = async (id) => {
    if (localStorage.getItem('bio') !== bioInput.value) {
        const result = await Fetch(id)

        if (result.status === 200) {
            updateUI();
            localStorage.setItem('bio', bioInput.value);
        }
    } else {
        updateUI();
    }
};
