document.addEventListener('DOMContentLoaded', function() {
    const tabs = document.querySelectorAll('.nav-item');
    const contentSections = document.querySelectorAll('.content-section');

    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove('active'));
            // Add active class to the clicked tab
            this.classList.add('active');

            // Hide all content sections
            contentSections.forEach(section => section.classList.remove('active'));
            // Show the content section associated with the clicked tab
            const target = this.getAttribute('data-target');
            document.getElementById(target).classList.add('active');
        });
    });
});
