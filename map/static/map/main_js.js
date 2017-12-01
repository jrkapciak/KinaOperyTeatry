function map_init_basic (map, options)
        {
        $.ajax
            ({
	        url:'http://localhost:8000/api/places/',
	        type:'GET',
	        data:'json',
            }).done(
                    function(response)
                        {
                        var today = new Date();
                        today = today.getDate() + "." + today.getMonth() + "." + today.getFullYear();
                        $.each(response, function(i,place)
                            {
                            $(place.shows).each(function(index){
                                if (place.shows[index].date == "24.11.2017"){
                                    $('#accordion').append('<h3></h3><div><p></p></div>')
                                    var marker = L.marker([place.lat,place.long])
                                    $("#accordion").accordion("refresh");
                                    $("h3").eq(i).text(place.name);
                                    alert($("h3").eq(i).text())
                                    marker.setBouncingOptions({
                                    bounceHeight : 10,
                                    bounceSpeed  : 80,
                                    exclusive    : true,
                                        }).on('click', function() {
                                    this.toggleBouncing();
                                        $("h3").eq(i).click()
                                     });
                                    marker.addTo(map);
                                   return false}else{}

                                });
                            })
                        }
                    );
             };




