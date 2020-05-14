
export function show_rides(response) {
    if (typeof(response) === 'string') {
                console.log("Inside show_rides function");
                window.location.href = '/show_rides';
                var div = document.createElement("div");
                div.className = "container";
                document.body.appendChild(div);
            }
}