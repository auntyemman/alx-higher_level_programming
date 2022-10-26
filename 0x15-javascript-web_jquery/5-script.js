// A JavaScript script that adds a <li> element to a list when the user clicks on the tag DIV#add_item
$('DIV#add_item').click(function () {
    $('li').append('<li>Item</li>')
});