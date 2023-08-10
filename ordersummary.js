function viewOrderDetails(orderID) {
    window.location.href = `/orderdetails?orderID=${orderID}`;
}



document.addEventListener('DOMContentLoaded', function() {
    const editButtons = document.querySelectorAll('.edit-button');
    function handleEditClick(event) {
        const row = event.target.closest('tr'); 
        const cells = row.querySelectorAll('td'); 
        const statusCell = cells[4];
        const statusText = statusCell.textContent;

        const select = document.createElement('select');
        select.className = 'status-select';

        
        const options = ['Pending', 'Shipped', 'Delivered'];
        for (const optionText of options) {
            const option = document.createElement('option');
            option.value = optionText;
            option.textContent = optionText;
            if (optionText === statusText) {
                option.selected = true;
            }
            select.appendChild(option);
        }

        statusCell.textContent = '';
        statusCell.appendChild(select);

        event.target.remove();

        const saveButton = document.createElement('button');
        saveButton.className = 'save-button';
        saveButton.textContent = 'Save';
        saveButton.addEventListener('click', handleSaveClick);
        row.querySelector('td:nth-last-child(1)').appendChild(saveButton);
    }
    editButtons.forEach(button => {
        button.addEventListener('click', handleEditClick);
    });
    function handleSaveClick(event) {
        const row = event.target.closest('tr'); 
        const selects = row.querySelectorAll('select'); 
    
        const data = {};
        data['OrderID'] = row.querySelector('td:nth-child(1)').textContent; 
        const select = selects[0];
        const selectedValue = select.value;
        data['Status'] = selectedValue;
        fetch('/updatestatus', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        });
        const cell = select.parentElement;
        cell.textContent = selectedValue;
        
        const editButton = document.createElement('button');
        editButton.className = 'edit-button';
        editButton.textContent = 'Edit';
        editButton.addEventListener('click', handleEditClick);
        row.querySelector('td:nth-last-child(1)').appendChild(editButton);
    
        event.target.remove();
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const StatusSelect = document.getElementById('Status');

    let selectedStatus = '';

    // Restore the selected status from the variable
    if (StatusSelect) {
        selectedStatus = localStorage.getItem('selectedStatus') || '';
        StatusSelect.value = selectedStatus;
        
        StatusSelect.addEventListener('change', event => handleSelectChange(event));
    }

    function performSearch(searchTerm) {
        data = {};
        data['Status'] = searchTerm;
        const queryString = encodeURIComponent(JSON.stringify(data));
        fetch(`/search?data=${queryString}`, {
            method: 'GET',
        });

        localStorage.setItem('selectedStatus', searchTerm);
        window.location.href = `/search?data=${queryString}`;
    }

    function handleSelectChange(event) {
        selectedStatus = event.target.value;
        performSearch(selectedStatus);
    }
});
