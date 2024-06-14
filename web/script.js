const photoInput = document.getElementById('photoInput');
const previewImage = document.getElementById('previewImage');
const processedImage = document.getElementById('processedImage');

photoInput.addEventListener('change', handleFileChange);

function handleFileChange() {
  const file = photoInput.files[0];
  if (file) {
    previewImage.src = URL.createObjectURL(file);
  }
}

function uploadPhoto() {
  const file = photoInput.files[0];
  if (!file) {
    return;
  }

  const formData = new FormData();
  formData.append('img_file', file);

  fetch('/api/generate_background', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(data => {
    setProcessedImage(data);
  })
  .catch(error => {
    console.error('Ошибка при загрузке фото:', error);
  });
}

function setProcessedImage(backgroundBase64) {
  processedImage.src = `data:image/jpeg;base64,${backgroundBase64}`;
}