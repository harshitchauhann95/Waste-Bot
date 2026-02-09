// Simulate waste classification
const uploadBox = document.querySelector('.upload-box');
const resultBox = document.getElementById('result');

uploadBox.addEventListener('click', () => {
  // Simulate API call
  setTimeout(() => {
    resultBox.classList.remove('hidden');
  }, 1000);
});