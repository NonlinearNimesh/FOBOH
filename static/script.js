document.getElementById('restaurantForm').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const restaurantName = document.getElementById('restaurantName').value;
    
    fetch('/recommend', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `restaurant_name=${restaurantName}`
    })
    .then(response => response.json())
    .then(data => {
        const resultDiv = document.getElementById('result');
        resultDiv.innerHTML = `<h2>Recommended Ingredients:</h2><ul>${data.ingredients.map(ingredient => `<li>${ingredient}</li>`).join('')}</ul>`;
    })
    .catch(error => console.error('Error:', error));
});
