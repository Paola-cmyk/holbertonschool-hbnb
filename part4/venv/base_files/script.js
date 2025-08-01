document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('login-form');
  
    if (loginForm) {
      loginForm.addEventListener('submit', async (e) => {
        e.preventDefault();
        const email = loginForm.email.value;
        const password = loginForm.password.value;
  
        try {
          const response = await fetch('https://your-api-url/login', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ email, password })
          });
  
          if (response.ok) {
            const data = await response.json();
            document.cookie = `token=${data.access_token}; path=/`;
            window.location.href = 'index.html';
          } else {
            alert('Login failed');
          }
        } catch (err) {
          console.error('Login Error:', err);
        }
      });
    }
  });

  function getCookie(name) {
    const match = document.cookie.match(new RegExp('(^| )' + name + '=([^;]+)'));
    return match ? match[2] : null;
  }
  
  async function fetchPlaces(token) {
    const response = await fetch('https://your-api-url/places', {
      headers: { 'Authorization': `Bearer ${token}` }
    });
  
    const places = await response.json();
    displayPlaces(places);
  }
  
  function displayPlaces(places) {
    const list = document.getElementById('places-list');
    list.innerHTML = '';
  
    places.forEach(place => {
      const div = document.createElement('div');
      div.className = 'place-card';
      div.setAttribute('data-price', place.price);
      div.innerHTML = `
        <h3>${place.name}</h3>
        <p>$${place.price} per night</p>
        <a class="details-button" href="place.html?id=${place.id}">View Details</a>
      `;
      list.appendChild(div);
    });
  }
  
  function checkAuthAndLoad() {
    const token = getCookie('token');
    const loginLink = document.getElementById('login-link');
  
    if (!token) {
      loginLink.style.display = 'block';
    } else {
      loginLink.style.display = 'none';
      fetchPlaces(token);
    }
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    checkAuthAndLoad();
  
    document.getElementById('price-filter').addEventListener('change', function () {
      const selected = this.value;
      const cards = document.querySelectorAll('.place-card');
  
      cards.forEach(card => {
        const price = parseFloat(card.getAttribute('data-price'));
        card.style.display = (selected === 'All' || price <= parseFloat(selected)) ? 'block' : 'none';
      });
    });
  });

  function getPlaceIdFromURL() {
    const params = new URLSearchParams(window.location.search);
    return params.get('id');
  }
  
  async function fetchPlaceDetails(token, placeId) {
    const res = await fetch(`https://your-api-url/places/${placeId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
  
    const place = await res.json();
    displayPlaceDetails(place);
  }
  
  function displayPlaceDetails(place) {
    const container = document.getElementById('place-details');
    container.innerHTML = `
      <h2>${place.name}</h2>
      <p>Host: ${place.host}</p>
      <p>Price: $${place.price}</p>
      <p>${place.description}</p>
      <p>Amenities: ${place.amenities.join(', ')}</p>
      <div class="reviews">
        ${place.reviews.map(review => `
          <div class="review-card">
            <p>${review.user}: ${review.comment}</p>
            <small>Rating: ${review.rating}</small>
          </div>
        `).join('')}
      </div>
    `;
  }
  
  document.addEventListener('DOMContentLoaded', () => {
    const token = getCookie('token');
    const placeId = getPlaceIdFromURL();
  
    if (token) {
      document.getElementById('add-review').style.display = 'block';
      document.querySelector('#add-review a').href = `add_review.html?id=${placeId}`;
    }
  
    fetchPlaceDetails(token, placeId);
  });

  document.addEventListener('DOMContentLoaded', () => {
    const token = getCookie('token');
    const placeId = new URLSearchParams(window.location.search).get('id');
  
    if (!token) return window.location.href = 'index.html';
  
    const form = document.getElementById('review-form');
  
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const review = form.review.value;
  
      const res = await fetch(`https://your-api-url/places/${placeId}/reviews`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({ text: review })
      });
  
      if (res.ok) {
        alert('Review submitted!');
        form.reset();
      } else {
        alert('Error submitting review');
      }
    });
  });
  