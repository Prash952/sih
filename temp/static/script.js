async function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const resultDiv = document.getElementById('result');
    
    if (fileInput.files.length === 0) {
        resultDiv.innerText = 'Please select an image file.';
        return;
    }
    
    const formData = new FormData();
    formData.append('image', fileInput.files[0]);

    try {
        const response = await fetch('/classify', {  // Use relative URL
            method: 'POST',
            body: formData
        });
        
        const result = await response.json();
        resultDiv.innerText = `The waste type is: ${result.prediction}`;
    } catch (error) {
        console.error('Error:', error);
        resultDiv.innerText = 'An error occurred while classifying the image.';
    }
}
