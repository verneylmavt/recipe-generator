$(document).ready(function() {
    $("#ingredients").autocomplete({
        source: function(request, response) {
            $.ajax({
                url: "/api/ingredients",
                type: "GET",
                dataType: "json",
                success: function(data) {
                    var filtered = $.grep(data, function(item) {
                        return item.toLowerCase().startsWith(request.term.toLowerCase());
                    });
                    response(filtered);
                },
                error: function() {
                    response([]);
                }
            });
        },
        minLength: 1,
        select: function(event, ui) {
            var terms = this.value.split(/,\s*/);
            terms.pop();
            terms.push(ui.item.value);
            terms.push("");
            this.value = terms.join(", ");
            return false;
        }
    });

    $('a[href^="#"]').on('click', function(event) {
        var target = this.hash;
        if (target) {
            event.preventDefault();
            $('html, body').animate({
                scrollTop: $(target).offset().top
            }, 800, function(){
                window.location.hash = target;
            });
        }
    });
});