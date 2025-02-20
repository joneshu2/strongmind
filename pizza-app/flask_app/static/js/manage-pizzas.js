//
// Hunter Jones
//
// Adds Pizza Management functionality
//


function deletePizza(selectedPizzaId) {
  // Get the pizza id
  let pizza_data = {'pizza_id': selectedPizzaId};

  // Send data to server via jQuery.ajax({})
  jQuery.ajax({
    url: "/processpizzadeletion",
    data: pizza_data,
    type: "POST",
    success: function (returned_data) {
      returned_data = JSON.parse(returned_data);
      if ('success' in returned_data) {
        window.location.reload();
      } else {
        alert("Unable to delete Pizza");
      }
    }
  });

}