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
    const deleteButtons = document.querySelectorAll('.delete-button');
    const insertButtons = document.querySelectorAll('.insert-button')


    function handleEditClick(event) {
        const row = event.target.closest('tr'); 
        const cells = row.querySelectorAll('td'); 

        for (let i = 2; i < cells.length - 2; i++) {
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
        saveButton.addEventListener('click', handleSaveClick);
        row.querySelector('td:nth-last-child(2)').appendChild(saveButton);
    }

    function handleSaveClick(event) {
        const row = event.target.closest('tr'); 
        const inputs = row.querySelectorAll('input'); 

        const data = {};
        data['ProductID'] = row.querySelector('td:nth-child(1)').textContent; 
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
        editButton.addEventListener('click', handleEditClick);
        row.querySelector('td:nth-last-child(2)').appendChild(editButton);

        event.target.remove();
    }
    function handleDeleteClick(event) {
        const row = event.target.closest('tr');
        const productID = row.querySelector('td:nth-child(1)').textContent; 
        
        if (window.confirm('Are you fucking sure you want to delete this product?')){
            fetch('/delete', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ 'ProductID': productID }),
            })
            row.remove();
        }
    }

    
    editButtons.forEach(button => {
        button.addEventListener('click', handleEditClick);
    });
    deleteButtons.forEach(button =>{
        button.addEventListener('click', handleDeleteClick);
    });
    function handleCreateClick(event){
        const row = event.target.closest('tr');
        const inputs = row.querySelectorAll('input'); 
        const data = {};
        const imageElement = row.querySelector('td:nth-child(2) img');
        const srcParts = imageElement.src.split('/');
        const filename = srcParts[srcParts.length - 1];
        data['ProductID'] = row.querySelector('td:nth-child(1)').textContent; 
        data['PictureName'] = filename;
        for (let i = 0; i < inputs.length; i++) {
            const input = inputs[i];
            const columnName = input.parentElement.getAttribute('data-column-name');
            const inputValue = input.value;
            data[columnName] = inputValue;
        };
        fetch('/insert', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        for (let i = 0; i < inputs.length; i++) {
            const input = inputs[i];
            const inputValue = input.value;
            
            const cell = input.parentElement;
            cell.textContent = inputValue;
        };

        const editButton = document.createElement('button');
        editButton.className = 'edit-button';
        editButton.textContent = 'Edit';
        editButton.addEventListener('click', handleEditClick);
        row.querySelector('td:nth-last-child(2)').appendChild(editButton);

        event.target.remove();
    }


    function handleInsertClick() {
        const tableBody = document.querySelector('tbody');
        const lastRow = tableBody.lastElementChild;

        const currentProductID = lastRow ? parseInt(lastRow.querySelector('td:nth-child(1)').textContent) : 0;
        const newProductID = currentProductID + 1;
        
        const newRow = document.createElement('tr');
        newRow.innerHTML = `
            <td>${newProductID}</td>
            <td><img src ="Images/product${newProductID}.jpg"></td>
            <td data-column-name = 'ProductName'></td>
            <td data-column-name = 'Description'></td>
            <td data-column-name = 'Price'></td>
            <td data-column-name = 'CategoryID'></td>
            <td data-column-name = 'Quantity'></td>
            <td><button class="create-button">Create</button></td>
            <td><button class="delete-button">Delete</button></td>
        `;
        tableBody.appendChild(newRow);
        const cells = newRow.querySelectorAll('td');
        for (let i = 2; i < cells.length - 2; i++) {
            const cell = cells[i];
            const cellContent = cell.textContent;
            const input = document.createElement('input');
            input.type = 'text';
            input.value = cellContent;
            cell.textContent = '';
            cell.appendChild(input);
        }
            
        
        const deleteButton = newRow.querySelector('.delete-button');
        const createButton = newRow.querySelector('.create-button')

        createButton.addEventListener('click', handleCreateClick);
        
        
        editButtons.forEach(button => {
            button.addEventListener('click', handleEditClick);
        });
        deleteButton.addEventListener('click', function() {
            if (window.confirm('Are you sure you want to delete this row?')) {
                handleDeleteClick(newRow);
            }
        });
    }
    insertButtons.forEach(button => {
        button.addEventListener('click', handleInsertClick);
    });
});
