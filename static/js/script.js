let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () => {
    navbar.classList.toggle('active');
    searchForm.classList.remove('active');
    user.classList.remove('active');
    categories.classList.remove('active');
}

let user = document.querySelector('.user-profile');

document.querySelector('#user-btn').onclick = () => {
    user.classList.toggle('active');
    searchForm.classList.remove('active');
    navbar.classList.remove('active');
    categories.classList.remove('active');
}

let categories = document.querySelector('.categories-menu');

document.querySelector('#categories-btn').onclick = () => { 
    categories.classList.toggle('active');
    searchForm.classList.remove('active');
    navbar.classList.remove('active');
    user.classList.remove('active');
}

let searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active');
    navbar.classList.remove('active');
    user.classList.remove('active');
    categories.classList.remove('active');
    
}

window.onscroll = () => {
    navbar.classList.remove('active');
    searchForm.classList.remove('active');
}


document.querySelectorAll('.close-btn').forEach(function(button) {
    button.onclick = function() {
      const alert = this.parentElement;
      alert.classList.add('fadeout');
      setTimeout(function() {
        alert.style.display = 'none';
      }, 600);
    };
  });


function confirmDeletion() {
    return confirm("Czy na pewno chcesz usunąć puzzle?");
}