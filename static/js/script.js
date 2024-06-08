document.addEventListener('DOMContentLoaded', (event) => {
    const tabs = document.querySelectorAll('#myTab .nav-item');
    const BorderTabs = document.querySelectorAll('#myTab .nav-link');
    
    tabs.forEach(tab => {
      tab.addEventListener('click', function() {
        // Remove active class from all tabs
        tabs.forEach(t => t.classList.remove('active'));
        // Add active class to the clicked tab
        this.classList.add('active');
      });
    });

    BorderTabs.forEach(tab => {
        tab.addEventListener('click', function() {

            // Remove active class from all tabs
            BorderTabs.forEach(t => t.classList.remove('active'));

            // Add active class to the clicked tab
            this.classList.add('active');
        })
    })
});
  