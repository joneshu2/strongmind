//
// Hunter Jones
//
// Adds Topping Management functionality
//


function deleteTopping(selectedToppingId) {
  // Get the topping id
  let topping_data = {'topping_id': selectedToppingId};

  // Send data to server via jQuery.ajax({})
  jQuery.ajax({
    url: "/processtoppingdeletion",
    data: topping_data,
    type: "POST",
    success: function (returned_data) {
      returned_data = JSON.parse(returned_data);
      if ('success' in returned_data) {
        window.location.href = "/manage-toppings";
      } else {
        alert("Unable to delete Topping");
      }
    }
  });

}