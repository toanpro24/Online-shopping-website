document.addEventListener('DOMContentLoaded', function() {
    const ProductIDSearch = document.getElementById("ProductID");
    const CategoryIDSearch = document.getElementById('CategoryID');
    const ProductNameSearch= document.getElementById('ProductName');
    
    function performSearch(column, searchTerm) {
        data = {}
        data['col'] = column
        data['searchterm'] = searchTerm
        fetch('/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .catch(error => console.error('Error:', error));
        location.reload();
    }


    ProductIDSearch.addEventListener('keyup', function(event) {
        const searchTerm = event.target.value;
        performSearch('ProductID', searchTerm);
    });

    CategoryIDSearch.addEventListener('keyup', function(event) {
        const searchTerm = event.target.value;
        performSearch('CategoryID', searchTerm);
    });

    ProductNameSearch.addEventListener('keyup', function(event) {
        const searchTerm = event.target.value;
        performSearch('Product name', searchTerm);
    });
});
