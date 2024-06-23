window.addEventListener('scroll', function () {
    const title = document.getElementById('title');
    const maxScroll = window.innerHeight / 2; // Adjust this value as needed
    const scrollPosition = window.scrollY;
    
    // Calculate opacity based on scroll position
    const opacity = Math.max(0, 1 - (scrollPosition / maxScroll));
    
    // Apply the calculated opacity to the title
    title.style.opacity = opacity;
});
