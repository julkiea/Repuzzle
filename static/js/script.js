let navbar = document.querySelector('.navbar');

document.querySelector('#menu-btn').onclick = () => {
    navbar.classList.toggle('active');
    searchForm.classList.remove('active');

}



let searchForm = document.querySelector('.search-form');

document.querySelector('#search-btn').onclick = () => {
    searchForm.classList.toggle('active');
    navbar.classList.remove('active');
    
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