/*!
* Start Bootstrap - Clean Blog v6.0.9 (https://startbootstrap.com/theme/clean-blog)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-clean-blog/blob/master/LICENSE)
*/

function displaySelectedImage(event, elementId) {
    const selectedImage = document.getElementById(elementId);
    const fileInput = event.target;

    if (fileInput.files && fileInput.files[0]) {
        const reader = new FileReader();

        reader.onload = function(e) {
            selectedImage.src = e.target.result;
        };

        reader.readAsDataURL(fileInput.files[0]);
    }
}

async function loadColorData() {
    const fileInput = document.getElementById('customFile1');
    
    if (fileInput.files && fileInput.files[0]) {
        const formData = new FormData();
        formData.append('image', fileInput.files[0]);

        try {
            const response = await fetch('http://127.0.0.1:5000/colors', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();
            console.log(data);  // Check what data you are getting back
            displayColorList(data);
        } catch (error) {
            console.error('Error fetching color data:', error);
        }
    }
}

function displayColorList(colors) {
    const colorList1Div = document.getElementById('colorList1');
    const colorList2Div = document.getElementById('colorList2');
    
    // Clear previous color lists
    colorList1Div.innerHTML = '';
    colorList2Div.innerHTML = '';

    if (!colors || colors.length === 0) {
        colorList1Div.innerHTML = 'No colors found!';
        colorList2Div.innerHTML = 'No colors found!';
        return;
    }

    // Split colors into two halves
    const midIndex = Math.ceil(colors.length / 2);  // To handle odd number of colors
    const firstHalf = colors.slice(0, midIndex);
    const secondHalf = colors.slice(midIndex);

    // Function to append color boxes
    const appendColorsToColumn = (colorListDiv, colors) => {
        colors.forEach(color => {
            const colorDiv = document.createElement('div');
            colorDiv.style.backgroundColor = color.hex; // Assuming 'hex' contains color code
            colorDiv.innerText = `${color.name} (${color.hex})`;
            colorDiv.classList.add('color-box');
            colorListDiv.appendChild(colorDiv);
        });
    };

    // Populate the two columns
    appendColorsToColumn(colorList1Div, firstHalf);
    appendColorsToColumn(colorList2Div, secondHalf);
}

