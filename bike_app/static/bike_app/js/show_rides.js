
export function show_rides(response) {
    if (typeof(response) === 'string') {
                var div = document.createElement("div");
                div.className = "container";
                document.body.appendChild(div);
                window.location.replace('/show_rides');

            }
}