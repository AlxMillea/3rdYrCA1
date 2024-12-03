// Toggle search bar visibility
function toggleSearchBar() {
    const searchBar = document.getElementById('search-bar');
    searchBar.classList.toggle('show'); // Add/remove 'show' class to toggle visibility
    if (searchBar.classList.contains('show')) {
        searchBar.focus(); // Automatically focus on the input when shown
    }
}

// Sticky navbar on scroll
window.addEventListener('scroll', () => {
    const navbar = document.querySelector('nav.navbar');
    if (window.scrollY > 100) {
        navbar.classList.add('sticky-navbar');
    } else {
        navbar.classList.remove('sticky-navbar');
    }
});

    // Bar Chart Example
    var ctxBar = document.getElementById("myBarChart").getContext('2d');
    var myBarChart = new Chart(ctxBar, {
    type: 'bar',
    data: {
    labels: ["January", "February", "March", "April", "May", "June"],
    datasets: [{
    label: "Sales",
    backgroundColor: "rgba(2,117,216,1)",
    borderColor: "rgba(2,117,216,1)",
    data: [4215, 5312, 6251, 7841, 9821, 14984],
}],
},
    options: {
    scales: {
    x: {grid: {display: false}},
    y: {grid: {color: "rgba(0, 0, 0, .125)"}}
},
    plugins: {
    legend: {display: false}
}
}
});

    // Pie Chart Example
    var ctxPie = document.getElementById("myPieChart").getContext('2d');
    var myPieChart = new Chart(ctxPie, {
    type: 'pie',
    data: {
    labels: ["Direct", "Referral", "Social"],
    datasets: [{
    data: [55, 30, 15],
    backgroundColor: ['#007bff', '#dc3545', '#ffc107'],
}],
},
});
