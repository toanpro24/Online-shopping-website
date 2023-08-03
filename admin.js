document.addEventListener('DOMContentLoaded', function() {
    const productIDSearch = document.getElementById('ProductID');
    const productNameSearch = document.getElementById('ProductName');
    const categoryIDSearch = document.getElementById('CategoryID');

    function performSearch(column, searchTerm) {
        data = {};
        data['column'] = column;
        data['searchTerm'] = searchTerm;
        // fetch("/search", {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json', 
        //     },
        //     body: JSON.stringify(data),
        // });
        const queryString = encodeURIComponent(JSON.stringify(data));

        // Make the GET request with JSON data
        fetch(`/search?data=${queryString}`, {
            method: 'GET',
        });
        location.href = `/search?data=${queryString}`;
    }

    function handleEnterKey(event, column) {
        if (event.key === 'Enter') {
            const searchTerm = event.target.value;
            performSearch(column, searchTerm);
        }
    }
    
    if (productIDSearch) {
        productIDSearch.addEventListener('keydown', event => handleEnterKey(event, 'ProductID'));
    }
    
    if (productNameSearch) {
        productNameSearch.addEventListener('keydown', event => handleEnterKey(event, 'ProductName'));
    }
    
    if (categoryIDSearch) {
        categoryIDSearch.addEventListener('keydown', event => handleEnterKey(event, 'CategoryID'));
    }
});
document.addEventListener('DOMContentLoaded', function() {
    const productIDSearch = document.getElementById('ProductID');
    const productNameSearch = document.getElementById('ProductName');
    const categoryIDSearch = document.getElementById('CategoryID');

    function performSearch(column, searchTerm) {
        data = {};
        data['column'] = column;
        data['searchTerm'] = searchTerm;
        // fetch("/search", {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json', 
        //     },
        //     body: JSON.stringify(data),
        // });
        const queryString = encodeURIComponent(JSON.stringify(data));

        // Make the GET request with JSON data
        fetch(`/search?data=${queryString}`, {
            method: 'GET',
        });
        location.href = `/search?data=${queryString}`;
    }

    function handleEnterKey(event, column) {
        if (event.key === 'Enter') {
            const searchTerm = event.target.value;
            performSearch(column, searchTerm);
        }
    }
    
    if (productIDSearch) {
        productIDSearch.addEventListener('keydown', event => handleEnterKey(event, 'ProductID'));
    }
    
    if (productNameSearch) {
        productNameSearch.addEventListener('keydown', event => handleEnterKey(event, 'ProductName'));
    }
    
    if (categoryIDSearch) {
        categoryIDSearch.addEventListener('keydown', event => handleEnterKey(event, 'CategoryID'));
    }
});
document.addEventListener('DOMContentLoaded', function() {
    const editButtons = document.querySelectorAll('.edit-button');

    function handleEditClick(event) {
        const row = event.target.closest('tr');
        const cells = row.querySelectorAll('td');
        
        for (let i = 0; i < cells.length - 1; i++) {
            if(i == 1){
                continue;
            }
            const cell = cells[i];
            const cellContent = cell.textContent;
            const input = document.createElement('input');
            input.type = 'text';
            input.value = cellContent;
            cell.textContent = '';
            cell.appendChild(input);
        }

        event.target.remove();

        const saveButton = document.createElement('button');
        saveButton.className = 'save-button';
        saveButton.textContent = 'Save';
        saveButton.addEventListener('click', function() {
            handleSaveClick(row);
        });
        row.querySelector('td:last-child').appendChild(saveButton);
    }

    function handleSaveClick(row) {
        const inputs = row.querySelectorAll('input');
        const data = {};
        for (let i = 0; i < inputs.length; i++) {
            const input = inputs[i];
            const columnName = input.parentElement.getAttribute('data-column-name');
            const inputValue = input.value;
            data[columnName] = inputValue;
        }

        fetch('/update', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
       
        for (let i = 0; i < inputs.length; i++) {
            const input = inputs[i];
            const inputValue = input.value;
            const cell = input.parentElement;
            cell.textContent = inputValue;
        }

        const editButton = document.createElement('button');
        editButton.className = 'edit-button';
        editButton.textContent = 'Edit';
        editButton.addEventListener('click', handleEditClick(row));
        row.querySelector('td:last-child').appendChild(editButton);          
        row.querySelector('.save-button').remove();
    }

    editButtons.forEach(button => {
        button.addEventListener('click', function() {
            handleEditClick(button);
        });
    });
});