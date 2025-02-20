//
// Hunter Jones
//
// Adds Individual Pizza Page functionality for adding and removing toppings
//

function removeTopping(selectedToppingId, selectedPizzaId) {
  // Get the topping id
  let topping_data = {'topping_id': selectedToppingId, 'pizza_id': selectedPizzaId};

  // Send data to server via jQuery.ajax({})
  jQuery.ajax({
    url: "/processremovetopping",
    data: topping_data,
    type: "POST",
    success: function (returned_data) {
      returned_data = JSON.parse(returned_data);
      if ('success' in returned_data) {
        window.location.reload();
      } else {
        alert("Unable to Remove Topping");
      }
    }
  });

}

function addTopping(selectedToppingId, selectedPizzaId) {
  // Get the topping id
  let topping_data = {'topping_id': selectedToppingId, 'pizza_id': selectedPizzaId};

  // Send data to server via jQuery.ajax({})
  jQuery.ajax({
    url: "/processaddtopping",
    data: topping_data,
    type: "POST",
    success: function (returned_data) {
      returned_data = JSON.parse(returned_data);
      if ('success' in returned_data) {
        window.location.reload();
      } else {
        alert("Unable to Add Topping");
      }
    }
  });

}