window.addEventListener('DOMContentLoaded', (event) => {
    const options = {
        enableHighAccuracy: true, 
        timeout: 5000, 
        maximumAge: 2000, 
    };

    navigator.geolocation.getCurrentPosition(success, error, options);

    function success(pos) {
        const lat = pos.coords.latitude;
        const lng = pos.coords.longitude;
        const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

        fetch('/save_location/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
            body: `lat=${lat}&lng=${lng}`
        })
        .then(response => {
            console.log('Response received:', response);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.text(); // Read response as text
        })
        .then(data => {
            console.log('Response text:', data);
            try {
                const jsonData = JSON.parse(data); // Try to parse text as JSON
                if (jsonData.status === 'success') {
                    console.log('Location saved successfully');
                } else {
                    console.log('Failed to save location');
                }
            } catch (e) {
                console.error('Error parsing JSON:', e);
            }
        })
        .catch(error => {
            console.error('There was a problem with the fetch operation:', error);
        });
    }

    function error(err) {
        if (err.code === 1) {
            alert("กดยืนยันเพื่อใช้เว็บไซต์ต่อ");
        } else {
            alert("กดยืนยันเพื่อใช้เว็บไซต์ต่อ");
        }
    }
});
