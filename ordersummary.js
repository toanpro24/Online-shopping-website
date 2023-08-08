function handleStatusChange(selectElement, orderID) {
    const selectedValue = selectElement.value;
    const jsonData = {
        orderID: orderID,
        status: selectedValue
    };

    fetch('/updateOrderStatus', {
        method: 'POST',
        headers: {
        'Content-Type': 'application/json'
        },
        body: JSON.stringify(jsonData)
    })
    if (selectedValue === '3') {
        row.remove();
    }
}

  function viewOrderDetails(orderID) {
    window.location.href = `/orderdetails?orderID=${orderID}`;
  }